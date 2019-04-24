import React, { Component } from "react";
import axios from "axios";
// import tripData from "./trips-2018.6.1-2018.6.30.json";
import weights from "./06.18.Compiled.json";

import {
  Map as LeafletMap,
  TileLayer,
  CircleMarker,
  Popup,
  Polyline
} from "react-leaflet";

export class BySykkelStasjoner extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stations: null,
      lines: [],
      trips: []
    };
    axios
      .get(
        "https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json"
      )
      .then(Response =>
        this.setState({ stations: Response.data.data.stations })
      )
      .catch(error => {
        console.log(error.response);
      });
  }

  drawLines(center, from_station) {
    let list = [];
    console.log(weights);
    console.log(from_station);
    let weight = weights[from_station];
    console.log(typeof weight);

    if (weight) {
      Object.keys(weight).forEach(element => {
        var toCenter = this.state.stations[element];
        if (toCenter) {
          list.push(
            <Polyline
              key={"l" + element}
              color="purple"
              positions={[center, toCenter]}
              weight={1 + weight[element] * 0.5}
            />
          );
        }
      });
      this.setState({ lines: list });
    }
  }

  createList = stations => {
    let list = [];
    stations.forEach(element => {
      var center = [element.lat, element.lon];
      list.push(
        <CircleMarker
          key={element.station_id}
          center={center}
          fillColor="blue"
          radius={7}
          onclick={() => {
            this.drawLines(center, parseInt(element.station_id));
          }}
        >
          <Popup>
            <span>{element.station_id}</span>
          </Popup>
        </CircleMarker>
      );
    });

    return list;
  };

  render() {
    var position = [59.91, 10.75];
    if (this.state.stations) {
      var stations = this.state.stations;
      return (
        <LeafletMap center={position} zoom={11}>
          <TileLayer url="http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=norges_grunnkart_graatone&zoom={z}&x={x}&y={y}" />
          {this.createList(stations)}
          {this.state.lines}
        </LeafletMap>
      );
    }

    return <div>Loading...</div>;
  }
}

export default BySykkelStasjoner;

// {
//   params: {
//     "Client-Identifier": "kode-parallaxExample"
//   }
// }
