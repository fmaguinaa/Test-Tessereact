from config.tesseract import pytesseract
import pandas as pd
import cv2
from io import StringIO

from config.data_preload import image_filename

def on_new_shapes(shapes):
    data = pd.DataFrame.from_dict(shapes)
    img = cv2.imread(image_filename)

    data_shapes = pd.DataFrame()
    ReadingSection = pd.DataFrame()
    for index, row in data.iterrows():
        y1 = int(row.get('y0', 0))
        y2 = int(row.get('y1', 0))
        x1 = int(row.get('x0', 0))
        x2 = int(row.get('x1', 0))
        ReadingSection = img[y1:y2, x1:x2]
        text = pytesseract.image_to_string(ReadingSection, config='--psm 6')
        dfReadingSection = pd.DataFrame(dict(shape=index,label=row.get('label').get('text'),text=StringIO(text)))
        dfReadingSection['text'] = dfReadingSection['text'].str.replace('\n', '')
        dfReadingSection['text'] = dfReadingSection['text'].str.replace('\f', '')
        dfReadingSection = dfReadingSection[dfReadingSection['text'].str.len() > 0]
        dfReadingSection.reset_index(inplace=True)
        dfReadingSection = dfReadingSection.rename(columns = {'index':'row'})
        dfReadingSection = dfReadingSection.reindex(columns=['shape', 'label', 'row', 'text'])
        data_shapes = pd.concat([data_shapes, dfReadingSection])
    data_shapes = data_shapes.to_dict(orient='records')
    return data_shapes