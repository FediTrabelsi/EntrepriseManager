import {
    combineReducers
} from "redux";
import offers from "./offers";
import messages from './messages';
import errors from './errors';
export default combineReducers({
    offers,errors,messages 
});