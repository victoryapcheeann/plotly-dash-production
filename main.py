import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_extensions as de
from apps import home
import dash

app = dash.Dash(__name__, 
                title="SAT Score Analysis",
                suppress_callback_exceptions=True)
server = app.server

url = "https://assets8.lottiefiles.com/packages/lf20_2RSPTv.json"
url2 = "https://assets9.lottiefiles.com/packages/lf20_CYBIbn.json"
options_lottie = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        html.Div(de.Lottie(options=options_lottie, width="70%", height="70%", url=url), className="lottieContainer"),
        html.Div('VICTOR YAP', className='subTitle1'),
        html.Div('SAT SCORE ANALYSIS', className='subTitle2'),
        html.Div(['Dataset Source: ',
              html.A(html.Img(src=app.get_asset_url('pic/4990950.png'), className = "social_icon"), href='https://www.kaggle.com/nycopendata/high-schools', target="_blank"),
      ]),
        html.Div(['Let\'s Connect: ',
              html.A(html.Img(src=app.get_asset_url('pic/174857.png'), className = "social_icon"), href='https://www.linkedin.com/in/victor-yap-49b713b9/', target="_blank"),
      ]),
    ], className = 'nameContainer'),
    html.Div(id='page-content')
], className="mainContainer")


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/home':
        return home.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=False)