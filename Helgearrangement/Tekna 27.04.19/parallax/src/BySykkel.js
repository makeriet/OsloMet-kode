import React, { Component } from "react";
import axios from "axios";

import Circle from "./Circle";

export class BySykkel extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: null
    };
    axios
      .get("https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json")
      .then(Response => this.setState({ data: Response.data.data }));
  }

  createList = data => {
    let list = [];
    data.stations.forEach(element => {
      list.push(
        <Circle key={element.station_id} bikes={element.num_bikes_available} />
      );
    });

    return list;
  };

  render() {
    if (this.state.data) {
      console.log(this.state.data);

      var data = this.state.data;
      return <ul> {this.createList(data)} </ul>;
    }

    return <div>Loading...</div>;
  }
}

export default BySykkel;

// {
//   params: {
//     "Client-Identifier": "kode-parallaxExample"
//   }
// }
