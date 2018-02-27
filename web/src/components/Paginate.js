import React, { Component } from 'react';
import styles from './css/Paginate.css';

class Paginate extends Component {
    constructor(props){
        super(props);
        this.state = {
            page: 0
        }
        this.setPage = this.setPage.bind(this)
    }
    numberOfPages(){
        var numberOfPages = 1;
        var sc = this.props.shelfCount;
        var bc = this.props.bookCount;
        if(sc > bc){
            numberOfPages = Math.ceil(sc / bc);
        }
        return numberOfPages;
    }
    setPage(page){
        this.props.pageChange(page);
    }
    makeLinkList(){
        var numberOfPages = this.numberOfPages();
        var currentPage = this.props.currentPage;

        //alert(numberOfPages + " / " + currentPage + " / " + this.props.shelfCount)

        var firstPage, previousPage, nextPage, lastPage = "";

        if(currentPage !== 0){
            firstPage = (
                <li className={styles.pageLink} >
                    <a onClick={() => this.setPage(0)}>First</a>
                </li>
            )
            previousPage = (
                <li className={styles.pageLink} >
                    <a onClick={() => this.setPage(currentPage - 1)}>Previous</a>
                </li>
            )
        }
        console.log(currentPage, numberOfPages)
        if(currentPage !== (numberOfPages - 1)){
            nextPage = (
                <li className={styles.pageLink} >
                    <a onClick={() => this.setPage(currentPage + 1)}>Next</a>
                </li>
            )
            lastPage = (
                <li className={styles.pageLink} >
                    <a onClick={() => this.setPage(numberOfPages)}>Last</a>
                </li>
            )
        }

        return (
            <ul className={styles.pageList}>
                {firstPage}
                {previousPage}
                <li className={styles.pageLink} >
                    <strong>{currentPage + 1}</strong>
                </li>
                {nextPage}
                {lastPage}
            </ul>
        )
    }
    render(){
        if(this.props.shelfCount !== null){
            return (
                <section>
                    {this.makeLinkList()}
                </section>
            )
        }
        return ""
    }
}

export default Paginate;