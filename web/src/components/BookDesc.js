import React, { Component } from 'react';
import styles from './css/BookDesc.css'
import { Config } from '../config.js';

class BookDesc extends Component {
    constructor(props){
        super(props);
        this.state = {
            isLoaded: false,
            result: {},
            error: false,
            data: "",
            pages_read: this.props.pages_read,
            newvalue: this.props.pages_read
        }
        this.newPagesRead = this.newPagesRead.bind(this);
        this.handleSumbit = this.handleSumbit.bind(this);
    }
    newPagesRead(input){
       this.setState({
            newvalue: input.target.value
       });
    }
    handleSumbit(event){
        var newPages = this.state.newvalue;
        var url = Config.apiIp+"/pagesread/"+this.props.token+"/"+this.props.book.bookid+"/"+newPages;

        console.log(url)

        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        result: result,
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: false,
                        error: true,
                        data: error
                    });
                }
            ).then(() => {
                console.log(this.state.result)
            });
        event.preventDefault();
    }
    render(){
        var defacto = this.state.pages_read;
        return (
            <div className={styles.BookInfoWrap}>
                <div className={styles.BookInfoGrid}>
                    <header className={styles.BookInfoTitle}>
                        <b>{this.props.book.title}</b>
                    </header>
                    <section className={styles.BookInfoPages}>
                        Youve read: <form onSubmit={this.handleSumbit}><input onChange={this.newPagesRead} className={styles.pagesInput} defaultValue={defacto} /></form> of {this.props.book.pages} pages.
                    </section>
                </div>
            </div>
        )
    }
}

export default BookDesc;
