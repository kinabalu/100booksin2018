import React, { Component } from 'react';
import Book from './Book';
import styles from './css/List.css'

class List extends Component {
    render(){
        return(
            <section className={styles.BookListWrap} id='BookListWrap'>
                <div className={styles.BookList} id='BookList'>
                    {this.props.results.result.result.map(function(key, result){
                        //console.log(key, result)
                        //return <li key={key.bookid}>{result}</li>
                        return <Book key={key.bookid} book={key} />
                    })}
                </div>
            </section>
        )
    }
}

export default List;