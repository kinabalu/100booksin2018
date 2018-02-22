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
            bookCount: 15
        }
        this.handleTabClick = this.handleTabClick.bind(this);
        this.logout = this.logout.bind(this);
        this.handleCountChange = this.handleCountChange.bind(this);
    }
    handleTabClick(id, e){
      this.setState({
        shelf: id
      })
    }
    handleCountChange(e){
        this.setState({
            bookCount: e.target.value
        })
    }
    componentDidMount(){}
    logout(){
        this.state.cookies.remove("GRUserToken");
        window.location.reload();
    }
    render(){
        var shelf = this.state.shelf
        if(shelf === 0){
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
              <CreateReadList bookCount={this.state.bookCount} token={this.props.token} />
            </div>
          );
      } else if(shelf === 1){
          return(
            <div className={styles.TabsContainer}>
              <nav className={styles.Tabs}>
                  <section className={styles.bookCount}>
                      <select className={styles.countSelect}>
                          <option value="5">5</option>
                          <option value="10">10</option>
                          <option value="15" selected>15</option>
                          <option value="20">20</option>
                          <option value="25">25</option>
                          <option value="30">30</option>
                      </select>
                  </section>
                <input type="button" className={styles.firstTab} value="read" onClick={this.handleTabClick.bind(this, 0)} />
                <input type="button" className={styles.secondTab + " " + styles.selectedTab} value="to-read" onClick={this.handleTabClick.bind(this, 1)} />
                <input type='button' className={styles.logout} value='Logout' onClick={this.logout.bind(this)} />
              </nav>
              <CreateToReadList bookCount={this.state.bookCount} token={this.props.token} />
            </div>
          );
        } else {


        }
    }
}

export default ListView;
