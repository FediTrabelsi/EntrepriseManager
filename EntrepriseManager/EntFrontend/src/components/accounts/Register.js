import React, { Component } from 'react'
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import { connect } from 'react-redux';
import {register} from '../../actions/auth';
import { useAlert } from 'react-alert';
import {Route , Redirect } from 'react-router-dom'



const  mapStateToProps = state =>({
  isAuthenticated: state.auth.isAuthenticated,
  
  });
  const mapDispatchToProps = { register };

  export default connect(
    mapStateToProps,mapDispatchToProps
  )(Registerr);


function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const useStyles = makeStyles(theme => ({
  root: {
    height: '100vh',
  },
  image: {
    backgroundImage: 'url(../../../static/frontend/careers.jpg)',
    backgroundRepeat: 'no-repeat',
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main,
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1),
  },
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
}));

const initialState = {
  name : '',
  password :'',
  password2 :''
  
};
export  function   Registerr({isAuthenticated, register}) {
  const alert = useAlert()

  Registerr.state = {
              name : '',
              password :'',
              password2:''
          
          }
         

            const classes = useStyles();
            if(isAuthenticated){
              return <Redirect to="/" />
            }
        return (
         
        <Grid container component="main" className={classes.root}>
        <CssBaseline />
        <Grid item xs={false} sm={4} md={7} className={classes.image} />
        <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <div className={classes.paper}>
          <Avatar className={classes.avatar}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign up
          </Typography>
          <form className={classes.form} noValidate>
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              id="name"
              label="Entreprise Name"
              name="name"
              autoComplete="name"
              autoFocus
              inputRef={el => initialState.name= el} 
                          />
            
            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
              inputRef={el => initialState.password= el} 
            />

            <TextField
              variant="outlined"
              margin="normal"
              required
              fullWidth
              name="password2"
              label="Password confirmation"
              type="password"
              id="password2"
              autoComplete="current-password"
              inputRef={el => initialState.password2= el} 
            />

            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick={e => {e.preventDefault();
                register(initialState.name.value, initialState.password.value,initialState.password2.value);
              }
            }

            >
              Sign Up
            </Button>
            <Grid container>
              <Grid item xs>
                <Link href="#/login" variant="body2">
                  Already have an account? Sign in
                </Link>
              </Grid>
              
            </Grid>
            <Box mt={5}>
              <Copyright />
            </Box>
          </form>
        </div>
      </Grid>
      </Grid>

        );
    
}



