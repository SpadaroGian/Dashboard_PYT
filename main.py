import requests
import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Fetching data from the World Bank API
url = "https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?per_page=10000&format=json"
response = requests.get(url)
data = response.json()[1]

# Extracting relevant data and creating a DataFrame
population_data = []
for entry in data:
    population_data.append({
        'Country': entry['country']['value'],
        'Year': entry['date'],
        'Population': entry['value']
    })

df = pd.DataFrame(population_data)

# Dash app
app = dash.Dash(__name__)

# Layout of the dashboard
app.layout = html.Div([
    html.H1("World Population Dashboard"),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Country'].unique()],
        value='Africa Eastern and Southern'
    ),
    dcc.Graph(id='population-graph'),
])

# Callback to update the graph based on selected country
@app.callback(
    dash.dependencies.Output('population-graph', 'figure'),
    [dash.dependencies.Input('country-dropdown', 'value')]
)
def update_graph(selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.line(filtered_df, x='Year', y='Population', title=f'Population Trend for {selected_country}')
    fig.update_xaxes(categoryorder='category ascending')  # Set x-axis to display in ascending order
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
