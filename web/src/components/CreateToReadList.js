import React, { Component } from 'react';
import List from './List';
import { Config } from '../config.js';
//import styles from './css/List.css'

class CreateToReadList extends Component {
  constructor(props){
      super(props);
      this.state = {
          error: null,
          isLoaded: false,
          result: null,
      }
  }
  componentDidMount(){
      var url = Config.apiIp+"/shelf/"+this.props.token+"/to-read";

      console.log(url);

      fetch(url)
          .then(res => res.json())
          .then(
              (result) => {
                  this.setState({
                      isLoaded: true,
                      results: {result}
                  });
              },
              (error) => {
                  this.setState({
                      isLoaded: false,
                      error: true
                  });
              }
          );
  }
    render(){
      var { error, isLoaded, results } = this.state

      if(error){
          return <div className='error'><section>Server request error</section></div>
      } else if(!isLoaded){
          return <div className='waiting'><section>Loading...</section></div>
      } else if(results.fail){
          return <div className='error'><section>Server error</section></div>
      } else {
        return(
          <section id='ListView'>
              <List bookCount={this.props.bookCount} token={this.props.token} results={results} />
          </section>
        );
      }
    }
}

export default CreateToReadList;
