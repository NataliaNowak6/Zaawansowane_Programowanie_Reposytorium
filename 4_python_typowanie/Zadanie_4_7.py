# Stworzyć skrypt pythonowy, który połączy się z API, które zawiera informacje o browarach (dokumentacja https://www.openbrewerydb.org/documentation).

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
        website_url: Optional[str],
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
        self.website_url = website_url

    def __str__(self) -> str:
        return (
            f"Brewery:\n"
            f"  ID: {self.id}\n"
            f"  Name: {self.name}\n"
            f"  Type: {self.brewery_type}\n"
            f"  Address: {self.street or 'N/A'}, {self.city}, {self.state}, {self.postal_code}\n"
            f"  Country: {self.country}\n"
            f"  Coordinates: ({self.latitude}, {self.longitude})\n"
            f"  Phone: {self.phone or 'N/A'}\n"
            f"  Website: {self.website_url or 'N/A'}\n"
        )


def fetch_breweries(limit: int = 20) -> List[Brewery]:
    url = "https://api.openbrewerydb.org/v1/breweries"
    response = requests.get(url, params={"per_page": limit})
    response.raise_for_status()

    breweries_data = response.json()
    breweries: List[Brewery] = []

    for item in breweries_data:
        brewery = Brewery(
            id=item["id"],
            name=item["name"],
            brewery_type=item["brewery_type"],
            street=item.get("street"),
            city=item["city"],
            state=item["state"],
            postal_code=item["postal_code"],
            country=item["country"],
            longitude=item.get("longitude"),
            latitude=item.get("latitude"),
            phone=item.get("phone"),
            website_url=item.get("website_url"),
        )
        breweries.append(brewery)

    return breweries


def main():
    breweries = fetch_breweries(20)

    for brewery in breweries:
        print(brewery)
        print("-" * 50)


if __name__ == "__main__":
    main()
