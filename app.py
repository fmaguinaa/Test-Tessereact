from dash import Dash, dependencies, no_update

from callbacks.callbacks import on_new_shapes
from layout.layout import layout

app = Dash(__name__)
app.layout = layout

@app.callback(
    # dependencies.Output('annotations-pre', 'children'),
    dependencies.Output('canvaas-table', 'data'),
    dependencies.Input("fig-image", "relayoutData"),
    prevent_initial_call=True,
)
def on_new_annotation(annotation):
    #for key in relayout_data:
    if "shapes" in annotation:
        return on_new_shapes(annotation.get('shapes'))
    return no_update

if __name__ == "__main__":
    app.run_server(debug=True)