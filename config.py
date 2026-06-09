import requests

NBU_API = "https://bank.gov.ua/NBUStatService/v1/statdirectory/ovdp?json"


def fetch_bonds():
    r = requests.get(NBU_API)
    data = r.json()

    bonds = []

    for item in data:
        bonds.append({
            "id": item.get("id", item.get("cc", "")),
            "name": item.get("txt"),
            "yield": 0,
            "maturity": item.get("exchangedate")
        })

    return bonds
