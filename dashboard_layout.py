from dash import html, dcc

def create_layout(df_population):
    layout = html.Div([
        html.H1("A Look At the World's Population", style={'color': '#008080'}),  
        html.Div([
            dcc.Dropdown(
                id='country-dropdown',
                options=[{'label': country, 'value': country} for country in df_population['Country'].unique()[49:]],
                value=['France', 'Burkina Faso', 'Brazil'],
                multi=True,
                style={'backgroundColor': 'light-blue', 'color': '#008080'}
            ),
            dcc.Graph(id='population-graph')
        ], style={'display': 'inline-block', 'width': '50%', 'color': 'white'}), 
        html.Div([
            dcc.Graph(id='population-histogram')
        ], style={'display': 'inline-block', 'width': '50%', 'color': 'white'}),  
        html.Div([
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in df_population['Year'].unique()],
                value=df_population['Year'].min(),
                clearable=False,
                style={'backgroundColor': 'light-blue', 'color': '#008080'}
            ),
            dcc.Graph(id='population-map')
        ], style={'display': 'inline-block', 'width': '50%', 'color': 'white', 'float': 'left'}),
        
       html.Div([
    dcc.Graph(id='income-graph', style={'height': '68.7vh'}),
    html.H2(id='income-graph-title')
    ], style={'display': 'inline-block', 'width': '50%', 'color': 'white', 'float': 'right', 'text-align': 'center'})
    ], style={'background-color': '#E6E6FA'})


    return layout
