import axios from "axios";
import { createMessage} from './messages';
import { GET_OFFERS, DELETE_OFFER, ADD_OFFER, GET_ERRORS } from "./types";

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
        dispatch(createMessage({ deleteOffer : "this offer was deleted"}))
        dispatch({
          type: DELETE_OFFER,
          payload: id
        });
      })
      .catch(err => console.log(err.response.data));
  };

  export const addOffer = offer=> (dispatch, getState) => {
    axios
      .post("/api/offers/", offer)
      .then(res => {
        dispatch(createMessage({ addOffer : "New offer was added"}))
        dispatch({
          type: ADD_OFFER,
          payload: res.data
        });
      })
      .catch(err =>{
          const errors = {
              msg: err.response.data,
              status : err.response.status
          }
          dispatch({
            type: GET_ERRORS,
            payload: errors
          });
        });
  };
