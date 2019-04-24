import React from "react";
import ZoomReveal from "react-reveal/Zoom"; // Importing Zoom effect
import logo from "./logo.svg";

export default function Zoom() {
  return (
    <div>
      <ZoomReveal>
        {/*Using ZoomReveal Effect*/}
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
      </ZoomReveal>
    </div>
  );
}
