import React, { useEffect, useState } from 'react'
import { Container, Box, Card, CardContent, Tabs, Tab, Typography, TextField, Button, LinearProgress } from '@mui/material'

import useAPI from '../hooks/API_Handler'
import { toast } from 'react-toastify';
import { useNavigate } from 'react-router-dom';


function AuthScreen() 
{
    const navigate = useNavigate();
    const [tabValue, setTabValue] = useState(0);

    const handleTabChange =  (event, newValue) => 
    {
        setTabValue(newValue);
    };

    useEffect(() => 
    {
        if (localStorage.getItem("token)"))
        {
            navigate("/home");
        }
    }, [])

    return (
        <Container  maxWidth="sm" sx={{height:'100vh', display:'flex', alignItems:'center', justifyContent:'center'}}>
            <Card sx={{width:'100%'}}>
                <CardContent>
                    <Tabs value={tabValue} onChange={handleTabChange} centered>
                        <Tab label="Login" />
                        <Tab label="Sign Up" />
                    </Tabs>
                    {tabValue === 0 && <LoginForm />}
                    {tabValue === 1 && <SignUpForm />}
                </CardContent>
            </Card>
        </Container>
    );
};

function LoginForm()
{

    const navigate = useNavigate();
    const {callAPI, error, loading} = useAPI();

    const doLogin = async(e) =>
    {
        e.preventDefault();
        let response = await callAPI({url:"http://localhost:8000/api/auth/login/", method:"POST", body:{username:e.target.username.value, password:e.target.password.value}});
       
        if (response?.data?.access)
            {
                localStorage.setItem("token", response.data.access);
                toast.success("Login Successful!")
                navigate("/home");
            }
            else
            {
                toast.error("Login Failed!");
    
            }
        
        console.log(response);
    }

    return (
        <Box sx={{mt : 3}}>
            <form onSubmit={doLogin}>
                <Typography variant="h5" component="div" gutterBottom>
                    Login
                </Typography>

                <TextField
                fullWidth
                label='Username'
                name = "username"
                margin='normal'
                variant='outlined'
                />

                <TextField
                fullWidth
                label='Password'
                type='password'
                name='password'
                margin='normal'
                variant='outlined'
                />

                {loading ? <LinearProgress style={{width:"100%"}} /> : 
                    <Button variant="contained" type='submit' color="primary" fullWidth sx={{mt : 2}}>
                        Login
                    </Button>
                }
            </form>
        </Box>
    );
}


function SignUpForm()
{

    const navigate = useNavigate();
    const {callAPI, error, loading} = useAPI();

    const doSignUp = async(e) =>
    {
        e.preventDefault();
        let response = await callAPI({url:"http://127.0.0.1:8000/api/auth/signup/", method:"POST", body:{username:e.target.username.value, password:e.target.password.value, email:e.target.email.value, profile_pic:"W"}});
        
        if (response?.data?.access)
        {
            localStorage.setItem("token", response.data.access);
            toast.success("Sign Up Successful!")
            navigate("/home");
        }
        else
        {
            toast.error("Sign Up Failed!");

        }

        console.log(response);
    }

    return (
        <Box sx={{mt : 3}}>
            <form onSubmit={doSignUp}>
                <Typography variant="h5" component="div" gutterBottom>
                    Sign Up
                </Typography>

                <TextField
                fullWidth
                label='Username'
                name='username'
                margin='normal'
                variant='outlined'
                />

                <TextField
                fullWidth
                label="Email"
                type='email'
                name='email'
                margin='normal'
                variant='outlined'
                />

                <TextField
                fullWidth
                label='Password'
                type='password'
                name='password'
                margin='normal'
                variant='outlined'
                />

                {loading ? <LinearProgress style={{width:"100%"}} /> : 
                    <Button variant="contained" type='submit' color="primary" fullWidth sx={{mt : 2}}>
                        Sign Up
                    </Button>
                }
            </form>
        </Box>
    );
}

export default AuthScreen;