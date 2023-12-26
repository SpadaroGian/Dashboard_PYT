from dash import html, dcc

def create_layout(df):
    layout = html.Div([
        html.H1("A Look At The World's Population", style={'color': '#008080'}),  # Set text color to white
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['Country'].unique()],
                value=['France','Venezuela, RB','Italy'],  # Default country 
                multi=True,  # Allow multiple selection
                style={'backgroundColor': 'light-blue', 'color': '#008080'}
            ),
            dcc.Graph(id='population-graph')
        ], style={'display': 'inline-block', 'width': '50%', 'color': 'white'}),  # Set text color to white
        html.Div([
            dcc.Graph(id='population-histogram')
        ], style={'display': 'inline-block', 'width': '50%', 'color': 'white'}),  # Set text color to white
        html.Div([
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in df['Year'].unique()],
                value=df['Year'].min(),  # Default year 
                clearable=False,
                style={'backgroundColor': 'light-blue', 'color': '#008080'}
            ),
            dcc.Graph(id='population-map')
        ], style={'color': 'white'})  # Set text color to white
    ], style={'background-color': '#E6E6FA'})  # Set background color to black

    return layout
