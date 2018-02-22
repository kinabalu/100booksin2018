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
            pages_read: this.props.pages_read
        }
        this.newPagesRead = this.newPagesRead.bind(this);
    }
    newPagesRead(input){
        // Send ajax
        var newPages = input.target.value;
        var url = Config.apiIp+"/pagesread/"+this.props.token+"/"+this.props.book.bookid+"/"+newPages;

        console.log(url)

        var pr = this.props.pages_read
        fetch(url)
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        result: result,
                        pages_read: pr+1
                    });
                },
                (error) => {
                    this.setState({
                        isLoaded: false,
                        error: true,
                        data: error
                    });
                }
            );
        console.log(this.state.result);
        this.forceUpdate();
    }
    render(){
        return (
            <div className={styles.BookInfoWrap}>
                <div className={styles.BookInfoGrid}>
                    <header className={styles.BookInfoTitle}>
                        <b>{this.props.book.title}</b>
                    </header>
                    <section className={styles.BookInfoPages}>
                        Youve read: <input onChange={this.newPagesRead} className={styles.pagesInput} value={this.state.pages_read} type='number' /> of {this.props.book.pages} pages.
                    </section>
                </div>
            </div>
        )
    }
}

export default BookDesc;
