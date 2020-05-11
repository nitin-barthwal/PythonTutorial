'''
dash==1.9.1
dash-core-components==1.8.1
dash-html-components==1.0.2
'''

'''
Download and install libraries

pip install dash
pip install dash-core-components
pip install dash-html-components
'''
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

app =dash.Dash(__name__)

df = pd.read_csv('generated_data.csv')

app.layout = html.Div(
    [
        html.H1(' Dash App1'),
        html.Div ([
            dcc.Graph(id='graph1',
            style={},
            figure={
                'data':[ {'x' : df['Date'],'y':df['A']} ],
                'layout':{
                    'title' : 'Title of the Graph',
                    'xaxis': {'title': 'X-axis'},
                    'yaxis': {'title': 'Y-axis'},
                    'paper_bgcolor':'lightblue',
                    'plot_bgcolor':'lightgrey',
                    
                }
            }
            )
        ]

        )
    ]
)

if __name__ == '__main__':
    app.run_server( port = 8056,debug= True )

