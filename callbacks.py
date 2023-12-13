from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

def update_graph(df, selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    fig = px.line(filtered_df, x='Year', y='Population', color='Country',
                  title='Population Trends for Selected Countries')
    return fig

def update_histogram(df, selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    fig = px.histogram(filtered_df, x='Population', color='Country',
                       title='Population Distribution for Selected Countries')
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
                name=country
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
