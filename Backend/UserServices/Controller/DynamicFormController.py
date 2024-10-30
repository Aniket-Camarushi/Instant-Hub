from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.apps import apps
from django.core.serializers import serialize
import json

from InstantHub.Helper import getDynamicFormModels, getDynamicFormFields, getExcludeFields
from UserServices.models import Users

class DynamicFormController(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, modelName):

        # Checking if the model exists in our Dynamic Form Models (Database).
        if modelName not in getDynamicFormModels():
            return Response("Model does not exist", status=404)

        # Get the model (The place where the model can be found. Ex: ProductServices.Categories) 
        # from the dictionary of dynamic form models.
        model = getDynamicFormModels()[modelName]
        
        # Getting the "class" or the ACTUAL categories model from the "model" variable.
        model_class = apps.get_model(model)

        # Checking if model class exists
        if model_class is None:
            return Response("Model not found", status=404)
        
        # Get the meta data (data from the models) and the fields from the model.
        # Ex: Name, ID,  etc.
        fields_info = model_class._meta.fields

        # Getting the keys/variables (Ex:  name, id, etc.) from the fields info.
        model_fields = {field.name for field in fields_info}
        exclude_fields = getExcludeFields()

        # Filtering fields that are required by "request.data" and are not null.
        required_fields = [field.name for field in fields_info if not field.null and field.default is not None and field.name not in exclude_fields]

        # Filtering data that user has not passed which are important/required.
        missing_fields = [field for field in required_fields if field not in request.data]

        if missing_fields:
            return Response({f"The following field is required: {field}" for field in missing_fields}, status=400)
        
        # Creating copy of passed-in data (hereby refd as "request.data") 
        # for manipulation (of printing/giving data to client/user side).
        fields = request.data.copy()

        # Manipulating by adding below keys for further information that may be displayed/used.
        fields['domain_user_id'] = request.user.domain_user_id
        fields['added_by_user_id'] = Users.objects.get(id = request.user.id)

        # Filtering data that user has passed which are not required or variables not in the database.
        # Check Postman "Dynamic Form API POST" > Body > raw > JSON > "abc" : 1
        # "abc" is not a variable like "description", which means it will be filter OUT.
        fields_data = {key:value for key, value in fields.items() if key in model_fields}

        # All the Model Fields Data
        ### print(model_fields)
        
        # All the Post Fields Data (Data that was passed in by the user).
        ### print(fields.items())

        # Sanitizing/Keeping the Post Fields Data by only keeping the fields that are in the Model Fields Data.
        ### print(fields_data.items())
        
        # Assigning Foreign Key instance for ForeignKey fields in request.data
        # by getting the instance of the related model by the ID.
        # This works with "parent_id" since it is a ForeignKey with "self" meaning it is related to itself. 
        for field in fields_info:
            if field.is_relation and field.name in fields_data and isinstance(fields_data[field.name], int):
                related_model = field.related_model

                try:
                    fields_data[field.name] = related_model.objects.get(id = fields_data[field.name])
                except:
                    return Response({'error':f'{field.name} Relation Not Exist'}, status=404)



        # If the **kwargs is replaced with "fields", then the extra (non-variable) data passed in by user
        # will throw an Error. So only use only the data needed for **kwargs.
        # This saves the data in the database.
        model_instance = model_class.objects.create(**fields_data)

        # Serializing the Data
        serialzed_data = serialize('json', [model_instance])
        
        # Converting the serialized data into JSON format
        model_json = json.loads(serialzed_data)

        # Getting and manipulating the first object of JSON which are the fields/variables in a database.
        response_json = model_json[0]['fields']
        response_json['id'] = model_json[0]['pk']
        return Response({"Data": response_json, "Message":"Data saved successfully!"})


    def get(self, request, modelName):
        
        if  modelName not in getDynamicFormModels():
            return Response({'error' : 'Model not  found'}, status=404)
        
        model = getDynamicFormModels()[modelName]
        model_class = apps.get_model(model)

        if model_class is None:
            return Response({'error' : 'Model not found'}, status=404)
        
        model_instance = model_class()
        fields = getDynamicFormFields(model_instance, request.user.domain_user_id)
        return Response({'data' :  fields, 'message' : 'Form fields fetched sucessfully'})


