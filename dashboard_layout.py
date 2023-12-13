from dash import html, dcc

def create_layout(df):
    layout = html.Div([
        html.H1("World Population Dashboard"),
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['Country'].unique()],
                value=['Afghanistan'],  # Set default selected countries here
                multi=True  # Allow multiple selection
            ),
            dcc.Graph(id='population-graph')
        ], style={'display': 'inline-block', 'width': '50%'}),
        html.Div([
            dcc.Graph(id='population-histogram')
        ], style={'display': 'inline-block', 'width': '50%'}),
        html.Div([
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in df['Year'].unique()],
                value=df['Year'].min(),  # Set default year here
                clearable=False
            ),
            dcc.Graph(id='population-map')
        ])
    ])
    return layout
