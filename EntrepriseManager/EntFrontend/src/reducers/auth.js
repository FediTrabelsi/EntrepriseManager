import { ENTREPRISE_LOADED,ENTREPRISE_LOADING,AUTH_ERROR,LOGIN_SUCCESS,LOGIN_FAIL } from '../actions/types'


const initialState = {
    user : null,
    isAuthentificated : null
}

export default function(state = initialState, action){
    switch(action.type){
        case ENTREPRISE_LOADED:
            return {
                ...state,
                isAuthentificated:true,
                entreprise: action.payload
            }
        case LOGIN_SUCCESS :
            return{
                ...state,
                ...action.payload,
                isAuthentificated:true
            }
        case AUTH_ERROR :
        case LOGIN_FAIL :
            return {
                ...state,
                user: null,
                isAuthentificated: false
            }
        default :
            return state ;
    }
}