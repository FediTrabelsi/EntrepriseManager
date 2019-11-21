import React, { Component, Fragment } from 'react'
import Skills from './Skills'
import SkillsForm from './SkillsForm'
export class skillsF extends Component {
    render() {
        return (
           <Fragment>
               <SkillsForm/>
               <Skills/>
               
           </Fragment>
        )
    }
}

export default skillsF
