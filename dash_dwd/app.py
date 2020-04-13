import dash
import dash_bootstrap_components as dbc


def main():
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

    app.layout = dbc.Alert("Hello, Bootstrap!", className="m-5")
