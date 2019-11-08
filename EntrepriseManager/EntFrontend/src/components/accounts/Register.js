import React, { Component } from 'react'
import { Link } from 'react-router-dom'
export class Register extends Component {
    state = {
        name : '',
        password : '',
        password_conf : ''
    };

    onSubmit = e=>{
        e.preventDefault();
        console.log("submit")
    };

    onChange= e =>this.setState({ [e.target.name]: e.target.value})
    render() {
        const { name , password , password_conf} = this.state;
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
                value={password_conf}
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

export default Register
