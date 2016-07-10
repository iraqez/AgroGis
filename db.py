import psycopg2
import postgis


import datacadnum

cd = datacadnum.resp
conn = psycopg2.connect("host=agro2012.com.ua dbname=agro2012 user=postgres password=workfree")
cur = conn.cursor()

s1 = datacadnum.params_point.get('cadnum')
print(type(s1))
cur.execute('SELECT count(*) FROM cadnum where cadnum = %s', ('0524587000:01:003:0358',))
s = cur.fetchone()
print(s[0])

if s[0] == 0:
    lat = str(datacadnum.resp.get('lat'))
    lng = str(datacadnum.resp.get('long'))
    cadnum = datacadnum.resp.get('cadnum')
    geom = postgis.Point(x=lng, y=lat, srid=4326)

    cur.execute('INSERT INTO cadnum(geom, lat, lng, cadnum) VALUES (%s, %s, %s, %s)',(geom, lat, lng, cadnum))
    conn.commit()
else:
    print('Номер {} существует в базе!!!'.format(s1) )

cur.close()
conn.close()