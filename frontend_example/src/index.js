import React from "react";
import ReactDOM from "react-dom";
import OpenLayersMap from "./components/openLayersMap";

import "./css/map.css";

class ReactMap extends React.Component {
    render() {
        return (
            <div id="map"></div>
        );
    }

    componentDidMount() {
        this.map = new OpenLayersMap("map");
        this.map.drawGeoJSON(37.419670, -122.064930);
    }
}

ReactDOM.render(<ReactMap />, document.getElementById("index"));
