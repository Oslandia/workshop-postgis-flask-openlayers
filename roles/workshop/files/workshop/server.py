from flask import Flask
from psycopg2 import connect

app = Flask(__name__)

@app.route('/geojson')
def geojson():
    with connect("service=workshop") as con:
        cur = con.cursor()
        cur.execute("""
            select json_build_object(
                'type', 'FeatureCollection',
                'features', json_agg(ST_AsGeoJSON(verre.*)::json)
            ) as geojson
            from verre
            """)
        return cur.fetchone()[0]

@app.route('/<path:path>')
def send_file(path):
    return app.send_static_file(path)

@app.route('/bati/<z>/<x>/<y>')
def bati(z, x, y):
    with connect("service=workshop") as con:
        cur = con.cursor()
        cur.execute("""
            with 
            bounds as ( 
                select ST_Segmentize(ST_MakeEnvelope(x_min, y_min, x_max, y_max, 3857), 100) as geom,
                       ST_MakeEnvelope(x_min, y_min, x_max, y_max, 3857)::box2d as bbox
                from (values (
                    {x} * (40075016/2^{z}) - 40075016/2, 
                    ({x}+1) * (40075016/2^{z}) - 40075016/2,
                    40075016/2 - ({y}+1) * (40075016/2^{z}),
                    40075016/2 - {y}*(40075016/2^{z})
                    )) as t(x_min, x_max, y_min, y_max)
            ), 
            mvtgeom AS ( 
                select ST_AsMVTGeom(ST_Transform(bati.msgeometry, 3857), bounds.bbox) AS geom, type, gid
                from bati, bounds
                where ST_Intersects(bati.msgeometry, ST_Transform(bounds.geom, 4171)) 
            ) 
            select ST_AsMVT(mvtgeom.*) from mvtgeom
            """.format(z=z, x=x, y=y))
        return bytes(cur.fetchone()[0])


if __name__=="__main__":
    app.run(host='0.0.0.0', port='5000')
