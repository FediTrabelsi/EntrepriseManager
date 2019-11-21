import React, { Component, Fragment  } from "react";
import {connect } from 'react-redux';
import PropTypes from 'prop-types';
import {getSkills, deleteSkill, addSkill} from '../../actions/skills';


export class Skills extends Component {
    static propTypes = {
        skills: PropTypes.array.isRequired,
        getSkills:PropTypes.func.isRequired,
        deleteSkill:PropTypes.func.isRequired

      };
      componentDidMount() {
        this.props.getSkills();
      }
    render() {
        return (
            <Fragment>
            <h2>Skills List</h2>
            <table className="table table-striped">
              <thead>
                <tr> 
                  <th>ID</th>
                  <th>Name</th>
                  <th>Description</th>
                  <th />
                </tr>
              </thead>
              <tbody>
                {this.props.skills.map(skill => (
                  <tr key={skill.id}>
                    <td>{skill.id}</td>
                    <td>{skill.name}</td>
                    <td>{skill.description}</td>
                    <td>
                    <button onClick={this.props.deleteSkill.bind(this,skill.id)} className="btn btn-danger btn-sm"
>

                        {" "}
                        Delete
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </Fragment>
   
        )
    }
}
const mapStateToProps = state => ({
    skills: state.skills.skills,
  });
export default connect(mapStateToProps, {getSkills, deleteSkill})(Skills)