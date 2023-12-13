import dash
from dashboard_layout import create_layout
from callbacks import register_callbacks
from data_fetch import fetch_data

app = dash.Dash(__name__)

# Fetching data
df = fetch_data()

# Creating layout
app.layout = create_layout(df)

# Registering callbacks
register_callbacks(app, df)

if __name__ == '__main__':
    app.run_server(debug=True)
