import React, { Component } from 'react';
import SignIn from './components/SignIn';
import ListView from './components/ListView';

class Home extends Component {
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            isLoggedIn: false
        }
    }
    componentDidMount(){
        fetch("http://192.168.99.100:8080/isloggedin")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        isLoggedIn: result.result
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: false,
                        error: true
                    });
                }
            );
    }
    render() {
        var { error, isLoaded, isLoggedIn } = this.state

        if(false){
            isLoaded = true;
            isLoggedIn = true;
        }

        if(error){
            console.log(isLoggedIn);
            return <div class='error'>Error in fetch</div>
        } else if(!isLoaded){
            return <div class='waiting'>Loading...</div>
        } else {
            if(isLoggedIn){
                console.log("Logged in");
                return (
                    <ListView />
                );
            } else {
                console.log("Not logged in");
                return(
                    <SignIn isLoggedIn={isLoggedIn} />
                );
            }
        }
    }
}

export default Home;
