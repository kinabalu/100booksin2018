import React, { Component } from 'react';
import ListView from './ListView';
import styles from './css/SignIn.css'
import Cookies from 'universal-cookie';
import { Config } from '../config.js';

// 76836596

class SignIn extends Component {
    constructor(props) {
        super(props);
        this.state = {
            value: '76836596',
            error: null,
            isLoaded: false,
            isLoggedIn: false,
            submitted: false,
            cookies: new Cookies(),
            userError: false,
            userErrorMsg: ""
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(event) {
        if(!isNaN(event.target.value)){
            this.setState({
                value: event.target.value,
                userError: false,
                userErrorMsg: ""
            });
        } else {
            this.setState({
                userError: true,
                userErrorMsg: "GoodReads user ID must be number."
            })
        }
    }
    handleSubmit(event){
        // Validate input
        if(!this.state.userError){
            this.setState({
                submitted: true
            });
        } else {
            return ""
        }

        var url = Config.apiIp+"/user/"+this.state.value

        console.log(url);

        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        token: result.result.token
                    });
                    this.state.cookies.set("GRUserToken", result.result.token, {path: '/'})
                },
                (error) => {
                    this.setState({
                        isLoaded: false,
                        error: true,
                        data: error
                    });
                }
            );

        event.preventDefault();
    }
    render(){
        var { error, isLoaded, submitted, userError, userErrorMsg } = this.state
        var preMsg = ""

        if(userError){
            preMsg = <div className='error'><section>{userErrorMsg}</section></div>
        }

        if(!submitted){
            return (
                <form onSubmit={this.handleSubmit}>
                    {preMsg}
                    <section className={styles.SignIn}>
                        <section className={styles.gridInfo}>
                            GoodReads user ID:
                        </section>
                        <section className={styles.grid}>
                            <input defaultValue={this.state.value} required pattern="[0-9]*" onChange={this.handleChange} />
                        </section>

                        <section className={styles.bookCountInfo}>
                            Book count:
                        </section>
                        <section className={styles.bookCount}>
                            <select>
                                <option value="5">5</option>
                                <option value="10">10</option>
                                <option value="15" selected>15</option>
                                <option value="20">20</option>
                                <option value="25">25</option>
                                <option value="30">30</option>
                            </select>
                        </section>


                        <section className={styles.submit}>
                            <input type='submit' value='Load' />
                        </section>
                    </section>
                </form>
            );
        } else {
            if(error){
                console.log(this.state.data);
                return <div className='error'><section>Server request error</section></div>
            } else if(!isLoaded){
                return <div className='waiting'><section>Loading...</section></div>
            } else {
                return (
                    <ListView token={this.state.token} />
                )
            }
        }
    }
}

export default SignIn;
