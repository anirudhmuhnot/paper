from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash
import home
from predictHotspots import hotspots
from drivingBehaviour import behaviour,newRecord, analysis
import pandas as pd



app = dash.Dash()
app.title = 'Road Safety App'
server = app.server
app.config['suppress_callback_exceptions']=True
#implement Notifications and validations
#apps_database
apps = {
  '/home':home,
  '/drivingBehaviour/behaviour': behaviour,
  '/predictHotspots/hotspots': hotspots,
  '/drivingBehaviour/newRecord': newRecord,
  '/drivingBehaviour/analysis': analysis
}

#loaded navbar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(className='navbar-fixed',children=[
        html.Nav([
            html.Div(className='nav-wrapper light-green',children=[
                dcc.Link(className='brand-logo right hide-on-med-and-down',children=[html.I(className='material-icons left',children=['blur_on']),'SafeRoads'],href='/home'),
                html.Ul(className='left hide-on-med-and-down',children=[
                    dcc.Link(html.Li(children=[html.I(className='material-icons left',children=['home']),'Home']),href='/home')
                ]),
                html.Ul(className='left',children=[
                    dcc.Link(html.Li(children=[html.I(className='material-icons left',children=['local_taxi']),'Driving Behaviour']),href='/drivingBehaviour/behaviour')
                ]),
                    html.Ul(className='left',children=[
                    dcc.Link(html.Li(children=[html.I(className='material-icons left',children=['find_in_page']),'Hotspots']),href='/predictHotspots/hotspots')
                ])
            ])
        ])
    ]),
    #display container, layouts are returned to this container
    html.Div(id='output'),
    html.Div(id='temp')
])


#for content
@app.callback(Output('output', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    for key,value in apps.items():
      if pathname == key:
        return value.layout
    return home.layout


@app.callback(Output('temp','children'),
    [
        Input('my-button', 'n_clicks'),
        Input('fname', 'value'),
        Input('lname', 'value'),
        Input('gender', 'value'),
        Input('dob', 'value'),
        Input('licence', 'value'),
        Input('registeration', 'value'),
        Input('date', 'value'),
        Input('time', 'value'),
        Input('injuries', 'value'),
        Input('fatalities', 'value'),
        Input('vehicles', 'value'),
        Input('upload-image', 'contents'),
        Input('upload-image', 'filename')
    ])
def on_submit(n_clicks,fname,lname,gender,dob,licence,registeration,date,time,injuries,fatalties,vehicles,contents,
              filename):
    if n_clicks >=1:
        arr = [fname,lname,gender,dob,licence,registeration,date,time,injuries,fatalties,vehicles,contents,
              filename]
        df = pd.DataFrame(arr)
    return dcc.Location(id='url',pathname='/home')


external_css = [
    'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css',
    'https://fonts.googleapis.com/icon?family=Material+Icons',
    'https://codepen.io/muhnot/pen/bKzaZr.css'
]
external_js = [
     'https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js'
]

for my_js in external_js:
  app.scripts.append_script({"external_url": my_js})


for css in external_css:
    app.css.append_css({"external_url": css})


if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0',port=8050)