from owslib.wms import WebMapService
wms = WebMapService('http://212.26.144.110/geowebcache/service/wms', version='1.1.1')

wms.getfeatureinfo(layers='kadastr', query_layers='kadastr',styles='',
                   info_format='application/vnd.ogc.gml',srs='EPSG:900913')