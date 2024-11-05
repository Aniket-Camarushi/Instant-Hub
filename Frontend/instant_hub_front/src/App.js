import './App.css';
import AuthScreen from './pages/AuthScreen';
import Home from './pages/Home';
import Layout from './utils/Layout';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import 'react-toastify/ReactToastify.css'
import ProtectedRoute from './utils/ProtectedRoute';

const router = createBrowserRouter(
  [
    {path : "/", element : <AuthScreen />}, 
    {path : "/home", element : <ProtectedRoute element={<Home />} />},
  ]
)

function App() {
  return (
    <Layout>
      <RouterProvider router={router}/>
    </Layout>
  );
}

export default App;
