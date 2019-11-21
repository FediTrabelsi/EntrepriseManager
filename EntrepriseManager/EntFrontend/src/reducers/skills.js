import {GET_SKILLS ,DELETE_SKILL, ADD_SKILL, GET_ERRORS} from '../actions/types.js';

const initialState = {
    skills: [], 
    msg : null,
  };

  export default function (state = initialState, action) {
    switch (action.type) {
      case GET_SKILLS:
        return {
          ...state,
          skills: action.payload.skills,
          msg: action.payload.message
        };
      case DELETE_SKILL:
        return {
          ...state,
          skills: state.skills.filter(skill => skill.id !== action.payload)
        };
      case ADD_SKILL:
        return {
          ...state,
          skills: [...state.skills, action.payload.data.skill],
          msg:action.payload.message

        };
      default:
        return state;
    }
  }