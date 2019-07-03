import requests

MY_GEOTAG = ''
TIME_MAX = ''
URL_FLAT = ''
URL_GT = ''


def get_data():
    pass


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
