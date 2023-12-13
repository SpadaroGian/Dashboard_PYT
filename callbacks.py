from dash.dependencies import Input, Output
import plotly.express as px

def update_graph(df, selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.line(filtered_df, x='Year', y='Population', title=f'Population Trend for {selected_country}')
    fig.update_xaxes(categoryorder='category ascending')
    return fig

def update_histogram(df, selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.histogram(filtered_df, x='Year', y='Population', title=f'Population Distribution for {selected_country}')
    fig.update_xaxes(categoryorder='category ascending')
    return fig

def register_callbacks(app, df):
    @app.callback(
        Output('population-graph', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_graph_callback(selected_country):
        return update_graph(df, selected_country)

    @app.callback(
        Output('population-histogram', 'figure'),
        [Input('country-dropdown', 'value')]
    )
    def update_histogram_callback(selected_country):
        return update_histogram(df, selected_country)
