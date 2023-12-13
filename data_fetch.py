import requests
import pandas as pd

def fetch_data():
    url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?per_page=10000&format=json"
    response = requests.get(url)
    data = response.json()[1]

    population_data = []
    for entry in data:
        population_data.append({
            'Country': entry['country']['value'],
            'Year': entry['date'],
            'Population': entry['value']
        })

    df = pd.DataFrame(population_data)
    return df
