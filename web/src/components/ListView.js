import React, { Component } from 'react';
import CreateReadList from './CreateReadList';
import CreateToReadList from './CreateToReadList';
import Paginate from './Paginate';
import styles from './css/ListView.css';
import Cookies from 'universal-cookie';

class ListView extends Component{
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded: true,
            shelf: 0,
            cookies: new Cookies(),
            bookCount: 15,
            userError: false,
            userErrorMsg: "",
            page: 0,
            shelfCount: null
        }
        this.handleTabClick = this.handleTabClick.bind(this);
        this.logout = this.logout.bind(this);
        this.handleCountChange = this.handleCountChange.bind(this);
        this.sendBookCount = this.sendBookCount.bind(this);
        this.handlePageChange = this.handlePageChange.bind(this);

        if(this.props.bookCount){
            this.state.bookCount = this.props.bookCount;
        }
    }
    handlePageChange(whatPage){
        this.setState({
            page: whatPage
        })
    }
    handleTabClick(id, e){
      this.setState({
        shelf: id,
        page: 0,
      })
    }
    handleCountChange(e){
        if(!isNaN(e.target.value)){
            this.setState({
                bookCount: e.target.value,
                userError:false,
                userErrorMsg:"",
                page: 0,
            })
        } else {
            this.setState({
                userError: true,
                userErrorMsg: "Book count must be a number",
            });
        }
    }
    componentDidMount(){}
    logout(){
        this.state.cookies.remove("GRUserToken");
        window.location.reload();
    }
    sendBookCount(count){
        this.setState({
            shelfCount: count
        })
    }
    render(){
        var { error, isLoaded, submitted, userError, userErrorMsg, shelf } = this.state
        var preMsg = "";
        var shelfElement = ""
        if(userError){
            preMsg = <div className='error'><section>{userErrorMsg}</section></div>
        }

        if(shelf === 0){
            shelfElement = <CreateReadList page={this.state.page} onDone={this.sendBookCount} bookCount={this.state.bookCount} token={this.props.token} />
        } else if(shelf === 1) {
            shelfElement = <CreateToReadList page={this.state.page} onDone={this.sendBookCount} bookCount={this.state.bookCount} token={this.props.token} />
        }

        var firstTabSelected = (shelf === 0)? " " + styles.selectedTab:"";
        var secondTabSelected = (shelf === 1)? " " + styles.selectedTab:"";

        return (
          <div>
          <div className={styles.TabsContainer}>
            <nav className={styles.Tabs}>
              <section className={styles.bookCount}>
                  <select className={styles.countSelect} value={this.state.bookCount} onChange={this.handleCountChange}>
                      <option value="5">5</option>
                      <option value="10">10</option>
                      <option value="15">15</option>
                      <option value="20">20</option>
                      <option value="25">25</option>
                      <option value="30">30</option>
                  </select>
              </section>
              <input type="button" className={styles.firstTab + firstTabSelected} value="read" onClick={this.handleTabClick.bind(this, 0)} />
              <input type="button" className={styles.secondTab + secondTabSelected} value="to-read" onClick={this.handleTabClick.bind(this, 1)} />
              <input type='button' className={styles.logout} value='Logout' onClick={this.logout.bind(this)} />
            </nav>
            {preMsg}
            {shelfElement}
          </div>
          <footer className="footer">
            <Paginate currentPage={this.state.page} bookCount={this.state.bookCount} shelfCount={this.state.shelfCount} pageChange={this.handlePageChange} />
          </footer>
          </div>
        );
    }
}

export default ListView;
