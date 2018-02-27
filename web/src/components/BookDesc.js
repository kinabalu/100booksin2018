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
            newvalue: this.props.pages_read,
            pagesEdited: false,
            pagesSaved: false,
            userError: false,
            userErrorMsg: "",
        }
        this.newPagesRead = this.newPagesRead.bind(this);
        this.handleSumbit = this.handleSumbit.bind(this);
    }
    newPagesRead(input){
       this.setState({
            newvalue: input.target.value,
            pagesEdited: true,
            pagesSaved: false
       });
    }
    handleSumbit(event){
        if(!this.state.pagesEdited){
            event.preventDefault();
            return false
        }
        var newPages = this.state.newvalue;
        //var url = Config.apiIp+"/pagesread/"+this.props.token+"/"+this.props.book.bookid+"/"+newPages;
        var url = Config.apiIp+"/pagesread/"+this.props.token+"/"+this.props.book.bookid+"/"+newPages;

        console.log(url)

        var onDone = this.props.renderNew;

        fetch(url)
            .then(res => res.json())
            .then((result) => {
                    this.setState({
                        isLoaded: true,
                        result: result,
                        pagesSaved: true,
                        pagesEdited: false
                    })
                    onDone(newPages);
                }, (error) => {
                    this.setState({
                        isLoaded: false,
                        error: true,
                        data: error,
                        userError: true,
                        userErrorMsg: "Server error"
                    })
                })
        this.forceUpdate();
        event.preventDefault();
    }
    render(){
        var defacto = this.state.pages_read;
        var preMsg = ""
        var { userErrorMsg, userError } = this.state;
        var classes = styles.pagesInput; // {"pagesInput": true, "input-edited": this.state.pagesEdited, "input-saved":false}
        if(this.state.pagesEdited) classes += " " + styles.inputEdited;
        if(this.state.pagesSaved) classes += " " + styles.inputSaved;

        if(userError){
            preMsg = <div className='error'><section>{userErrorMsg}</section></div>
        }

        return (
            <div className={styles.BookInfoWrap}>
                {preMsg}
                <div className={styles.BookInfoGrid}>
                    <header className={styles.BookInfoTitle}>
                        <b>{this.props.book.title}</b>
                    </header>
                    <section className={styles.BookInfoPages}>
                        Youve read: <form onSubmit={this.handleSumbit}><input onChange={this.newPagesRead} className={classes} defaultValue={defacto} /><input type='submit' className={styles.pagesSubmit} value="✓" /></form> pages.
                    </section>
                </div>
            </div>
        )
    }
}

export default BookDesc;
