import React, { Component } from 'react';

class App extends Component {
  state = {
    blog_posts: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/');
      const blog_posts = await res.json();
      this.setState({
        blog_posts
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.blog_posts.map(item => (
          <div>
            <h1>{item.title}</h1>
            <span>{item.body}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
