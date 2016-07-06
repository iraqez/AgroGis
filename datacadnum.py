import json, requests
import coordinates
url_point = 'http://212.26.144.110/kadastrova-karta/find-Parcel'
url_data = 'http://212.26.144.110/kadastrova-karta/get-parcel-Info'

cadnum='0523080200:02:001:0200'
#cadnum = input('Вставьте кадастровый номер: ')

params_point = dict(
    cadnum=cadnum,
)

resp = (json.loads(requests.get(url=url_point, params=params_point).text)['data'])[0]
try:
    params_data = dict(
        koatuu=cadnum.split(':')[0],
        zone=cadnum.split(':')[1],
        quartal=cadnum.split(':')[2],
        parcel=cadnum.split(':')[3],
    )
    resp.update((json.loads(requests.get(url=url_data, params=params_data).text)['data'])[0])
    coordinates.addCoordinates(resp)
    print(resp)
except:
    print("Нет данных по {}".format(cadnum))
