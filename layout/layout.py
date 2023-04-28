from dash import dash_table, dcc, html

from config.data_preload import fig, config

columns = ['shape', 'label', 'row', 'text']

layout = html.Div(
    [
        html.H4("Draw a shape, then modify it"),
        dcc.Graph(id="fig-image", figure=fig, config=config,style={'width': '150vh', 'height': '150vh',"border":"1px black solid"}),
        dcc.Markdown("Characteristics of shapes"),
        # html.Pre(id="annotations-pre"),
        dash_table.DataTable(id='canvaas-table',
                             style_cell={'textAlign': 'left'},
                             columns=[{"name": i, "id": i} for i in columns]),
    ]
)
