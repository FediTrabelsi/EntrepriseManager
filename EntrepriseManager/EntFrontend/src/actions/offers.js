import axios from "axios";

import { GET_OFFERS, DELETE_OFFER, ADD_OFFER } from "./types";

// GET OFFERS
export const getOffers = () => (dispatch, getState) => {
  axios
    .get("/api/offers/")
    .then(res => {
      dispatch({
        type: GET_OFFERS,
        payload: res.data
      });
    })
    .catch(err =>
      console.log(err)
    );
};

export const deleteOffer = id => (dispatch, getState) => {
    axios
      .delete(`/api/offers/${id}/`)
      .then(res => {
        
        dispatch({
          type: DELETE_OFFER,
          payload: id
        });
      })
      .catch(err => console.log(err));
  };

  export const addOffer = offer=> (dispatch, getState) => {
    axios
      .post("/api/offers/", offer)
      .then(res => {
        dispatch({
          type: ADD_OFFER,
          payload: res.data
        });
      })
      .catch(err =>
          console.log(err)
      );
  };
