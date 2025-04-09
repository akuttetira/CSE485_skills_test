import requests

def get_cities(coordinates, username):
    lat = float(coordinates[0])
    lng = float(coordinates[1])

    north = lat + 2
    south = lat - 2
    west = lng - 2
    east = lng + 2

    url = f"http://api.geonames.org/citiesJSON?north={north}&south={south}&east={east}&west={west}&lang=de&username=akuttetira"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        geonames = data.get("geonames", [])

        i = 0
        cities = []
        for city in geonames:
            cities.append(city["name"])
        return cities

    return []

def get_coordinates(city, username):
    url = f"http://api.geonames.org/searchJSON?name_startsWith={city}&username=akuttetira"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        cities = data.get("geonames", [])
        print(cities[0]["lat"] + cities[0]["lng"])
        return (cities[0]["lat"], cities[0]["lng"])

if __name__ == "__main__":
    name = input("What is your name? ")
    city = input("Enter a city name: ")
    username = "akuttetira"  # Replace with your GeoNames username

    coordinates = get_coordinates(city, username)
    cities = get_cities(coordinates, username)

    for i, city_name in enumerate(cities, 1):
            print(f"{i}. {city_name}")

