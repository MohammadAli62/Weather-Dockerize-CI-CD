import requests
import pandas as pd

# Koordinater för städer
städer = {
    "stockholm": {"latitude": "59.30", "longitude": "18.02"},
    "göteborg": {"latitude": "57.70", "longitude": "11.97"},
    "malmö": {"latitude": "55.60", "longitude": "13.00"}  # korrigerad Malmö
}

def hämta_väderdata(stad: str) -> dict:
    """
    Hämtar väderdata från SMHI API för en given stad.
    """
    if stad not in städer:
        raise ValueError(f"Stad '{stad}' finns inte i listan.")

    lat = städer[stad]["latitude"]
    lon = städer[stad]["longitude"]

    url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{lon}/lat/{lat}/data.json"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Fel om något går fel

    return response.json()


def skapa_dataframe(stad: str) -> pd.DataFrame:
    """
    Skapar en pandas DataFrame med temperaturdata för de första 24 timmarna.
    """
    data = hämta_väderdata(stad)

    tider = []
    grader = []

    for tidpunkt in data.get("timeSeries", []):
        for parameter in tidpunkt.get("parameters", []):
            if parameter.get("name") == "t":  # temperaturparameter
                tider.append(tidpunkt.get("validTime"))
                grader.append(parameter.get("values", [None])[0])

    df = pd.DataFrame({
        "tid": tider[:24],
        "grad": grader[:24]
    })

    return df


if __name__ == "__main__":
    # Exempel: Hämta väder för Göteborg
    stad_namn = "göteborg"
    df = skapa_dataframe(stad_namn)
    print(df)
