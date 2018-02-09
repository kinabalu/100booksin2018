import React, { Component } from 'react';
import List from './List';
//import styles from './css/List.css'

class CreateReadList extends Component {
  constructor(props){
      super(props);
      this.state = {
          error: null,
          isLoaded: false,
          result: null,
      }
  }
  componentDidMount(){
      var url = "http://192.168.99.100:8080/shelf/"+this.props.token+"/read";

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
              <List results={results} />
          </section>
        );
      }
    }
}

export default CreateReadList;
