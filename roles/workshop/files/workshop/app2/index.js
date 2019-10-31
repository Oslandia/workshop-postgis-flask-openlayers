import 'ol/ol.css';
import {Map, View} from 'ol';
import TileLayer from 'ol/layer/Tile';
import VectorLayer from 'ol/layer/Vector';
import OSM from 'ol/source/OSM';
import VectorSource from 'ol/source/Vector';
import GeoJSON from 'ol/format/GeoJSON';
import {transform} from 'ol/proj';

const map = new Map({
    target: 'map',
    layers: [
        new TileLayer({
            source: new OSM()
            }),
        new VectorLayer({
            title: 'verre',
            source: new VectorSource({
                url: 'geojson',
                format: new GeoJSON()
                })
            }),
        new VectorTileLayer({
            title: 'bati',
            source: new VectorTileSource({
                format: new MVT(),
                url: `bati/{z}/{x}/{y}`,
                })
            })
        ],
    view: new View({
        center: transform([4.83, 45.76], 'EPSG:4326', 'EPSG:3857'),
        zoom: 14
        })
});
