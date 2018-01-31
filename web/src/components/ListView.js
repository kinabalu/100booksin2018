import React, { Component } from 'react';

class ListView extends Component{
    constructor(props){
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            result: null
        }
    }
    componentDidMount(){
        fetch("http://192.168.99.100:8080/getread")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        result: result
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
        var { error, isLoaded, result } = this.state
        if(error){
            return <div class='error'>Error in fetch</div>
        } else if(!isLoaded){
            return <div class='waiting'>Loading...</div>
        } else {
            console.log(result);
            return(
                <section id='ListView'>
                    <h1>Signed in, listview here</h1>
                </section>
            );
        }
    }
}

export default ListView;