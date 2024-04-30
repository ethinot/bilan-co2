import axios from "axios";
import base_url from "./base_url";


export async function fetchTrackersTransport(){
    try{
        const response = await axios.get(`${base_url}/consommations/search/transport`);
        if (response.status === 200) {
            return response;
        }
    }catch(error){
        console.log(error);
    }
}

export async function fetchTrackersEnergie(){
    try{
        const response = await axios.get(`${base_url}/consommations/search/energie`);
        if (response.status === 200) {
            return response;
        }
    }catch(error){
        console.log(error);
    }
}

export async function fetchTrackersAliment(){
    try{
        const response = await axios.get(`${base_url}/consommations/search/aliment`);
        if (response.status === 200) {
            return response;
        }
    }catch(error){
        console.log(error);
    }
}