#!/usr/bin/env python
# folium : 지도를 표시해주는 라이브러리
import folium
latitude = 37.566345
longitutbe = 126.977893

map_osm = folium.Map(location=[latitude, longitutbe])
map_osm.save('./xx_map1.html')
print(type(map_osm))

map_osm = folium.Map(location=[latitude, longitutbe], zoom_start=16)
map_osm.save('./xx_map2.html')

map_osm = folium.Map(location=[latitude, longitutbe], zoom_start=17)
# folium.TileLayer('OpenStreetMap').add_to(map_osm)
# folium.TileLayer('cartodb dark_matter').add_to(map_osm)
folium.TileLayer('OpenTopoMap').add_to(map_osm)
# tiles preview site : https//leaflet-extras.github.io/leaflet-providers/preview
map_osm.save('./xx_map3.html')

map_osm = folium.Map(location=[latitude, longitutbe], zoom_start=17)
folium.Marker([latitude, longitutbe], popup='서울특별시청',
              icon=folium.Icon(color='red', icon='info-sign')).add_to(map_osm)
folium.CircleMarker([37.5658859, 126.9754788], radius=150,
                    color='blue', fill_color='red',fill=False, popup='덕수궁').add_to(map_osm)
map_osm.save('./xx_map5.html')
print('file saved..')
