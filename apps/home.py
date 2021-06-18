import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_extensions as de
px.set_mapbox_access_token('pk.eyJ1IjoidmljdG9yeWFwIiwiYSI6ImNqZGljMm4wdzE2OHEzMW5xamFqMGNiNXcifQ.VBHGRcYrbq9wIer87aNUfA')

from app import app

data = pd.read_csv('data/final_data.csv')
data_2 = pd.read_csv('data/wtf.csv')
data_2 = data_2.drop('Unnamed: 0', axis=1)
data_2 = data_2.sort_values(by='Score', ascending=False)
data_3 = pd.read_csv('data/wtf2.csv')
data_3 = data_3.drop('Unnamed: 0', axis=1)
data_3 = data_3.sort_values(by='Total', ascending=False)

fig = px.scatter_mapbox(data, 
                        lat=data['Latitude'], 
                        lon=data['Longitude'],  
                        color="Total Average Score",
                        color_continuous_scale=px.colors.cyclical.IceFire, 
                        hover_data=["School Name", "City","Student Enrollment","Total Average Score"],
                        size_max=20, zoom=9)
fig.update_layout(mapbox = {'style': "dark"})

fig2 = px.scatter(data, x="Student Enrollment", y="Total Average Score", color="City", trendline="ols", color_continuous_scale=px.colors.cyclical.IceFire)
fig2.update_layout(hovermode="x")
fig2.update_layout(xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    color = 'white',
                    linecolor='white',
                    linewidth=2,
                ),
                    yaxis=dict(
                    color = 'white',
                    linecolor='white',
                    showgrid=False,
                    zeroline=False,
                    showline=True,
                    showticklabels=True,
                ),
                    showlegend=True,
                    plot_bgcolor='white'
                )

fig3 = px.bar(data_2, x="City", y="Score", color="Type", text="Score", color_discrete_sequence =px.colors.qualitative.Pastel1)
fig3.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig3.update_layout(uniformtext_minsize=10, uniformtext_mode='hide')
fig3.add_hline(y=1320, line_dash="dot",line_color="white")
fig3.add_annotation(
        x="Rockaway Park",
        y=1320,
        xref="x",
        yref="y",
        text="Average Total Score",
        showarrow=True,
        font=dict(
            family="Poppins",
            size=12,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor="#ffffff",
        ax=20,
        ay=-25,
        opacity=0.8
        )
fig3.add_annotation(
        x="Oakland Gardens",
        y=1568,
        xref="x",
        yref="y",
        text="Max = 1568",
        showarrow=True,
        font=dict(
            family="Poppins",
            size=12,
            color="#ffffff"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1.5,
        arrowcolor="#ffffff",
        ax=30,
        ay=-25,
        bordercolor="#ffffff",
        borderwidth=1,
        borderpad=4,
        bgcolor="white",
        opacity=0.8
        )
fig3.add_annotation(
        x="Queens Village",
        y=1500,
        xref="x",
        yref="y",
        text="Last 3",
        showarrow=True,
        font=dict(
            family="Poppins",
            size=12,
            color="#ffffff"
        ))
fig3.add_vrect(x0="Far Rockaway", x1="Cambria Heights", 
              fillcolor="red", opacity=0.25, line_width=0)
fig3.update_layout(xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    color = 'white',
                    linecolor='white',
                    linewidth=2,
                ),
                    yaxis=dict(
                    color = 'white',
                    linecolor='white',
                    showgrid=False,
                    zeroline=False,
                    showline=True,
                    showticklabels=True,
                ),
                    showlegend=True,
                    plot_bgcolor='white'
                )

fig4 = px.bar(data_3, x="City", y="Total", color="Type", text="Total", color_discrete_sequence =px.colors.qualitative.Pastel1)
fig4.update_traces(texttemplate='%{text:.2s}', textposition='inside')
fig4.update_layout(uniformtext_minsize=10, uniformtext_mode='hide')
fig4.add_hline(y=1280, line_dash="dot",line_color="white")
fig4.add_annotation(
            x="Corona",
            y=1280,
            xref="x",
            yref="y",
            text="Average Population",
            showarrow=True,
            font=dict(
                family="Poppins",
                size=12,
                color="#ffffff"
                ),
            align="center",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1.5,
            arrowcolor="#ffffff",
            ax=20,
            ay=-25,
            opacity=0.8
        )
fig4.update_layout(xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    color = 'white',
                    linecolor='white',
                    linewidth=2,
                ),
                    yaxis=dict(
                    color = 'white',
                    linecolor='white',
                    showgrid=False,
                    zeroline=False,
                    showline=True,
                    showticklabels=True,
                ),
                    showlegend=True,
                    plot_bgcolor='white'
                )

