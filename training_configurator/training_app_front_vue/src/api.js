const  eventUrl= '/api/event/'
const  authorUrl= '/api/author/'
const  taskUrl= '/api/task/'
import axios from "axios"


export function toURLParams(filters){
    let params = new URLSearchParams();
    for (let f in filters){
        if (Array.isArray(filters[f])){
            for (let p of filters[f]){
                if (p){
                    params.append(f,p);
                }
            }
        }else if (filters[f] && filters[f].id){
            params.append(f,filters[f]['id'])

        }else{
                if (filters[f] !=undefined){
            params.append(f,filters[f]);
                }

        }
    }
    return params
}

async function _save(url,obj){
    let response 
    if (obj.id){
         response = await axios.patch(url+obj.id+'/',obj)
    }else{
         response = await axios.post(url,obj)
    }
    return response.data
}
  
async function _delete(url,obj){
    let response 
    if (obj.id){
         response = await axios.delete(url+obj.id+'/',obj)
    }


    return response
}
    
async function _filter(url,filter){
    const response = await axios.get(url+'?'+toURLParams(filter))
    return response.data
}

async function _getById(url,id){
    const response = await axios.get(url+id+'/')
    return response.data
}
                      


function apiConstructor(apiUrl){

    let objects= {
        async save(obj){
            return _save(apiUrl,obj)
        },
        async get(obj){
            return _getById(apiUrl,obj)
        },
        async filter(filter){
            return _filter(apiUrl,filter)
        },
        async delete(obj){
            return _delete(apiUrl,obj)
        },
    }
    return {
        url:apiUrl,
        objects,
    }
}           

export let Event = apiConstructor(eventUrl)
export let Task = apiConstructor(taskUrl)

export let Author = {
    url:authorUrl,
    objects:{

        async who_iam(){
            return (await axios.get('/api/author/who_iam/')).data

        },
        async filter(params){
            return (await axios.get(authorUrl,{params})).data

        }
    }

}

import CSRF_TOKEN from "./csrf_token.js";

async function getJSON(response) {
  if (response.status === 204) return "";
  return response.json();
}

function apiService(endpoint, method, data) {
  const config = {
    credentials: "same-origin",
    method: method || "GET",
    body: data !== undefined ? JSON.stringify(data) : null,
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": CSRF_TOKEN
    }
  };
  return fetch(endpoint, config)
    .then(getJSON)
    .catch(error => console.log(error));
}

export { apiService };