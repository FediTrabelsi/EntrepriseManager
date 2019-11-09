import { ENTREPRISE_LOADED,ENTREPRISE_LOADING,REGISTER_SUCCESS,REGISTER_FAIL, AUTH_ERROR,LOGIN_SUCCESS,LOGIN_FAIL } from '../actions/types'


const initialState = {
    user : null,
    isAuthenticated : null,
    msg:null

}

export default function(state = initialState, action){
    switch(action.type){
        case ENTREPRISE_LOADED:
            return {
                ...state,
                isAuthenticated:false,
                
            }
        case LOGIN_SUCCESS :
            return{
                isAuthenticated:true,
                user: action.entreprise
            }
        case AUTH_ERROR :
        case LOGIN_FAIL :
            return {
                ...state,
                user: null,
                isAuthenticated: false
            }
        case REGISTER_SUCCESS:
            return{
                isAuthenticated: true,
                user: action.entreprise
            }
        case REGISTER_FAIL:
            return{
                ...state,
                user:null,
                isAuthenticated:false,
                msg:action.payload
            }
        default :
            return state ;
    }
}