import requests
import googlemaps

MY_GEOTAG = ''
TIME_MAX = ''
'https://www.lun.ua/uk/%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0-%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B8%D1%80-%D0%BA%D0%B8%D1%97%D0%B2?district=1&district=5&district=6&district=7&district=8&district=9&district=10&priceMax=10000&roomCount=2'
'origins=41.43206,-81.38992|-33.86748,151.20699'
URL_FLAT = ''
URL_GT = 'https://www.lun.ua/api/v2/search_map_layers/all_realties_points_geojson'
PARAM_GT = {"district": ["1", "5", "6", "7", "8", "9", "10"], "priceMax": "10000",
            "roomCount": "2", "city": 1, "contractType": 2, "realtyType": 1}


def get_data():
    flats = requests.get(URL_FLAT)
    flats_geo = requests.post(URL_GET)


def check_repeat():
    pass


def get_direction():
    pass


def store():
    pass


def result():
    pass


if __name__ == '__main__':
    raw_data = get_data()
    new_flat = check_repeat(raw_data)
    data = get_direction(new_flat)
    store(new_flat)
    print(result(data))
