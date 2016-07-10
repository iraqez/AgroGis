import psycopg2
import postgis


import datacadnum

cd = datacadnum.resp
conn = psycopg2.connect("host=agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
cur = conn.cursor()


lat = str(datacadnum.resp.get('lat'))
lng = str(datacadnum.resp.get('long'))
cadnum = datacadnum.resp.get('cadnum')
geom = postgis.Point(x=lng, y=lat, srid=4326)

cur.execute('INSERT INTO cadnum(geom, lat, lng, cadnum) VALUES (%s, %s, %s, %s)',(geom, lat, lng, cadnum))
conn.commit()

cur.close()
conn.close()
#cur.execute('INSERT INTO cadnum(id, geom, lat, "long", cadnum) VALUES ()
            #(1, ST_SetSRID(ST_MakePoint(48.92512215545735, 28.43709578282804), 4326), 48.92512215545735, 28.43709578282804, "0524587000:01:003:0358"))