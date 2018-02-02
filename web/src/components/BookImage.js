import React, { Component } from 'react';
import styles from './css/BookImage.css'

class BookImage extends Component {
    render(){
        return (
            <div className={styles.BookImageWrap}>
                <img className={styles.BookImage} src={this.props.imageurl} alt='' />
            </div>
        )
    }
}

export default BookImage;