from dash import html, dcc

def create_layout(df):
    layout = html.Div([
        html.H1("World Population Dashboard"),
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df['Country'].unique()],
                value=['France'],  # Default country 
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
                value=df['Year'].min(),  # Default year 
                clearable=False
            ),
            dcc.Graph(id='population-map')
        ]),
        dcc.Interval(
            id='interval-component',
            interval=2*1000,  # in milliseconds
            n_intervals=0
        ),
        html.Div(id='manual-selection-flag', style={'display': 'none'})  # Hidden div for manual selection flag
    ])

    return layout
