import React, { Component } from 'react';
import Book from './Book';
import styles from './css/List.css'

class List extends Component {
    render(){
        var bookCount = this.props.bookCount;
        var token = this.props.token;
        //console.log(this.props.results.result.result)
        var page = this.props.page;
        var pageStart = bookCount * page;
        var pageEnd = pageStart + parseInt(bookCount);

        console.log(pageStart, pageEnd);

        return(
            <section className={styles.BookListWrap} id='BookListWrap'>
                <div className={styles.BookList} id='BookList'>
                    {this.props.results.result.result.slice(pageStart, pageEnd).map(function(key, result){
                        return <Book token={token} key={key.bookid} book={key} />
                    })}
                </div>
            </section>
        )
    }
}

export default List;
