import React, { Component, Fragment } from 'react'
import {connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addOffer } from '../../actions/offers'
export class Form extends Component {
    state ={ 
        name:'',
        description:'',
        nb_places:'',
        nb_applicants:'',
        CreationDate:'',
        ExpDate:'',
        Status:''
    }

    static propTypes = {
      Entreprise:PropTypes.number
    };
    onChange = e => this.setState({ [e.target.name]: e.target.value });

onSubmit = e => {
  e.preventDefault();
  const { name, description, nb_places, nb_applicants,CreationDate,ExpDate,Status} = this.state;
  const Entreprise=  this.props.Entreprise;
  const offer = {  name, description, nb_places,ExpDate,Entreprise};
  
  this.props.addOffer(offer);
  this.setState({
        name:"",
        description:"",
        nb_places:"",
        nb_applicants:"",
        CreationDate:"",
        ExpDate:"",
        Status:""
  });
};

    render() {
        const { name, description, nb_places, ExpDate} = this.state;

        return (
            <div className="card card-body mt-2 mb-2">
            <h2>Add Offer</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Offer name</label>
                <input
                  className="form-control"
                  type="text"
                  name="name"
                  onChange={this.onChange}
                  value={name}
                />
              </div>
              <div className="form-group">
                <label>Description</label>
                <input
                  className="form-control"
                  type="description"
                  name="description"
                  onChange={this.onChange}
                  value={description}
                />
              </div>
              <div className="form-group">
                <label>Available positions</label>
                <textarea
                  className="form-control"
                  type="text"
                  name="nb_places"
                  onChange={this.onChange}
                  value={nb_places}
                />
              </div>
          
              <div className="form-group">
                <label>Expiration date</label>
                <textarea
                  className="form-control"
                  type="text"
                  name="ExpDate" 
                  onChange={this.onChange}
                  value={ExpDate}
                />
              </div>
          
             
              <div className="form-group">
                <button type="submit" className="btn btn-primary">
                  Submit
                </button>
              </div>
            </form>
          </div>
        )
    }
}


const mapStateToProps = state => ({
  Entreprise : state.auth.user.id
});

export default connect(
    mapStateToProps,
    { addOffer }
  )(Form);