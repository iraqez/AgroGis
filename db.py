import psycopg2
import postgis

import datacadnum

cd = datacadnum.resp
conn = psycopg2.connect("host=gis.agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
cur = conn.cursor()

s1 = datacadnum.params_point.get('cadnum')
cur.execute('SELECT count(*) FROM cadnum_point where cadnum = %s', (s1,))
s = cur.fetchone()

if s[0] == False:
    lat = str(datacadnum.resp.get('lat'))
    lng = str(datacadnum.resp.get('long'))
    cadnum = datacadnum.resp.get('cadnum')
    geom = postgis.Point(x=lng, y=lat, srid=4326)
    area = str(datacadnum.resp.get('area'))

    cur.execute('INSERT INTO cadnum_point(geom, cadnum) VALUES (%s, %s)', (geom, cadnum))
    conn.commit()
    logstr = ('Номер {} успешно добавлен!!!'.format(s1) )
else:
    logstr = ('Номер {} существует в базе!!!'.format(s1) )

cur.close()
conn.close()

print(logstr)