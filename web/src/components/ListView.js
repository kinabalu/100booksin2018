import React, { Component } from 'react';
import CreateReadList from './CreateReadList';
import CreateToReadList from './CreateToReadList';
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
        }
        this.handleTabClick = this.handleTabClick.bind(this);
        this.logout = this.logout.bind(this);
        this.handleCountChange = this.handleCountChange.bind(this);

        if(this.props.bookCount){
            this.state.bookCount = this.props.bookCount;
        }
    }
    handleTabClick(id, e){
      this.setState({
        shelf: id
      })
    }
    handleCountChange(e){
        if(!isNaN(e.target.value)){
            this.setState({
                bookCount: e.target.value,
                userError:false,
                userErrorMsg:""
            })
        } else {
            this.setState({
                userError: true,
                userErrorMsg: "Book count must be a number"
            });
        }
    }
    componentDidMount(){}
    logout(){
        this.state.cookies.remove("GRUserToken");
        window.location.reload();
    }
    render(){
        var { error, isLoaded, submitted, userError, userErrorMsg, shelf } = this.state
        var preMsg = "";
        var shelfElement = ""
        if(userError){
            preMsg = <div className='error'><section>{userErrorMsg}</section></div>
        }

        if(shelf == 0){
            shelfElement = <CreateReadList bookCount={this.state.bookCount} token={this.props.token} />
        } else if(shelf == 1) {
            shelfElement = <CreateToReadList bookCount={this.state.bookCount} token={this.props.token} />
        }

        return (
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
              <input type="button" className={styles.firstTab + " " + styles.selectedTab} value="read" onClick={this.handleTabClick.bind(this, 0)} />
              <input type="button" className={styles.secondTab} value="to-read" onClick={this.handleTabClick.bind(this, 1)} />
              <input type='button' className={styles.logout} value='Logout' onClick={this.logout.bind(this)} />
            </nav>
            {preMsg}
            {shelfElement}
          </div>
        );
    }
}

export default ListView;
