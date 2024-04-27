import axios from "axios"
import base_url from "./base_url"

export async function createUser({username, email, password}){
    try{
        console.log(username,email,password);
        const response = await axios.post(`${base_url}/users/`, 
        {
         username : username,
         email : email,
         password   
        });
        
        return response;
        
    }catch(error) {
        console.log(error);
        throw error;
    }

}

export async function login({username, password}) {
    try{
        const response = await axios.post(`${base_url}/token/login/`,{
            username : username,
            password : password
        });
        return response;
    }catch(error) {
        console.log(error);
        throw error;
    }
}