import { useState } from "react";
import axios from "axios";


function useAPI()
{
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);
    const callAPI = async ({url, method="GET", body={}, header={}}) =>
    {
        setLoading(true);

        let response = null;
        
        try 
        {
            response = await axios.request({url:url, method:method, data:body, headers:header});
        }
        catch (err)
        {
            setError(err)
        }
        
        setLoading(false);

        return response;
    }

    return {callAPI, error, loading};
}

export default useAPI;