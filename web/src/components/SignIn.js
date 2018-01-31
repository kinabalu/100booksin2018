import React, { Component } from 'react';
import ListView from './ListView';
import styles from './SignIn.css'

class SignIn extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 'Name here',
            error: null,
            isLoaded: false,
            isLoggedIn: false,
            submitted: false,
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(event) {
        this.setState({value: event.target.value});
    }
    handleSubmit(event){
        // Validate input
        //window.alert("http://192.168.99.100:8080/login?grid="+this.state.value);
        this.setState({
            submitted: true
        });
        fetch("http://192.168.99.100:8080/login?grid="+this.state.value)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        result: result.result
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: false,
                        error: true
                    });
                }
            );

        event.preventDefault();
    }
    render(){
        var { error, isLoaded, result, submitted } = this.state

        if(!submitted){
            return(
                <section className={styles.SignIn}>
                    <form onSubmit={this.handleSubmit}>
                        <input value={this.state.value} onChange={this.handleChange} />
                        <input type='submit' />
                    </form>
                </section>
            );
        } else {
            if(error){
                console.log("Error doing stuff");
                return <div class='error'>Error in fetch</div>
            } else if(!isLoaded){
                return <div class='waiting'>Loading...</div>
            } else {
                console.log(result);
                return (
                    <ListView />
                )
            }
        }
    }
}

export default SignIn;