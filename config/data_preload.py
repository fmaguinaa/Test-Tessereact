import cv2
import os
from PIL import Image, ImageEnhance, ImageFilter
import plotly.express as px

import pandas as pd

from .tesseract import pytesseract

directory = os.getcwd()
data_path = f'{directory}/config/data'

image_filename = f'{data_path}/ADMIN1.jpg'


def preload_image_shapes():

    img = cv2.imread(image_filename)
    d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    dfCoord=pd.DataFrame.from_dict(d)
    dfCoord = dfCoord[(dfCoord['text'] == "77487-5029")]
    dfCoord=dfCoord.iloc[0]
    yCoor = dfCoord['top']
    xCoor = dfCoord['left']

    fig = Image.open(image_filename)
    fig = px.imshow(fig)
    shapes=pd.read_csv(f'{data_path}/shapeSugarLand1.csv')
    row_1=shapes.iloc[0]

    yCoor = yCoor-row_1['y0']
    xCoor = xCoor-row_1['x0']

    for index, row in shapes.iterrows():
        fig.add_shape(
            type='rect', xref='x', yref='y', label=dict(text=f'shape-{index}', textposition="top left", font=dict(color="red"), padding=0),
            x0=row['x0']+xCoor, x1=row['x1']+xCoor, y0=row['y0']+yCoor, y1=row['y1']+yCoor, line=dict(color="red", width=1)
        )

    fig.update_layout(dragmode="drawrect",
                    #newshape=dict(fillcolor="cyan", opacity=0.3, line=dict(color="red", width=1)),)
                    newshape=dict(line=dict(color="red", width=1), label=dict(text='new-shape', textposition="top left", font=dict(color="red"), padding=0)),)
    fig.update_layout( margin={'l': 0, 'r': 0, 't': 0, 'b': 0})

    return fig

fig = preload_image_shapes()

config = {
    "modeBarButtonsToAdd": [
        #"drawline",
        #"drawopenpath",
        #"drawclosedpath",
        #"drawcircle",
        "drawrect",
        "eraseshape",
    ]
}