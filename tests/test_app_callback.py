from .mock_data import data

from app import on_new_annotation

def test_new_annotation():
    output = on_new_annotation(data)
    first_row = output[0]
    assert len(output) == 5
    assert first_row.get('shape') == 0
    assert first_row.get('label') == 'shape-10'
    assert first_row.get('row') == 0
    assert first_row.get('text') == 'WATER VOLUME 70359619 A 12/10/2021 01/11/2022 50680 51076 39600 $55.84'