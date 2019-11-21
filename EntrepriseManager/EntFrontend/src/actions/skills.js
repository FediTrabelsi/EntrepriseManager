import axios from "axios";
import { createMessage, returnErrors} from './messages';
import { GET_SKILLS, DELETE_SKILL, ADD_SKILL, GET_ERRORS} from "./types";



// GET SKILLS
export const getSkills = () => dispatch => {
  const config = {
    headers:{
        'Content-Type': 'application/json'
    }
}
  axios
  .get("/skills/SkillsList",config)
  .then(res => {
    if(res.data.success){
      console.log(res.data.skills)
      dispatch({
        type: GET_SKILLS,
        payload: res.data
      });
      dispatch(createMessage({ skillsList : "skills List"}))
    }
    
    
    
  })
  ;
};
// DELETE SKILL

export const deleteSkill = id => (dispatch, getState) => {
    const config = {
      headers:{
          'Content-Type': 'application/json'
      }
  }

  const body = JSON.stringify({ id})
    axios
      .post("/skills/deleteSkill/",body,config)
      .then(res => {
        dispatch(createMessage({ deleteSkill : "this skill was deleted"}))
        dispatch({
          type: DELETE_SKILL,
          payload: id
        });
      })
      .catch(err => console.log(err.response.data));
  };


  //ADD SKILL 

  export const addSkill = skill=> (dispatch, getState) => {
    const config = {
      headers:{
          'Content-Type': 'application/json'
      }
  }
  console.log(skill)
  
    axios
      .post("/skills/createSkill/", skill,config)   
      .then(res => {
        console.log(res)
        if(res.data.success){
          console.log(res.data)

          dispatch(createMessage({ addSkill : "New skill was added"}))
        dispatch({
          type: ADD_SKILL,
          payload: res.data
        });
        }
        else{
          dispatch({
              type:GET_ERRORS,
              payload: res.data.message
              
          })
      }
        
      })
     
  };
