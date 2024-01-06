import requests
import pandas as pd

def fetch_data():

    """
    Récupère les données de population depuis l'API de la Banque mondiale.

    Returns:
    pandas.DataFrame: Un DataFrame contenant les données de population avec les colonnes 'Country', 'Year' et 'Population'.
    
    """

    url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?per_page=18000&format=json"
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

def fetch_data2():

    """
    Récupère les données de revenu depuis l'API de la Banque mondiale.

    Returns:
    pandas.DataFrame: Un DataFrame contenant les données de revenu avec les colonnes 'country' et 'income'.

    """
    
    url = "https://api.worldbank.org/v2/country?per_page=297&format=json"
    response = requests.get(url)
    data = response.json()[1]

    population_data2 = []
    for entry in data:
        population_data2.append({
            'country': entry['name'],
            'income': entry['incomeLevel']['value'],
        })

    df = pd.DataFrame(population_data2)
    return df