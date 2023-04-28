## Create Virtual Environment

```bash
python3.9 -m venv venv 
```

Define your path for tesseract in `.env`. For example for linux

```nano
TESSERACT='pytesseract'
```

Install dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Launch App in local

```bash
python app.py 
```

## Test

```bash
pytest
```

## Suggestions

Moved and structured Dash app in `callbacks`, `config`, `layout`, and `test`. Also removed prints. For improve timing and code, a suggestion may can be to have a preloaded data and only import that data for another components. It can be stored as a database field. Next, only analise the new shapes and update the text extracted previously.