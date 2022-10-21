import os.path
import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc, html
from dash.dependencies import Input, Output, State
from flask import Flask
import git


server = Flask(__name__)


external_stylesheets =['https://www.w3schools.com/w3css/4/w3.css', dbc.themes.BOOTSTRAP]
app = dash.Dash(server=server, external_stylesheets=external_stylesheets)

@server.route('/git-update', methods=['POST'])
def git_update():
  repo = git.Repo('./pyanywhere')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()                                
  origin.pull()
  return '', 200

nav_contents = [
    dbc.NavItem(dbc.NavLink("Active", href="#", active=True)),
    dbc.NavItem(dbc.NavLink("A much longer link label", href="#")),
    dbc.NavItem(dbc.NavLink("Link", href="#")),
]

nav1 = dbc.Nav(nav_contents, pills=True, fill=True)

nav2 = dbc.Nav(nav_contents, pills=True, justified=True)

navs = html.Div([nav1, html.Hr(), nav2])


app.layout = html.Div([
    dcc.Input(id='mbid', value='Fruits-per-City1.csv', type="text"),
    dcc.Input(id='username', value='t', type='text'),

    html.Button('Click Me', id='button'),
    html.Div(id='my-div')
])


@app.callback(
    Output('my-div', 'children'),
    [Input('button', 'n_clicks')],
    [State('mbid', 'value'),
        State('username', 'value')]
)



def update_output_div(n_clicks, mbid, username): 
    if os.path.exists(mbid)==True:
        df = pd.read_csv(mbid)

        fig1 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
        fig2 = px.line(df, x="Fruit", y="Amount", color="City")
        
        graph_website = html.Div(children=[
            html.H1(children='Hello Dash'),

            html.Div(children='''
                Dashyyyyyyy: A web application framework for your data.
            '''),

            dcc.Graph(
                id='example-graph',
                figure=fig1
            ),

            html.Div(children='''
                Dash: A web application framework for your data.
            '''),

            dcc.Graph(
                id='example-graph',
                figure=fig2
            )
        ])

        return graph_website
    return 'You! have entered "{}" and "{}" and clicked {} times. Please provide valid information'.format(mbid, username, n_clicks)



    




if __name__ == '__main__':
    app.run_server()
