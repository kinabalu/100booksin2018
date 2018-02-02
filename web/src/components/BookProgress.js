import React, { Component } from 'react';
import styles from './css/BookProgress.css'

class BookProgress extends Component {
    render(){
        var progressStyle = {
            width: this.props.percent+"%"
        }
        return (
            <section className={styles.ProgressBar}>
                <section className={styles.ProgressMarker} style={progressStyle} />
                <section className={styles.ProgressPercent}>{this.props.percent}%</section>
            </section>
        );
    }
}

export default BookProgress;