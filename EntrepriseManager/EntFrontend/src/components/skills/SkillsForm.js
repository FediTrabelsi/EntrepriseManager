import React, { Component, Fragment  } from "react";
import {connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addSkill } from '../../actions/skills'




export class SkillsForm extends Component {
    state ={ 
        name:'',
        description:''
    }
    PropTypes = {
        addSkill:PropTypes.func.isRequired
    }
    onChange = e => this.setState({ [e.target.name]: e.target.value });


onSubmit = e => {
  e.preventDefault();
  const { name, description} = this.state;
  const skill = {  name, description};
  this.props.addSkill(skill);
  this.setState({
        name:"",
        description:""
  });
};
    
    render() {
        const { name, description} = this.state;
        return (
            <div className="card card-body mt-2 mb-2">
            <h2>Add Skill</h2>
            <form onSubmit={this.onSubmit}>
              <div className="form-group">
                <label>Skill name</label>
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
                <button type="submit" className="btn btn-primary">
                  Submit
                </button>
              </div>
            </form>
          </div>
   
   
        )
    }
}

export default connect(null, {addSkill} )(SkillsForm);