import json, requests
url_point = 'http://212.26.144.110/kadastrova-karta/find-Parcel'
url_data = 'http://212.26.144.110/kadastrova-karta/get-parcel-Info'

cadnum='6822789100:03:010:0064'

params_point = dict(
    cadnum=cadnum,
)

params_data = dict(
    koatuu = cadnum.split(':')[0],
    zone = cadnum.split(':')[1],
    quartal = cadnum.split(':')[2],
    parcel = cadnum.split(':')[3],
)

resp = (json.loads(requests.get(url=url_point, params=params_point).text)['data'])[0]
try:
    resp.update((json.loads(requests.get(url=url_data, params=params_data).text)['data'])[0])
    print(resp)
except:
    print("Нет данных")

