import axios from "axios";
import { createMessage, returnErrors} from './messages';
import { GET_OFFERS, DELETE_OFFER, ADD_OFFER, GET_ERRORS } from "./types";

// GET OFFERS
export const getOffers = (id) => (dispatch, getState) => {
  const config = {
    headers:{
        'Content-Type': 'application/json'
    }
}

const body = JSON.stringify({ id})
  axios
    .post("/offers/getByEntId/",body,config)
    .then(res => {
      if(res.data.success){
        dispatch({
          type: GET_OFFERS,
          payload: res.data
        });
      }
      else{
        dispatch({
            type:GET_ERRORS,
            payload: res.data.message
            
        })
    }
      
    })
      
};

export const deleteOffer = id => (dispatch, getState) => {
  const config = {
    headers:{
        'Content-Type': 'application/json'
    }
}

const body = JSON.stringify({ id})
    axios
      .post(`/offers/deleteOffer/`,body,config)
      .then(res => {
        dispatch(createMessage({ deleteOffer : "this offer was deleted"}))
        dispatch({
          type: DELETE_OFFER,
          payload: id
        });
      })
      .catch(err => console.log(err.response.data));
  };

export const addOffer = offer=> (dispatch, getState) => {
    const config = {
      headers:{
          'Content-Type': 'application/json'
      }
  }
  var newOffer={};
  Object.keys(offer).forEach(function (key) {
    if(offer[key]!=""){
   newOffer[key]=offer[key];
  }
  });
  
    axios
      .post("/offers/createOffer/", newOffer,config)
      .then(res => {
        console.log(res)
        if(res.data.success){
          console.log(res.data)

          dispatch(createMessage({ addOffer : "New offer was added"}))
        dispatch({
          type: ADD_OFFER,
          payload: res.data
        });
        }
        else{
          
          dispatch({
              type:GET_ERRORS,
              payload: res.data
              
          })
      }
        
      })
     
  };
