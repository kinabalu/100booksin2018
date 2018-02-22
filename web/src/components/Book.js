import React, { Component } from 'react';
import BookImage from './BookImage';
import BookDesc from './BookDesc';
import BookProgress from './BookProgress';
import styles from './css/Book.css'

class Book extends Component {
    constructor(props){
        super(props);
        this.state = {
            pages: this.props.book.pages_read
        }
        this.handlePercentChange = this.handlePercentChange.bind(this);
    }
    handlePercentChange(newPages){
        this.setState({
            pages: newPages
        })
        this.forceUpdate()
        console.log("RERender")
    }
    render(){

        var percentProgress = 0
        if(this.props.book.pages_read !== 0){
            percentProgress = (this.props.book.pages_read / this.props.book.pages) * 100;
        }
        return (
            <div key={this.props.book.bookid} className={styles.Book}>
                <div className={styles.BookLayout}>
                    <BookImage imageurl={this.props.book.imageurl} />
                    <BookDesc token={this.props.token} renderNew={this.handlePercentChange} pages_read={this.props.book.pages_read} book={this.props.book} />
                    <BookProgress percent={percentProgress} />
                </div>
            </div>
        )
    }
}

export default Book;
