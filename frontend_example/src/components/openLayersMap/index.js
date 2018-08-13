import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import XYZ from 'ol/source/XYZ';
import GeoJSON from 'ol/format/GeoJSON.js';
import {Vector as VectorLayer} from 'ol/layer.js';
import {Vector as VectorSource} from 'ol/source.js';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style.js';

import 'ol/ol.css';

class OpenLayersMap {
  constructor(divName) {
    this.map = new Map({
      target: divName,
      layers: [
        new TileLayer({
          source: new XYZ({
            url: 'https://{a-c}.tile.openstreetmap.org/{z}/{x}/{y}.png'
          })
        })
      ],
      view: new View({
        center: [-122.064930, 37.419670],
        zoom: 18,
        projection: "EPSG:4326",
      })
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

    var vectorLayer = new VectorLayer({
      source: vectorSource,
      style: styleFunction
    });

    this.map.addLayer(vectorLayer);
  }
}

export default OpenLayersMap;