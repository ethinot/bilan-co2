import axios from "axios";
import base_url from "./base_url";
import store from "@/store";
export async function fetchUserInfo() {
  try {
    const token = store.getters.auth_token;
    const response = await axios.get(`${base_url}/user_data/me/`, {
      headers: {
        Authorization: token,
      },
    });
    if (response.status === 200) {
      return response;
    } else throw Error("Something went wrong when fetching user info");
  } catch (error) {
    console.log(error);
    throw error;
  }
}

export async function editUserInfo({ age, localisation, profession }) {
  try {
    const token = store.getters.auth_token;
    const response = await axios.patch(`${base_url}/user_data/update/me/`, {
      headers: {
        Authorization: token,
      },
    });
    if (response.status === 200) {
      return response;
    } else if (response.status === 304) {
      throw Error("Content already up to date !");
    } else throw Error("Something went wrong when updating user info");
  } catch (error) {
    console.log(error);
    throw error;
  }
}
