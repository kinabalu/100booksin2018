import React, { Component } from 'react';
//import cookie from "react-cookie";
import SignIn from './components/SignIn';
import ListView from './components/ListView';
import Cookies from 'universal-cookie';

class Home extends Component {
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            isLoggedIn: false,
            cookies: new Cookies()
        }
    }
    componentDidMount(){
        if(typeof this.state.cookies.get("GRUserToken") !== 'undefined'){ // Cookie exists, check it's validity
            var url = "http://192.168.99.100:8080/token/"+this.state.cookies.get("GRUserToken");
            fetch(url)
                .then(res => res.json())
                .then(
                    (result) => {
                        const re = result.result ? true : false;
                        this.setState({
                            isLoaded: true,
                            isLoggedIn: re,
                            token: this.state.cookies.get("GRUserToken")
                        });
                    },
                    (error) => {
                        this.setState({
                            isLoaded: false,
                            error: true
                        });
                    }
                );
        } else { // Cookie doesn't exist
            this.setState({
                isLoaded: true
            });
        }
    }
    render() {
        var { error, isLoaded, isLoggedIn } = this.state

        if(error){
            return <div className='error'><section>Server request error</section></div>
        } else if(!isLoaded){
            return <div className='waiting'><section>Loading...</section></div>
        } else {
            if(isLoggedIn){
                return (
                  <ListView token={this.state.token} />
                );
            } else {
                return(
                    <SignIn />
                );
            }
        }
    }
}

export default Home;
