import requests
from Country import country_codes
from datetime import datetime as dt

from googletrans import Translator
trans = Translator()

def get_info(country_code):
    now = dt.now()
    day = now.day
    month = now.month
    output = {}
    holidays = []
    country_code = country_code.upper()
    country = country_codes[country_code]
    country = trans.translate(country, 'uz').text
    url = f"https://holidays.abstractapi.com/v1/?api_key=adb91123aeb44beaa2f5c6d3f16e1fc2&country={country_code}&month={month}&day={day}"
    r = requests.get(url)
    res = r.json()
    if r.status_code == 200 and res:
        for i in range(len(res)):
            holiday = res[i]['name']
            if holiday not in holidays:
                holidays.append(trans.translate(holiday, 'uz').text)
    output['country'] = country
    output['holidays'] = holidays
    return output

if __name__ == '__main__':
    print(get_info('an'))
    print(get_info('uz'))
    print(get_info('us'))
    print(get_info('ua'))