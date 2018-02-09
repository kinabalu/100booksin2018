import React, { Component } from 'react';
import ListView from './ListView';
import styles from './css/SignIn.css'
import Cookies from 'universal-cookie';

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
            cookies: new Cookies()
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(event) {
        this.setState({value: event.target.value});
    }
    handleSubmit(event){
        // Validate input
        this.setState({
            submitted: true
        });
        fetch("http://192.168.99.100:8080/user/"+this.state.value)
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
        var { error, isLoaded, result, submitted } = this.state

        if(!submitted){
            return(
                <form onSubmit={this.handleSubmit}>
                    <section className={styles.SignIn}>
                        <section className={styles.gridInfo}>
                            GoodReads user ID:
                        </section>
                        <section className={styles.grid}>
                            <input value={this.state.value} onChange={this.handleChange} />
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
