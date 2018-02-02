import React, { Component } from 'react';
import List from './List';

class ListView extends Component{
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            result: null,
        }
    }
    componentDidMount(){
        var url = "http://192.168.99.100:8080/getread?grid="+this.props.grid;
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
            return <div className='error'>Error in fetch - ListView</div>
        } else if(!isLoaded){
            return <div className='waiting'>Loading...</div>
        } else if(results.fail){
            return <div className='error'>Error on server - ListView</div>
        } else {
            return (
                <section id='ListView'>
                    <List results={results} />
                </section>
            );
        }
    }
}

export default ListView;