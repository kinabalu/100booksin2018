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
        // Check to see if cookie exists for user login
        // Set isLoggedIn to true
        // Set isLoaded to true
        // Set grid to goodreads user id
        this.setState({
            isLoaded: true,
            isLoggedIn: true,
            grid: 76836596
        });
    }
    render() {
        var { error, isLoaded, isLoggedIn } = this.state

        if(error){
            console.log(isLoggedIn);
            return <div className='error'>Error in fetch</div>
        } else if(!isLoaded){
            return <div className='waiting'>Loading...</div>
        } else {
            if(isLoggedIn){
                return (
                    <ListView grid={this.state.grid} />
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
