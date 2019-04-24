// This example is live editable
import React, { Component } from "react";

import L from "leaflet";

import "./App.css";
import "leaflet/dist/leaflet.css";
// import BySykkel from "./BySykkel";
import BySykkelStasjoner from "./BySykkelStasjoner";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png")
});

class App extends Component {
  render() {
    return <BySykkelStasjoner />;
  }
}

export default App;
