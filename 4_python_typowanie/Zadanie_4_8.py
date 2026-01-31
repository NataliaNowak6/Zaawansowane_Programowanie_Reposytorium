# Rozszerzyć skrypt z punktu 7 o przyjmowanie parametru city , który może być przekazywany w wierszu poleceń podczas wykonywania (np. python main.py --city=Berlin ).
# Należy wykorzystać moduł argparse do wczytywania przekazywanych parametrów, a w razie przekazania wartości ograniczyć pobierane browary do miasta, które zostało wskazane.

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Any, List, Optional

import requests

API_URL = "https://api.openbrewerydb.org/v1/breweries"


@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: Optional[str]
    postal_code: str
    country: str
    longitude: Optional[str]
    latitude: Optional[str]
    phone: Optional[str]
    website_url: Optional[str]
    state: Optional[str]
    street: Optional[str]

    def __str__(self) -> str:
        parts = [
            f"Nazwa: {self.name}",
            f"Typ: {self.brewery_type}",
            f"Miasto: {self.city}",
            f"Kraj: {self.country}",
        ]
        if self.website_url:
            parts.append(f"WWW: {self.website_url}")
        if self.phone:
            parts.append(f"Tel: {self.phone}")
        return " | ".join(parts)

    @staticmethod
    def from_api(data: dict[str, Any]) -> "Brewery":
        return Brewery(
            id=str(data.get("id", "")),
            name=str(data.get("name", "")),
            brewery_type=str(data.get("brewery_type", "")),
            address_1=data.get("address_1"),
            address_2=data.get("address_2"),
            address_3=data.get("address_3"),
            city=str(data.get("city", "")),
            state_province=data.get("state_province"),
            postal_code=str(data.get("postal_code", "")),
            country=str(data.get("country", "")),
            longitude=data.get("longitude"),
            latitude=data.get("latitude"),
            phone=data.get("phone"),
            website_url=data.get("website_url"),
            state=data.get("state"),
            street=data.get("street"),
        )


def fetch_breweries(per_page: int = 20, city: Optional[str] = None) -> List[Brewery]:
    params: dict[str, Any] = {"per_page": per_page}
    if city:
        params["by_city"] = city  # OpenBreweryDB: filter po mieście

    resp = requests.get(API_URL, params=params, timeout=20)
    resp.raise_for_status()

    data = resp.json()
    if not isinstance(data, list):
        raise ValueError("API zwróciło nieoczekiwany format danych (oczekiwano listy).")

    return [Brewery.from_api(item) for item in data][:per_page]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Pobiera browary z OpenBreweryDB.")
    parser.add_argument(
        "--city", type=str, default=None, help="Filtr po mieście, np. Berlin"
    )
    return parser.parse_known_args()[0]


if __name__ == "__main__":
    args = parse_args()
    breweries = fetch_breweries(per_page=20, city=args.city)

    for b in breweries:
        print(b)
