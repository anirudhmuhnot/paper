import dash_html_components as html
import dash_core_components as dcc


layout = html.Div(children=[
    #add top driving behaviours here and shift the lift to the leff
    html.Div(className='row',children=[
         html.Div(className='col s8'),
         html.Div(className='col s3',children=[
             html.H5(children=[
                 dcc.Link('Enter New Record',href='/drivingBehaviour/newRecord')
             ]),
             html.H5(children=[
                 dcc.Link('View Behavioural Analysis',href='/drivingBehaviour/analysis')
             ])
         ])
    ])
])

