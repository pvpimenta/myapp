from dash import Dash,html, dcc
import plotly.express as px
import pandas as pd



app=Dash(__name__)
server=app.server
colors={'background':'#050506',
        'text':'#ebebf0'
        }

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig=px.bar(df,x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


app.layout=html.Div(style={'backgroundColor':colors['background']},children=[
    html.H1(children='Hello Dash', style={'textAlign':'center','color':colors['text']}),
    html.Div(children='''
                 Dash: A web application framework for your data.
    ''',style={'textAlign':'center','color':colors['text']}),
    dcc.Graph(id='Graph', figure=fig)
])

app.run(debug=True)
