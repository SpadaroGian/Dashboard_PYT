import dash
from dashboard_layout import create_layout
from callbacks import register_callbacks
from data_fetch import fetch_data
from data_fetch import fetch_data2

"""
Point d'entrée principal de l'application Dash.

Ce script configure l'application Dash pour afficher des données de population et de revenu,
en utilisant des fonctions pour récupérer les données, créer la mise en page et enregistrer les callbacks.

"""

app = dash.Dash(__name__)

# Fetching population data
df_population = fetch_data()

# Fetching data for the income levels
df_income = fetch_data2()

# Creating layout
app.layout = create_layout(df_population)

# Registering callbacks
register_callbacks(app, df_population , df_income)

if __name__ == '__main__':
    app.run_server(debug=True)
