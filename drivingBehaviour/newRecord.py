import dash_core_components as dcc
import dash_html_components as html


layout = html.Div(className='container',children=[

    html.Center(html.H3('Incident Details')),
    html.H4('Enter Driver Details: '),

    html.Div(className='row',children=[

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['account_circle']),
            dcc.Input(id='fname', type='text'),
            html.Label(htmlFor='fname',children= ['First Name'])
        ]),

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['account_circle']),
            dcc.Input(id='lname', type='text'),
            html.Label(htmlFor='lname',children= ['Last Name'])
        ]),

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['date_range']),
            dcc.Input(id='dob', type='date',className='validate'),
            html.Label(htmlFor='dob',children= ['Date of Birth:'])
        ]),

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['perm_identity']),
            dcc.Input(id='licence', type='text'),
            html.Label(htmlFor='licence',children= ['Licence Number:'])
        ]),

        html.Div(className='col l12 m12 s12',children=[
            html.Label(children= ['Gender']),
            dcc.Dropdown(
                id='gender',
                options=[
                    {'label': 'Male', 'value': 'male'},
                    {'label': 'Female', 'value': 'female'}
             ],
            value=''
            )
        ]),

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['local_taxi']),
            dcc.Input(id='registeration', type='text'),html.Label(
                htmlFor='registeration',children= ['Registeration Number:'])
        ]),

        html.Div(className='col l12 m12 s12',children=[
                html.H4('Enter Event Details: ')
        ]),

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['date_range']),
            dcc.Input(id='date', type='date',className='validate'),
            html.Label(htmlFor='date',children= ['Date of Accident:'])
        ]),

        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['schedule']),
            dcc.Input(id='time', type='time',className='validate'),
            html.Label(htmlFor='time',children= ['Time of Accident'])
        ]),


        html.Div(className='input-field col l6 m6 s12',children=[
            html.I(className="material-icons prefix",children=['local_pharmacy']),
            dcc.Input(id='injuries', type='text'),
            html.Label(htmlFor='injuries',children= ['Injuries'])
        ]),

        html.Div(className='input-field col l6 m6 s12', children=[
            html.I(className="material-icons prefix", children=['mood_bad']),
            dcc.Input(id='fatalities', type='text'),
            html.Label(htmlFor='fatalities', children=['Fatalities'])
        ]),

        html.Div(className='input-field col l6 m6 s12', children=[
            html.I(className="material-icons prefix", children=['local_taxi']),
            dcc.Input(id='vehicles', type='text'),
            html.Label(htmlFor='vehicles', children=['Number of Vehicles'])
        ])

    ]),
    html.H3('Upload Picture of the event: '),
    html.Div(className='container',children=[
        dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
    html.Br(),
    html.Center(html.Button('Submit Details', id='my-button')),
    html.Br(),
    html.Br()
    ])
])