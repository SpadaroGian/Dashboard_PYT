from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objs as go
import random  
from dash import no_update

def update_graph(df, selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    fig = px.line(filtered_df, x='Year', y='Population', color='Country',
                  title='Population Trends for Selected Countries')
    fig.update_xaxes(categoryorder='category ascending') 
    return fig

def update_histogram(df, selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    fig = px.histogram(filtered_df, x='Year', y='Population', title=f'Population Distribution for {selected_countries}')
    fig.update_xaxes(categoryorder='category ascending')
    return fig

def update_map(df, selected_year, selected_countries):
    filtered_df = df[(df['Country'].isin(selected_countries)) & (df['Year'] == selected_year)]
    
    fig = go.Figure()

    for country in selected_countries:
        country_data = filtered_df[filtered_df['Country'] == country]
        if not country_data.empty:
            fig.add_trace(go.Choropleth(
                locations=[country_data.iloc[0]['Country']],
                z=[country_data.iloc[0]['Population']],
                locationmode='country names',
                colorscale='Viridis',
                marker_line_color='white',
                showscale=False, 
            ))

    fig.update_layout(
        title_text=f'Population by Country for the Selected Year ({selected_year})',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        )
    )

    return fig

def register_callbacks(app, df):
    @app.callback(
        Output('country-dropdown', 'value'),
        Input('interval-component', 'n_intervals'),
        State('manual-selection-flag', 'children')
    )
    def update_country_dropdown(n, manual_flag):
        if manual_flag == 'manual':
            # If manual selection was made, don't change the dropdown value
            return no_update

        selected_countries = df['Country'].unique().tolist()
        # Select only 5 random countries
        random_countries = random.sample(selected_countries, k=min(5, len(selected_countries)))
        return random_countries

    @app.callback(
        Output('population-graph', 'figure'),
        Input('country-dropdown', 'value')
    )
    def update_graph_callback(selected_countries):
        return update_graph(df, selected_countries)
    
    @app.callback(
        Output('population-histogram', 'figure'),
        Input('country-dropdown', 'value')
    )
    def update_histogram_callback(selected_countries):
        return update_histogram(df, selected_countries)
    
    @app.callback(
        Output('population-map', 'figure'),
        Input('year-dropdown', 'value'),
        Input('country-dropdown', 'value')
    )
    def update_map_callback(selected_year, selected_countries):
        return update_map(df, selected_year, selected_countries)
