## Create Virtual Environment

```bash
python3.9 -m venv venv 
```

Define your path for tesseract in `.env`. For example for linux

```nano
TESSERACT='pytesseract'
```

## Launch App in local

```bash
python app.py 
```

## Test

```bash
pytest
```