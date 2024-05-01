import axios from "axios";
import base_url from "./base_url";
import store from "@/store";

export async function createConsommation({ type, reason, date, quantity }) {
  try {
    console.log("Here");
    const token = store.getters.auth_token;
    console.log(token);
    const response = await axios.post(
      `${base_url}/consommations/`,
      {
        date_consommation: date,
        nom_produit: reason,
        quantite_co2: quantity,
        type_consommation: type,
      },
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function fetchConsommations() {
  try {
    const token = store.getters.auth_token;
    const response = await axios.get(`${base_url}/consommations/consult/me/`, {
      headers: {
        Authorization: `Token ${token}`,
      },
    });
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function fetchConsommation(consommationId) {
  try {
    const token = store.getters.auth_token;
    const response = await axios.get(
      `${base_url}/consommations/${consommationId}/`,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function editConsommation(consommationId, newData) {
  try {
    const token = store.getters.auth_token;
    const response = await axios.patch(
      `${base_url}/consommations/${consommationId}/`,
      newData,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function deleteConsommation(consommationId) {
  try {
    const token = store.getters.auth_token;
    const response = await axios.delete(
      `${base_url}/consommations/delete/me/${consommationId}/`,
      {
        headers: {
          Authorization: `Token ${token}`,
        },
      }
    );
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function calculateTripConsommation({ type, quantity }) {
  try {
    const token = store.getters.auth_token;
    const response = await axios.get(
      `${base_url}/consommations/calculate/transport/${type}/${quantity}/`,
      {
        headers: { Authorization: `Token ${token}` },
      }
    );
    return response;
  } catch (error) {
    console.log(error);
    throw error;
  }
}
