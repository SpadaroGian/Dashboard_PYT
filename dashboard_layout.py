from dash import html, dcc

def create_layout(df):
    layout = html.Div([
        html.H1("World Population Dashboard"),
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['Country'].unique()],
                value='Africa Eastern and Southern'
            ),
            dcc.Graph(id='population-graph')
        ], style={'display': 'inline-block', 'width': '70%'}),
        html.Div([
            dcc.Graph(id='population-histogram')
        ], style={'display': 'inline-block', 'width': '30%'}),
    ])
    return layout