url = "https://assets4.lottiefiles.com/packages/lf20_UhulBK.json"
url2 = "https://assets4.lottiefiles.com/packages/lf20_K7aZUG.json"
url3 = "https://assets4.lottiefiles.com/packages/lf20_fBCpuQ.json"
url4 = "https://assets2.lottiefiles.com/packages/lf20_2ixzdfvy.json"
options_lottie = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

layout = html.Div([
    html.H1('SAT Scores for NYC Public Schools Report'),
    html.Div('Name, location, enrollment, and scores for 2014-2015 school year', className = 'sub_title'),
    html.Div('', className = "separation_line"),
    
    ## Part 1 Map
    de.Lottie(options=options_lottie, width="7%", height="7%", url=url),
    html.H1('', id='my_title'),
    dcc.RadioItems(id='radio_button',
                   options=[{'label': 'Average Score', 'value': 'Total Average Score'},
                            {'label': 'Student Population', 'value': 'Student Enrollment'}],
                   value='Total Average Score', 
                   className = 'mapRadioButton'),
    html.Div([dcc.Graph(id='my_map', 
                        figure=fig, 
                        className='chartContainer')],
              className = 'chartOuterContainer'),
    
    #Part 1 Top 3 School in Score/Population
    html.H1('', id='my_top_title'),
    html.Div([html.Div([html.Img(src=app.get_asset_url('pic/geometric.png')),
                        html.Div([html.Div('', id='school1'),
                                  html.Div('', id='score1')], className="toptextContainer")], 
                                  className="topSubContainer firstBG"),
              html.Div([html.Img(src=app.get_asset_url('pic/logo.png')),
                        html.Div([html.Div('', id='school2'),
                                  html.Div('', id='score2')], className="toptextContainer")],  
                                  className="topSubContainer secondBG"),
              html.Div([html.Img(src=app.get_asset_url('pic/shapes.png')),
                        html.Div([html.Div('', id='school3'),
                                  html.Div('', id='score3')], className="toptextContainer")],  
                                  className="topSubContainer thirdBG")], 
              className = "topContainer"),

    ## Part 1 Observation
    html.H1('Observation'),
    html.Div(html.Div('It seems that the close the school is to the center of New York, the higher the score, the lower the number of students', className = 'observation_container'), className = 'observation_outer_container'),
    html.Div('', className = "separation_line"),
    
    # Part 2 Relationship
    de.Lottie(options=options_lottie, width="10%", height="10%", url=url2),
    html.H1('', id='my_title2'),
    html.Div([
        html.Div([
            html.P('Choose X-Axis'),
            dcc.Dropdown(
                id='school-dropdown',
                options=[
                    {'label': 'Distance to New York Central (KM)', 'value': 'Distance'},
                    {'label': 'No of White', 'value': 'No of White'},
                    {'label': 'No of Black', 'value': 'No of Black'},
                    {'label': 'No of Hispanic', 'value': 'No of Hispanic'},
                    {'label': 'No of Asian', 'value': 'No of Asian'}
                ],
                value='Distance'
            )],className="sub_container"),
        html.Div([
            html.P('Choose Y-Axis'),
            dcc.Dropdown(
                id='school-dropdown2',
                options=[
                    {'label': 'Average Score (SAT Math)', 'value': 'Average Score (SAT Math)'},
                    {'label': 'Average Score (SAT Reading)', 'value': 'Average Score (SAT Reading)'},
                    {'label': 'Average Score (SAT Writing)', 'value': 'Average Score (SAT Writing)'},
                    {'label': 'Total Average Score', 'value': 'Total Average Score'},
                    {'label': 'No of Students', 'value': 'Student Enrollment'}
                ],
                value='Total Average Score'
            )],className="sub_container")], className="dropdownContainer"),
    html.Div([dcc.Graph(id='my_scatter', 
                        figure=fig2, 
                        className='chartContainer')],className = 'chartOuterContainer'),
    html.Div('', className = "separation_line"),

    #Part 3 Score Comparsion
    de.Lottie(options=options_lottie, width="10%", height="10%", url=url3),
    html.H1('Barchart breakdown for score and population'),
    html.H2('Score Breakdown'),
    html.Div([dcc.Graph(figure=fig3, className='chartContainer')],className = 'chartOuterContainer'),
    html.H2('Population Breakdown'),
    html.Div([dcc.Graph(figure=fig4, className='chartContainer')],className = 'chartOuterContainer'),
    html.Div('', className = "separation_line"),

    #The End       
    html.H1('End of Report'),
    de.Lottie(options=options_lottie, width="10%", height="10%", url=url4)

],className='mainContainer')

