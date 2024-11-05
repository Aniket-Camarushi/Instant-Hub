import './App.css';
//import AuthScreen from './pages/AuthScreen';
import Home from './pages/Home';
import Layout from './layout/layout';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import 'react-toastify/ReactToastify.css'
import ProtectedRoute from './utils/ProtectedRoute';
import { ToastContainer } from 'react-toastify';
import Auth from './pages/Auth';
import store from './redux/store/store';
import { useDispatch } from 'react-redux';
import { Provider } from 'react-redux';
import { fetchSidebar } from './redux/reducer/sidebardata';
import { useEffect,useState } from 'react';


function App() {

  const {status,error,items}=useSelector(state=>state.sidebardata);
  const dispatch=useDispatch();

  // const sidebarItems=[
  //   {name:"Home", link:"/home", icon:"home"}, 
  //   {name:"Products", link:"/products", icon:"products"}, 
  //   {name:"Categories", icon:"categories", children:[{name: "All Categories", link: "/categories"}, {name: "Add Category", link: '/categories/add'}]}, 
  //   {name:"Orders", link:"/orders", icon:"orders"}, 
  //   {name:"Users", link:"/users", icon:"users"}, 
  //   {name:"Settings", link:"/settings", icon:"settings"}, 
  
  // ]

  useEffect(()=>{
    if(status=='idle'){
      dispatch(fetchSidebar());
    }
  },[status,dispatch])

  const router = createBrowserRouter(
    [
      {path : "/auth", element : <Auth />}, 
      {
        path : "/", 
        element : <Layout sidebarList={items}/>,
        children : [
          {path : "home", element:<ProtectedRoute element={<Home/>}/>}
        ]},
    ]
  )

  return (
    <>
      <RouterProvider router={router}/>
      <ToastContainer position = "bottom-right" autoclose={3000} hideProgressBar={false} style={{marginBottom : '30px'}} />
    
    
    </>
  );
}

export default App;
