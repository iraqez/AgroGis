import json, requests
url = 'http://212.26.144.110/kadastrova-karta/find-Parcel'
url2 = ''
cadnum='6822789100:03:010:0064'

params = dict(
        cadnum=cadnum,
        koatuu=koatuu,
        zone=zone,
        quartal=quartal,
        parcel=parcel,
)
# params = dict(
#     cadnum=cadnum,
# )

koatuu = cadnum.split(':')[0]
zone = cadnum.split(':')[1]
quartal = cadnum.split(':')[2]
parcel = cadnum.split(':')[3]

resp = requests.get(url=url, params=params(cadnum))
data = json.loads(resp.text)
data=((data['data'])[0])

print(data)

# data=(dict(data))
# xmax=(str(data.get('st_xmax')))
# xmin=(str(data.get('st_xmin')))
# ymax=(str(data.get('st_ymax')))
# ymin=(str(data.get('st_ymin')))
#
# print('Кадастровый номер: '+cadnum)
# print('КОАТУУ = ' + koatuu)
# print('Зона = ' + zone)
# print('Квартал = ' + quartal)
# print('Номер участка = ' + parcel)

# print('Координаты крайних точек = '+xmax+' '+ymax+'_'+xmin+'_'+ymin)
# print('Верхняя правая: '+xmax+' '+ymax)
# print('Нижняя левая: '+xmin+' '+ymin)