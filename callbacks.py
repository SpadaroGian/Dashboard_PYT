from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objs as go

# Update the graph style for line plot
def update_graph(df, selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    fig = px.line(filtered_df, x='Year', y='Population', color='Country',
                  title='Population for Selected Countries')
    fig.update_xaxes(categoryorder='category ascending')
    fig.update_layout(
        plot_bgcolor='#E6E6FA',  # Background color
        paper_bgcolor='#E6E6FA',  # Background color
        font=dict(color='#008080')  # Text color
    )
    return fig

# Update the histogram style
def update_histogram(df, selected_countries):
    filtered_df = df[df['Country'].isin(selected_countries)]
    fig = px.histogram(filtered_df, x='Year', y='Population', title=f'The Addition of Population per country: {selected_countries}')
    fig.update_xaxes(categoryorder='category ascending')
    fig.update_layout(
        plot_bgcolor='#E6E6FA',  # Background color
        paper_bgcolor='#E6E6FA',  # Background color
        font=dict(color='#008080')  # Text color
    )
    return fig

# Update the map style
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
                marker_line_color='#008080',
                showscale=False,
            ))

    fig.update_layout(
        title_text=f'A Geographical Map Showing The Population in {selected_year} on The Selected Countries',
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        plot_bgcolor='#E6E6FA',  # Background color
        paper_bgcolor='#E6E6FA',  # Background color
        font=dict(color='#008080')  # Text color
    )

    return fig

# Registering the updated callbacks
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
