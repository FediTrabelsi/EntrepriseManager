import React, { Component, Fragment } from 'react'
import Form from './Form';
import Offers from './Offers'
import Login from '../accounts/Loign'
export class Dashboard extends Component {
    render() {
        return (
           <Fragment>
               <Form/>
               <Offers/>
           </Fragment>
           
        )
    }
}

export default Dashboard
