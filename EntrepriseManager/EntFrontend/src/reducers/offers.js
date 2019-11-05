import {GET_OFFERS ,DELETE_OFFER, ADD_OFFER, CLEAR_OFFERS} from '../actions/types.js';

const initialState = {
    offers: []
  };

  export default function (state = initialState, action) {
    switch (action.type) {
      case GET_OFFERS:
        return {
          ...state,
          offers: action.payload
        };
      case DELETE_OFFER:
        return {
          ...state,
          offers: state.offers.filter(offer => offer.id !== action.payload)
        };
      case ADD_OFFER:
        return {
          ...state,
          offers: [...state.offers, action.payload]
        };
      case CLEAR_OFFERS:
        return {
          ...state,
          offers: []
        };
      default:
        return state;
    }
  }
  