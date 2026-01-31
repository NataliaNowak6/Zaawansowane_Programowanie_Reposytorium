import requests
from typing import Optional, List

class Brewery:
    def __init__(
            self,
            id: str,
            name: str,
            brewery_type: str,
            street: Optional[str],
            city: str,
            state: str,
            postal_code: str,
            country: str,
            longitude: Optional[str],
            latitude: Optional[str],
            phone: Optional[str],
            website: Optional[str]
    ):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website = website

    def __str__(self) -> str:
        return (
            f"Brewery:\n"
            f" Name: {self.name}\n"
            f" Brewery Type: {self.brewery_type}\n"
            f" Address: {self.street or 'N/A'}, {self.city}, {self.state}, {self.postal_code}\n"
            f" Country: {self.country}\n"
            f" Coordinates: {self.longitude}, {self.latitude}\n"
        )