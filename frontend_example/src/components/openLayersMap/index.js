import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';
import GeoJSON from 'ol/format/GeoJSON.js';
import {Vector as VectorLayer} from 'ol/layer.js';
import {Vector as VectorSource} from 'ol/source.js';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style.js';
import React from "react";
import 'ol/ol.css';
import './style.css';
import $ from "jquery";
import Overlay from 'ol/Overlay.js';


import {toStringHDMS} from 'ol/coordinate.js';
import {fromLonLat, toLonLat} from 'ol/proj.js';



class OpenLayersMap extends React.Component {
  render() {
    $("#map").height($("#map").parent().height());
    return (
      <div id="map"></div>
    );
  }

  componentDidMount() {
    this.map = new Map({
      controls: [],
      target: "map",
      layers: [
        new TileLayer({
          source: new XYZ({
            url: 'https://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png'
          })
        })
      ],
      view: new View({
        center: [-122.064930, 37.419670],
        zoom: 12,
        projection: "EPSG:4326",
      })
    });
    $("#map").height($("#map").parent().height());
    this.map.updateSize();

    // draw stuff when objects store has changed
    this.props.objectStore.subscribe(function () {
      for (let vl of this.vectorLayers)
      {
        this.map.removeLayer(vl);
      }
      this.vectorLayers = [];
      let filteredObjects = this.props.objectStore.getState().filteredObjects;
      let filteredPoints  = filteredObjects.map((x) => (x.point.coordinates));
      for (let p of filteredPoints) {
        this.drawGeoJSON(p[1], p[0]);
      }
    }.bind(this));

    // Popup showing the position the user clicked
    this.popup = new Overlay({
      element: document.getElementById('popoverButton')
    });
    this.map.addOverlay(this.popup);

    // popup magic
    this.map.on('click', function(event) {
      var feature = this.map.forEachFeatureAtPixel(event.pixel, function(feature, layer) {
        return feature;
      });

      if (feature)
      {
        console.log(feature);
        $("#popoverButton").show();
        let coordinate = event.coordinate;
        let hdms = toStringHDMS(toLonLat(coordinate));
        this.popup.setPosition(coordinate);
        this.setPopoverText(feature.values_.geometry.flatCoordinates[0]);
      }

      
    }.bind(this));
  
  }

  constructor(props) {
    super(props);
    this.vectorLayers = [];
  }

  setPopoverText(text) {
    this.props.popoverStore.dispatch({
      type: "change-text",
      text: text,
    });
  }

  drawGeoJSON(latitude, longitude) {
    var image = new CircleStyle({
      radius: 5,
      fill: new Fill({
        color: 'rgba(255, 0, 0, 1)'
      }),
      stroke: new Stroke({color: 'red', width: 1})
    });
    
    var styles = {
      'Point': new Style({
        image: image
      }),
      'Polygon': new Style({
        stroke: new Stroke({
          color: 'blue',
          lineDash: [4],
          width: 3
        }),
        fill: new Fill({
          color: 'rgba(255, 255, 255, 1)'
        })
      })
    };

    var styleFunction = function (feature) {
      return styles[feature.getGeometry().getType()];
    };

    var geojsonObject = {
      'type': 'FeatureCollection',
      'crs': {
        'type': 'name',
        'properties': {
          'name': 'EPSG:4326'
        }
      },
      'features': [
        {
        'type': 'Feature',
        'geometry': {
          "type": "Point",
          "coordinates": [
                longitude,
                latitude,
              ]
        }
      }]
    };

    var vectorSource = new VectorSource({
      features: (new GeoJSON()).readFeatures(geojsonObject)
    });

    let vl = new VectorLayer({
      source: vectorSource,
      style: styleFunction
    })

    this.vectorLayers.push(vl);

    this.map.addLayer(vl);    
  }
}

export default OpenLayersMap;