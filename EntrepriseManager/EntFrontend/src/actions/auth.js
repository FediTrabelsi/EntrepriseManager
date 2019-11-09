import axios from 'axios'
import {returnErrors } from './messages'

import {ENTREPRISE_LOADED,AUTH_ERROR,LOGIN_SUCCESS,LOGIN_FAIL, REGISTER_SUCCESS,REGISTER_FAIL} from './types'

export const loadEntreprise = () =>(dispatch,getState) =>{
    const config = {
        headers:{
            'Content-Type': 'application/json'
        }
    }

    axios.post('/entreprises/login/',config)
    .then(res => {
        console.log(res.data)
        dispatch({
            type:ENTREPRISE_LOADED,
            payload: res.data
        })
        }).catch(err=>{
            console.log(res)
            dispatch(returnErrors(err.response.data,err.response.status))
            dispatch({
                type:AUTH_ERROR
            })
        })
    
    



}

export const login = (name,password) =>(dispatch) =>{
    const config = {
        headers:{
            'Content-Type': 'application/json'
        }
    }

    const body = JSON.stringify({ name, password})

    axios.post('/entreprises/login/',body,config)
    .then(res => {
        if(res.data.success){
        dispatch({
            type:LOGIN_SUCCESS,
            payload: res.data.message,
            entreprise :res.data.data.entreprise
        })}
        else{
            dispatch({
                type:LOGIN_FAIL,
                payload: res.data.message
                
            })
        }
    })



}

export const register = (name,password,password2) =>(dispatch) =>{
    const config = {
        headers:{
            'Content-Type': 'application/json'
        }
    }

    const body = JSON.stringify({ name, password, password2})

    axios.post('/entreprises/register/',body,config)
    .then(res => {
        if(res.data.success){
        dispatch({
            type:REGISTER_SUCCESS,
            payload: res.data.message,
            entreprise :res.data.data.entreprise
        })}
        else{
            dispatch({
                type:REGISTER_FAIL,
                payload: res.data.message
                
            })
        }
    })



}