# Map Callback
@app.callback(Output('my_map', 'figure'),[Input('radio_button', 'value')])
def update_map(input_value):
    fig = px.scatter_mapbox(data, 
                            lat=data['Latitude'], 
                            lon=data['Longitude'],  
                            color=input_value,
                            color_continuous_scale=px.colors.cyclical.IceFire, 
                            hover_data=["School Name", "City","Student Enrollment","Total Average Score"],
                            size_max=20, zoom=9)
    fig.update_layout(mapbox = {'style': "dark"})
    return fig

@app.callback(Output('my_title', 'children'),[Input('radio_button', 'value')])
def update_title(value):
    title = value
    return 'SAT Score Map For "{}"'.format(title)

@app.callback([Output('school1', 'children'), 
               Output('school2', 'children'), 
               Output('school3', 'children'),
               Output('score1', 'children'), 
               Output('score2', 'children'), 
               Output('score3', 'children'),
               Output('my_top_title', 'children')],
              [Input('radio_button', 'value')])
def update_title(value):
    school1 = data.nlargest(3, value).iloc[[0]]['School Name'].values[0]
    school2 = data.nlargest(3, value).iloc[[1]]['School Name'].values[0]
    school3 = data.nlargest(3, value).iloc[[2]]['School Name'].values[0]
    score1 = data.nlargest(3, value).iloc[[0]][value].values[0]
    score2 = data.nlargest(3, value).iloc[[1]][value].values[0]
    score3 = data.nlargest(3, value).iloc[[2]][value].values[0]
    title = 'Top 3 For "{}"'.format(value)
    return [school1, school2, school3, score1, score2, score3, title]

# Scatter Callback
@app.callback(Output('my_title2', 'children'),[Input('school-dropdown', 'value'), Input('school-dropdown2', 'value')])
def update_title(value, value2):
    xaxis = value
    yaxis = value2
    return 'Scatterplot between "{}" and "{}"'.format(xaxis, yaxis)

@app.callback(Output('my_scatter', 'figure'),[Input('school-dropdown', 'value'), Input('school-dropdown2', 'value')])
def update_scatter(value, value2):
    fig2 = px.scatter(data, x=value, y=value2, color="City", trendline="ols", color_continuous_scale=px.colors.cyclical.IceFire)
    fig2.update_layout(xaxis=dict(
                        showline=True,
                        showgrid=False,
                        showticklabels=True,
                        color = 'white',
                        linecolor='white',
                        linewidth=2,
                    ),
                        yaxis=dict(
                        color = 'white',
                        linecolor='white',
                        showgrid=False,
                        zeroline=False,
                        showline=True,
                        showticklabels=True,
                    ),
                        showlegend=True,
                        plot_bgcolor='white'
                    )
    return fig2