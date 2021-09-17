from getHolidays import get_info
from Country import country_codes
from googletrans import Translator
translator = Translator()

def messageEdit(word):
    output = ''
    mes = translator.translate(word, 'en').text
    if word.upper() in country_codes.keys():
        response = get_info(word)
        if response.get('country') and response.get('holidays'):
            holidays = set(response['holidays'])
            holidays = "', '".join(holidays)
            holidays.split("', ")
            holidays.rsplit(", '")
            output += f"{response['country']}  👉  '{holidays}'"
    elif mes.capitalize() in country_codes.values():
        for c_code in country_codes.keys():
            if mes.lower() == country_codes[c_code].lower():
                response = get_info(c_code)
        if response.get('country') and response.get('holidays'):
            holidays = set(response['holidays'])
            holidays = "', '".join(holidays)
            holidays.split("', ")
            holidays.rsplit(", '")
            output += f"{response['country']}  👉  '{holidays}'"
    else:
        output += f"Bunaqa davlat topilmadi 😔"

    if not output:
        output = f"{response['country'].capitalize()}da bugun bayram yo'q."

    return output