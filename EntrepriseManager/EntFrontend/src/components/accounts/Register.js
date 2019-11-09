import React, { Component } from 'react'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import {register} from '../../actions/auth';
import {Route , Redirect } from 'react-router-dom'

export class Register extends Component {
    state = {
        name : '',
        password : '',
        password2 : ''
    };

    static propTypes = {
      register: PropTypes.func.isRequired,
      isAuthenticated: PropTypes.bool
    }
    onSubmit = e => {
        e.preventDefault();
        console.log(this.state.name, this.state.password, this.state.password2)
        this.props.register(this.state.name, this.state.password, this.state.password2);
        
    };
    
    onChange = e => this.setState({ [e.target.name]: e.target.value });
    render() {
      if(this.props.isAuthenticated){
        return <Redirect to="/" />
      }
        const { name , password , password2} = this.state;
        return (
            <div className="col-md-6 m-auto">
        <div className="card card-body mt-5">
          <h2 className="text-center">Register</h2>
          <form onSubmit={this.onSubmit}>
            <div className="form-group">
              <label>Username</label>
              <input
                type="text"
                className="form-control"
                name="name"
                onChange={this.onChange}
                value={name}
              />
            </div>
            <div className="form-group">
              <label>Password</label>
              <input
                type="password"
                className="form-control"
                name="password"
                onChange={this.onChange}
                value={password}
              />
            </div>
            <div className="form-group">
              <label>Confirm Password</label>
              <input
                type="password"
                className="form-control"
                name="password2"
                onChange={this.onChange}
                value={password2}
              />
            </div>
            <div className="form-group">
              <button type="submit" className="btn btn-primary">
                Register
              </button>
            </div>
            <p>
              Already have an account? <Link to="/login">Login</Link>
            </p>
          </form>
        </div>
      </div>
        )
    }
}


const  mapSatateToProps = state =>({
  isAuthenticated: state.auth.isAuthenticated
});


export default connect(mapSatateToProps, {register } )(Register)
