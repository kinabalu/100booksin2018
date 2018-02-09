import React, { Component } from 'react';
import styles from './css/BookDesc.css'

class BookDesc extends Component {
    render(){
        return (
            <div className={styles.BookInfoWrap}>
                <div className={styles.BookInfoGrid}>
                    <header className={styles.BookInfoTitle}>
                        <b>{this.props.book.title}</b>
                    </header>
                    <section className={styles.BookInfoPages}>
                        
                    </section>
                </div>
            </div>
        )
    }
}

export default BookDesc;
