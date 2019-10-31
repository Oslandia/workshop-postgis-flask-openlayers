import 'ol/ol.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import OSM from 'ol/source/OSM';
import VectorSource from 'ol/source/Vector';
import GeoJSON from 'ol/format/GeoJSON';

const map = new Map({
    target: 'map',
    layers: [
        new TileLayer({
            source: new OSM()
            }),
        new VectorLayer({
              title: 'verre',
              source: new VectorSource({
                 projection : 'EPSG:4171',
                 url: 'geojson',
                 format: new GeoJSON()
              })
           })
        ],
    view: new View({
        center: [0, 0],
        zoom: 0
        })
});
