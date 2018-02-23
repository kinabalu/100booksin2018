import React, { Component } from 'react';
import styles from './css/BookProgress.css'

function precisionRound(number, precision) {
  var factor = Math.pow(10, precision);
  return Math.round(number * factor) / factor;
}

class BookProgress extends Component {
    render(){
        var readablePercent = precisionRound(this.props.percent, 1);
        var progressStyle = {
            width: this.props.percent+"%"
        }
        return (
            <section className={styles.ProgressBar}>
                <section className={styles.ProgressMarker} style={progressStyle} />
                <section className={styles.ProgressPercent}><b>{readablePercent}% </b><small>of {this.props.total} pages</small></section>
            </section>
        );
    }
}

export default BookProgress;