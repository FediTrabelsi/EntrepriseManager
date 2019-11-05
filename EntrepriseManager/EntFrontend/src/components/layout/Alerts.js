import React, { Component, Fragment } from 'react'
import { withAlert } from 'react-alert';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
export class Alerts extends Component {

    static propTypes={
        error: PropTypes.object.isRequired,
        message: PropTypes.object.isRequired
    }
    componentDidUpdate(prevProps){
        const {error,alert, message  }= this.props;
        if(error !== prevProps.error){
            if(error.msg.name){
                alert.error(`Name: ${error.msg.name.join()}`)
            }else if(error.msg.description){
                    alert.error(`Description : ${error.msg.description.join()}`)
                }else if(error.msg.nb_places){
                    alert.error(`Available positions : ${error.msg.nb_places.join()}`)
                }else if(error.msg.ExpDate){
                    alert.error(`Expiration date : ${error.msg.ExpDate.join()}`)
                }
            
        }

        if(message !== prevProps.message){
            if(message.deleteOffer){
                alert.success(message.deleteOffer)
            }
            if(message.addOffer){
                alert.success(message.addOffer)
            }
        }
    }
    render() {
        return (
            <Fragment/>
        )
    }
}
const mapStateToProps= state =>({
    error: state.errors,
    message: state.messages
})

export default connect(mapStateToProps)(withAlert()(Alerts));
