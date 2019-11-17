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
                    
                    alert.error(error.msg.message)
                
            
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
