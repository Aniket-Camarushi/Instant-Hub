
from django.db.models import ForeignKey
from rest_framework.response import Response
from rest_framework.views import exception_handler 
from rest_framework.exceptions import AuthenticationFailed,NotAuthenticated,PermissionDenied
def getDynamicFormModels():
    return {
        'products':'ProductServices.Products',
        'category':'ProductServices.Categories',
        'warehouse' : 'InventoryServices.Warehouse',
    }


def getSuperAdminDynamicFormModels():
    return {
        'modules':'UserServices.Modules',
    }


def checkIsFileField(field):
    return field in ['image', 'file', 'path',  'video', 'audio']


def getExcludeFields():
    return['id',  'created_at', 'updated_at', 'domain_user_id', 'added_by_user_id', 'created_by_user_id', 'updated_by_user_id']


def getDynamicFormFields(model_instance, domain_user_id):
    fields = {'text' : [], 'select' : [], 'checkbox' : [], 'radio' : [], 'textarea' : [], 'json' : [], 'file' : []}

    for field in model_instance._meta.fields:
        
        if field.name in getExcludeFields():
            continue

        label = field.name.replace('_', ' ').title()
        
        field_data = {
            'name' : field.name,
            'label' : label,
            'placeholder' : 'Enter' + label,
            'default' : model_instance.__dict__[field.name] if field.name in model_instance.__dict__ else '',
            'required' : not field.null
        }

        if checkIsFileField(field.name):
            field_data['type'] = 'file'
        elif field.get_internal_type() == 'TextField':
            field_data['type'] = 'textarea'
        elif field.get_internal_type() == 'JSONField':
            field_data['type'] = 'json'
        elif field.get_internal_type() == 'CharField' and field.choices:
            field_data['type'] = 'select'
            field_data['options'] = [{'id' : choice[0], 'value' : choice[1]} for choice in field.choices]
        elif field.get_internal_type() == 'CharField' or field.get_internal_type() == 'IntegerField' or field.get_internal_type() == 'DecimalField':
            field_data['type'] = 'text'
        elif field.get_internal_type() == 'BooleanField':
            field_data['type'] = 'checkbox'
        else:
            field_data['type'] = 'text'

            if isinstance(field, ForeignKey):
                related_model = field.related_model
                related_key = field.name
                related_key_name = ''

                if hasattr(related_model, 'defaultkey'):

                    related_key_name = related_model.defaultkey()
                    options = related_model.objects.filter(domain_user_id = domain_user_id).values_list('id', related_key_name, related_model.defaultkey())
                else:
                    related_key_name = related_model._meta.pk.name
                    options = related_model.objects.filter(domain_user_id = domain_user_id).values_list('id', related_key_name, 'name')

                field_data['options'] = [{'id' : option[0], 'value' : option[1]} for option in options]
                field_data['type'] = 'select'
            
        fields[field_data['type']].append(field_data)
    return fields
        

def renderResponse(data, message, status=200):
    if status >= 200 and status < 300:
        return Response({'data': dictToList(data), 'message': message}, status = status)
    else:
        if isinstance(data, dict):
            return Response({'errors': data, 'message':message}, status = status)
        elif isinstance(data, list):
            return Response({'errors': data, 'message':message}, status = status)
        else:
            return Response({'errors':[data], 'message':message}, status = status)
        
def dictToList(data):
    values = []
    for key, value in data.items():
        values.extend(value)
    return values

def custom_exception_handler(exc, context):
    response=exception_handler(exc,context)

    if isinstance(exc,AuthenticationFailed):
        response_data={
            'message':exc.detail,
            'errors':exc.detail.get('messages',[])
        }
        return renderResponse(data=response_data['errors'],message=response_data['message']['detail'],status=exc.status_code)
    elif isinstance(exc,NotAuthenticated):
        return renderResponse(data='User Not Authenticated',message='User Not Authenticated',status=exc.status_code)
    elif isinstance(exc,PermissionDenied):
        return renderResponse(data="You Don't Have Permission to Access this page",message='Permission Denied',status=exc.status_code)
    return response