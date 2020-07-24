import config
import os
import time
from google_images_search import GoogleImagesSearch

#Config.py:
#api_key = XXXXXXXX
#cx = NNNNNNN

def fetch_images(countries):

    if not os.path.exists('data'):
        os.makedirs('data')

    os.chdir('./data')
    data_path = os.getcwd()
    print(data_path)

    gis = GoogleImagesSearch(config.api_key, config.cx)
    for country in countries:
        _search_params = {
            'q': country + ' food',
            'num': 2
        }
        if not os.path.exists(country):
            os.makedirs(country)
        elif len([name for name in os.listdir('./'+country) if os.path.isfile(name)]) >= 10:
            print(country, 'maxed images')
            continue

        os.chdir('./'+country)
        temp_path = os.getcwd()

        gis.search(search_params=_search_params, path_to_dir=temp_path)

        os.chdir('..')
        time.sleep(0.3)

if __name__=='__main__':
    fetch_images(['jamaica','thailand'])
