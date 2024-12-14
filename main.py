# example of one call api openweathermap

import requests
import json
import matplotlib.pyplot as pplt
import pandas
import numpy as np
import math

city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19
api_key = ''
dt = 1671354770


#req = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&dt={dt}&appid={api_key}')
#txt = req.text

txt = '''{"cod":"200","message":0,"cnt":40,"list":[{"dt":1734199200,"main":{"temp":269.77,"feels_like":264.64,"temp_min":269.77,"temp_max":273.55,"pressure":994,"sea_level":994,"grnd_level":983,"humidity":98,"temp_kf":-3.78},"weather":[{"id":601,"main":"Snow","description":"snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":4.09,"deg":201,"gust":10.87},"visibility":20,"pop":1,"snow":{"3h":3.97},"sys":{"pod":"n"},"dt_txt":"2024-12-14 18:00:00"},{"dt":1734210000,"main":{"temp":270.54,"feels_like":264.98,"temp_min":270.54,"temp_max":272.08,"pressure":993,"sea_level":993,"grnd_level":980,"humidity":97,"temp_kf":-1.54},"weather":[{"id":601,"main":"Snow","description":"snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":4.98,"deg":199,"gust":11.76},"visibility":216,"pop":1,"snow":{"3h":2.81},"sys":{"pod":"n"},"dt_txt":"2024-12-14 21:00:00"},{"dt":1734220800,"main":{"temp":270.67,"feels_like":265.35,"temp_min":270.67,"temp_max":271.12,"pressure":990,"sea_level":990,"grnd_level":978,"humidity":96,"temp_kf":-0.45},"weather":[{"id":601,"main":"Snow","description":"snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":4.66,"deg":195,"gust":11.81},"visibility":197,"pop":1,"snow":{"3h":1.52},"sys":{"pod":"n"},"dt_txt":"2024-12-15 00:00:00"},{"dt":1734231600,"main":{"temp":271,"feels_like":266.59,"temp_min":271,"temp_max":271,"pressure":987,"sea_level":987,"grnd_level":976,"humidity":97,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":3.54,"deg":192,"gust":10.01},"visibility":151,"pop":1,"snow":{"3h":1.44},"sys":{"pod":"n"},"dt_txt":"2024-12-15 03:00:00"},{"dt":1734242400,"main":{"temp":271.74,"feels_like":268.64,"temp_min":271.74,"temp_max":271.74,"pressure":987,"sea_level":987,"grnd_level":976,"humidity":96,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":2.34,"deg":209,"gust":7.23},"visibility":3841,"pop":1,"snow":{"3h":0.97},"sys":{"pod":"n"},"dt_txt":"2024-12-15 06:00:00"},{"dt":1734253200,"main":{"temp":273.43,"feels_like":270.18,"temp_min":273.43,"temp_max":273.43,"pressure":988,"sea_level":988,"grnd_level":978,"humidity":97,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":2.79,"deg":277,"gust":6.18},"visibility":10000,"pop":0.93,"snow":{"3h":0.46},"sys":{"pod":"d"},"dt_txt":"2024-12-15 09:00:00"},{"dt":1734264000,"main":{"temp":271.29,"feels_like":267.41,"temp_min":271.29,"temp_max":271.29,"pressure":991,"sea_level":991,"grnd_level":980,"humidity":99,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":3.01,"deg":0,"gust":5.77},"pop":1,"snow":{"3h":0.56},"sys":{"pod":"d"},"dt_txt":"2024-12-15 12:00:00"},{"dt":1734274800,"main":{"temp":268.78,"feels_like":263.21,"temp_min":268.78,"temp_max":268.78,"pressure":994,"sea_level":994,"grnd_level":984,"humidity":94,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":97},"wind":{"speed":4.37,"deg":360,"gust":9.09},"visibility":10000,"pop":1,"snow":{"3h":0.45},"sys":{"pod":"n"},"dt_txt":"2024-12-15 15:00:00"},{"dt":1734285600,"main":{"temp":266,"feels_like":261.04,"temp_min":266,"temp_max":266,"pressure":997,"sea_level":997,"grnd_level":986,"humidity":96,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":91},"wind":{"speed":3.02,"deg":328,"gust":7.97},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-15 18:00:00"},{"dt":1734296400,"main":{"temp":263.2,"feels_like":259.38,"temp_min":263.2,"temp_max":263.2,"pressure":997,"sea_level":997,"grnd_level":986,"humidity":99,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":74},"wind":{"speed":1.84,"deg":290,"gust":3.35},"visibility":6370,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-15 21:00:00"},{"dt":1734307200,"main":{"temp":262.15,"feels_like":258.13,"temp_min":262.15,"temp_max":262.15,"pressure":996,"sea_level":996,"grnd_level":985,"humidity":98,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":85},"wind":{"speed":1.86,"deg":232,"gust":1.62},"visibility":6443,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-16 00:00:00"},{"dt":1734318000,"main":{"temp":264.57,"feels_like":259.13,"temp_min":264.57,"temp_max":264.57,"pressure":991,"sea_level":991,"grnd_level":980,"humidity":97,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":97},"wind":{"speed":3.19,"deg":171,"gust":9.59},"visibility":8062,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-16 03:00:00"},{"dt":1734328800,"main":{"temp":267.58,"feels_like":260.58,"temp_min":267.58,"temp_max":267.58,"pressure":983,"sea_level":983,"grnd_level":973,"humidity":95,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":98},"wind":{"speed":6.09,"deg":153,"gust":14.46},"visibility":163,"pop":1,"snow":{"3h":1.34},"sys":{"pod":"n"},"dt_txt":"2024-12-16 06:00:00"},{"dt":1734339600,"main":{"temp":269.47,"feels_like":262.9,"temp_min":269.47,"temp_max":269.47,"pressure":977,"sea_level":977,"grnd_level":966,"humidity":95,"temp_kf":0},"weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":6.23,"deg":170,"gust":14.78},"visibility":146,"pop":1,"snow":{"3h":4.43},"sys":{"pod":"d"},"dt_txt":"2024-12-16 09:00:00"},{"dt":1734350400,"main":{"temp":273.97,"feels_like":267.31,"temp_min":273.97,"temp_max":273.97,"pressure":976,"sea_level":976,"grnd_level":965,"humidity":85,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":9.65,"deg":296,"gust":16.32},"visibility":10000,"pop":1,"snow":{"3h":0.97},"sys":{"pod":"d"},"dt_txt":"2024-12-16 12:00:00"},{"dt":1734361200,"main":{"temp":272.16,"feels_like":265.55,"temp_min":272.16,"temp_max":272.16,"pressure":981,"sea_level":981,"grnd_level":970,"humidity":82,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":98},"wind":{"speed":7.98,"deg":295,"gust":14.92},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-16 15:00:00"},{"dt":1734372000,"main":{"temp":272.89,"feels_like":267.03,"temp_min":272.89,"temp_max":272.89,"pressure":982,"sea_level":982,"grnd_level":971,"humidity":97,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":99},"wind":{"speed":6.72,"deg":291,"gust":14.86},"pop":1,"snow":{"3h":0.83},"sys":{"pod":"n"},"dt_txt":"2024-12-16 18:00:00"},{"dt":1734382800,"main":{"temp":272.75,"feels_like":266.54,"temp_min":272.75,"temp_max":272.75,"pressure":984,"sea_level":984,"grnd_level":974,"humidity":92,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":7.41,"deg":296,"gust":14.03},"visibility":3222,"pop":1,"snow":{"3h":0.91},"sys":{"pod":"n"},"dt_txt":"2024-12-16 21:00:00"},{"dt":1734393600,"main":{"temp":272.32,"feels_like":266.6,"temp_min":272.32,"temp_max":272.32,"pressure":986,"sea_level":986,"grnd_level":975,"humidity":95,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":6.1,"deg":293,"gust":13.06},"pop":1,"snow":{"3h":0.85},"sys":{"pod":"n"},"dt_txt":"2024-12-17 00:00:00"},{"dt":1734404400,"main":{"temp":271.65,"feels_like":267.21,"temp_min":271.65,"temp_max":271.65,"pressure":986,"sea_level":986,"grnd_level":976,"humidity":86,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":97},"wind":{"speed":3.75,"deg":287,"gust":9.84},"visibility":10000,"pop":1,"snow":{"3h":0.53},"sys":{"pod":"n"},"dt_txt":"2024-12-17 03:00:00"},{"dt":1734415200,"main":{"temp":270.08,"feels_like":266.66,"temp_min":270.08,"temp_max":270.08,"pressure":986,"sea_level":986,"grnd_level":976,"humidity":97,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":97},"wind":{"speed":2.36,"deg":239,"gust":6.41},"pop":0.5,"sys":{"pod":"n"},"dt_txt":"2024-12-17 06:00:00"},{"dt":1734426000,"main":{"temp":271.5,"feels_like":269.11,"temp_min":271.5,"temp_max":271.5,"pressure":987,"sea_level":987,"grnd_level":977,"humidity":98,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":1.76,"deg":343,"gust":4.38},"visibility":1354,"pop":0.86,"snow":{"3h":0.49},"sys":{"pod":"d"},"dt_txt":"2024-12-17 09:00:00"},{"dt":1734436800,"main":{"temp":268.73,"feels_like":263.6,"temp_min":268.73,"temp_max":268.73,"pressure":991,"sea_level":991,"grnd_level":981,"humidity":96,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"}],"clouds":{"all":97},"wind":{"speed":3.8,"deg":336,"gust":8.92},"pop":0.58,"snow":{"3h":0.2},"sys":{"pod":"d"},"dt_txt":"2024-12-17 12:00:00"},{"dt":1734447600,"main":{"temp":266.69,"feels_like":260.67,"temp_min":266.69,"temp_max":266.69,"pressure":997,"sea_level":997,"grnd_level":986,"humidity":92,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":99},"wind":{"speed":4.31,"deg":327,"gust":9.37},"visibility":10000,"pop":0.2,"snow":{"3h":0.19},"sys":{"pod":"n"},"dt_txt":"2024-12-17 15:00:00"},{"dt":1734458400,"main":{"temp":262.01,"feels_like":256.96,"temp_min":262.01,"temp_max":262.01,"pressure":1000,"sea_level":1000,"grnd_level":989,"humidity":94,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":76},"wind":{"speed":2.48,"deg":299,"gust":6.81},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-17 18:00:00"},{"dt":1734469200,"main":{"temp":259.56,"feels_like":255.23,"temp_min":259.56,"temp_max":259.56,"pressure":1002,"sea_level":1002,"grnd_level":990,"humidity":99,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":23},"wind":{"speed":1.81,"deg":253,"gust":1.49},"visibility":4445,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-17 21:00:00"},{"dt":1734480000,"main":{"temp":264.86,"feels_like":262.07,"temp_min":264.86,"temp_max":264.86,"pressure":1001,"sea_level":1001,"grnd_level":990,"humidity":96,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":56},"wind":{"speed":1.44,"deg":235,"gust":2.62},"visibility":324,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-18 00:00:00"},{"dt":1734490800,"main":{"temp":265.46,"feels_like":265.46,"temp_min":265.46,"temp_max":265.46,"pressure":1002,"sea_level":1002,"grnd_level":991,"humidity":98,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":1.33,"deg":340,"gust":0.99},"visibility":731,"pop":1,"snow":{"3h":0.38},"sys":{"pod":"n"},"dt_txt":"2024-12-18 03:00:00"},{"dt":1734501600,"main":{"temp":266.05,"feels_like":259.05,"temp_min":266.05,"temp_max":266.05,"pressure":1006,"sea_level":1006,"grnd_level":995,"humidity":91,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":5.99,"deg":328,"gust":11.99},"pop":1,"snow":{"3h":0.45},"sys":{"pod":"n"},"dt_txt":"2024-12-18 06:00:00"},{"dt":1734512400,"main":{"temp":265.17,"feels_like":258.28,"temp_min":265.17,"temp_max":265.17,"pressure":1009,"sea_level":1009,"grnd_level":998,"humidity":83,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"clouds":{"all":94},"wind":{"speed":4.96,"deg":331,"gust":10.96},"visibility":10000,"pop":0,"sys":{"pod":"d"},"dt_txt":"2024-12-18 09:00:00"},{"dt":1734523200,"main":{"temp":262.95,"feels_like":257.71,"temp_min":262.95,"temp_max":262.95,"pressure":1011,"sea_level":1011,"grnd_level":1000,"humidity":89,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":2.75,"deg":307,"gust":6.68},"visibility":10000,"pop":0,"sys":{"pod":"d"},"dt_txt":"2024-12-18 12:00:00"},{"dt":1734534000,"main":{"temp":256.69,"feels_like":252.8,"temp_min":256.69,"temp_max":256.69,"pressure":1012,"sea_level":1012,"grnd_level":1001,"humidity":98,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"few clouds","icon":"02n"}],"clouds":{"all":12},"wind":{"speed":1.43,"deg":272,"gust":1.22},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-18 15:00:00"},{"dt":1734544800,"main":{"temp":257.53,"feels_like":253.76,"temp_min":257.53,"temp_max":257.53,"pressure":1012,"sea_level":1012,"grnd_level":1000,"humidity":97,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"clouds":{"all":56},"wind":{"speed":1.43,"deg":224,"gust":1.26},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-18 18:00:00"},{"dt":1734555600,"main":{"temp":260.47,"feels_like":255.65,"temp_min":260.47,"temp_max":260.47,"pressure":1011,"sea_level":1011,"grnd_level":1000,"humidity":96,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":100},"wind":{"speed":2.16,"deg":164,"gust":5.55},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-18 21:00:00"},{"dt":1734566400,"main":{"temp":262.81,"feels_like":256.28,"temp_min":262.81,"temp_max":262.81,"pressure":1008,"sea_level":1008,"grnd_level":997,"humidity":94,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":100},"wind":{"speed":3.88,"deg":150,"gust":10.82},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-19 00:00:00"},{"dt":1734577200,"main":{"temp":264.66,"feels_like":257.66,"temp_min":264.66,"temp_max":264.66,"pressure":1004,"sea_level":1004,"grnd_level":993,"humidity":93,"temp_kf":0},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],"clouds":{"all":99},"wind":{"speed":5.11,"deg":142,"gust":13.5},"visibility":10000,"pop":0,"sys":{"pod":"n"},"dt_txt":"2024-12-19 03:00:00"},{"dt":1734588000,"main":{"temp":266.45,"feels_like":259.45,"temp_min":266.45,"temp_max":266.45,"pressure":999,"sea_level":999,"grnd_level":988,"humidity":94,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13n"}],"clouds":{"all":100},"wind":{"speed":6.74,"deg":150,"gust":17.29},"visibility":180,"pop":0.2,"snow":{"3h":0.31},"sys":{"pod":"n"},"dt_txt":"2024-12-19 06:00:00"},{"dt":1734598800,"main":{"temp":268.54,"feels_like":261.54,"temp_min":268.54,"temp_max":268.54,"pressure":995,"sea_level":995,"grnd_level":984,"humidity":92,"temp_kf":0},"weather":[{"id":601,"main":"Snow","description":"snow","icon":"13d"},{"id":613,"main":"Snow","description":"shower sleet","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":7.11,"deg":165,"gust":15.74},"visibility":2448,"pop":1,"snow":{"3h":2.1},"sys":{"pod":"d"},"dt_txt":"2024-12-19 09:00:00"},{"dt":1734609600,"main":{"temp":271.31,"feels_like":265.35,"temp_min":271.31,"temp_max":271.31,"pressure":991,"sea_level":991,"grnd_level":980,"humidity":96,"temp_kf":0},"weather":[{"id":600,"main":"Snow","description":"light snow","icon":"13d"},{"id":511,"main":"Rain","description":"freezing rain","icon":"13d"}],"clouds":{"all":100},"wind":{"speed":6.02,"deg":177,"gust":15.25},"visibility":2868,"pop":1,"snow":{"3h":0.6},"sys":{"pod":"d"},"dt_txt":"2024-12-19 12:00:00"},{"dt":1734620400,"main":{"temp":274.67,"feels_like":269.69,"temp_min":274.67,"temp_max":274.67,"pressure":987,"sea_level":987,"grnd_level":977,"humidity":100,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"light rain","icon":"10n"}],"clouds":{"all":100},"wind":{"speed":5.88,"deg":179,"gust":15.75},"visibility":90,"pop":1,"rain":{"3h":0.63},"sys":{"pod":"n"},"dt_txt":"2024-12-19 15:00:00"}],"city":{"id":512047,"name":"Pavlovskaya","coord":{"lat":59.57,"lon":30.19},"country":"RU","population":0,"timezone":10800,"sunrise":1734159101,"sunset":1734180991}}'''

