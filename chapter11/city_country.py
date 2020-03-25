def print_city_country(city, country, population=''):
    if population:
        city_country = city.format() + ',' + country.format + ',' + population
    else:
        city_country = city.format() + ',' + country.format
    return city_country.title()
