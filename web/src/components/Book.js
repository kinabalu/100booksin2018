import React, { Component } from 'react';
import BookImage from './BookImage';
import BookDesc from './BookDesc';
import BookProgress from './BookProgress';
import styles from './css/Book.css'

class Book extends Component {
    render(){
        console.log(this.props.book);
        if(this.props.book.pages_read !== 0){
            //var percentProgress = (this.props.book.pages_read / this.props.book.pages) * 100;
            var percentProgress = (this.props.book.pages_read / 18) * 100;
        } else {
            var percentProgress = 0;
        }
        console.log(percentProgress);
        return (
            <div key={this.props.book.bookid} className={styles.Book}>
                <div className={styles.BookLayout}>
                    <BookImage imageurl={this.props.book.imageurl} />
                    <BookDesc book={this.props.book} />
                    <BookProgress percent={percentProgress} />
                </div>
            </div>
        )
    }
}

export default Book;