req_obj = json.loads(txt)  # Преобразуем объект типа Request в json-формат

#req_obj = json.loads(string1.replace("'",'"'))

print(req_obj)
v = []
for i in req_obj['list']:
    #print(i)
    v.append([i['dt'], i['dt_txt'].replace(':00:00', 'ч'), i['main']['temp']-273.15])

for i in v:
    print(i)



def visualise_data(json_data=''):

    if json_data:
        ax = pplt.axes()
        pos = ax.get_position()
        pos.y0 = 0.2
        ax.set_position(pos)

        # получим отдельные столбцы с датами
        dates = [_d[1] for _d in json_data]
        print(dates)
        # и тепературами
        temps = [_d[2] for _d in json_data]

        # построим их на диаграмме рассеяния

        pplt.scatter(dates, temps)
        pplt.title("Прогноз погоды СПБ")
        pplt.xlabel("Дата-время")
        pplt.ylabel("Температура")
        pplt.yticks(np.arange(math.floor(min(temps)-1), math.floor(max(temps)+1), 1))
        pplt.xticks(np.arange(len(dates)), dates,
       rotation =80)



        bdata = []
        data = []
        days = []
        lst = 0
        for i in range(len(temps)):
            now = dates[i][8:10]

            if lst != now:
                bdata.append(data)
                days.append(str(lst))
                data = []
                lst = now
            data.append(temps[i])
        print(days)
        days.append(dates[len(dates)-1][8:10])
        bdata.append(data)



        pplt.show()


        fig = pplt.figure(figsize=(10, 7))

        # Creating axes instance
        fig, ax = pplt.subplots()
        ax.set_ylabel('Разброс температуры')
        ax.set_xlabel('Дата')

        print(bdata)

        # Creating plot
        bp = ax.boxplot(bdata, patch_artist=True, tick_labels=list(days))



        pplt.show()

        # построенный график необходимо оптимизировать:
        ' - добавить название'
        '  - правильно расположить ось абсцисс ?'
        ' - упростить вывод дат (на этом графике они выводятся в формате unixtime)'
        ' - вывести более строгие значения для подписей осей абсцисс и ординат' #?
        '(xticks, yticks)'
        'добавить на график температуры остальных дат'
        ' - добавить второй график с box plot'

visualise_data(v)