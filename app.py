import dash

app = dash.Dash(__name__, 
                title="SAT Score Analysis",
                suppress_callback_exceptions=True)
server = app.server
