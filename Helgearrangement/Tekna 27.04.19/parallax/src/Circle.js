import React, { Component } from "react";

export class Circle extends Component {
  render() {
    var circleStyle = {
      padding: 10,
      margin: 20,
      display: "inline-block",
      backgroundColor: "#1C89BF",
      borderRadius: "50%",
      width: this.props.bikes * 10 + 1,
      height: this.props.bikes * 10 + 1
    };
    return <div style={circleStyle} />;
  }
}

export default Circle;
