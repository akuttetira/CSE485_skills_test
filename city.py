class City:
    def __init__(self, name, country, population, latitude, longitude, geoname_id=None):
        self.name = name
        self.country = country
        self.population = population
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.geoname_id = geoname_id

    def __repr__(self):
        return f"City(name={self.name}, country={self.country}, population={self.population}, location=({self.latitude}, {self.longitude}))"

    def to_dict(self):
        return {
            "name": self.name,
            "country": self.country,
            "population": self.population,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "geoname_id": self.geoname_id,
        }

    def summary(self):
        return f"{self.name}, {self.country} — Population: {self.population:,} — Coordinates: ({self.latitude}, {self.longitude})"

