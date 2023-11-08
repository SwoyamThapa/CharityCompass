from organization_data import get_updated_data
import plotly.express as px
import plotly.io as pio
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

def individual_fig_creator():
    data = get_updated_data()

    fig = []

    for items in data:
        item = [items] 
        df = pd.DataFrame(item)

        _fig1 = px.bar(df, x='name', y=['goal', 'funding'], title='Project Funding vs. Goal',
                labels={'title': 'Organization', 'value': 'Amount'},
                barmode='group') 

        _fig2 = px.bar(df, x='name', y=['totalProjects', 'activeProjects'], title='Total Projects and Active Projects',
                labels={'title': 'Organization', 'value': 'No. of Projects'},
                barmode='group') 
            
        fig.append(_fig1)
        fig.append(_fig2)

    
    return fig


figs = individual_fig_creator()


app = dash.Dash(__name__)

layout = html.Div([html.Div(dcc.Graph(figure=fig)) for fig in figs])

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)
        