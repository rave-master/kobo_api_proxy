# KoboToolbox API Proxy (Flask)

A simple Flask-based proxy server to securely fetch KoboToolbox form submissions using an API token and form ID.

## 🚀 Deploy on Render.com

1. Fork or clone this repo.
2. Go to https://render.com and create a new Web Service.
3. Connect your GitHub repo and deploy with the following settings:
   - Runtime: Python 3
   - Start Command: `gunicorn app:app`

## 🧪 Test Locally

```bash
pip install -r requirements.txt
python app.py
```

Then use POST to `/get-data` with JSON like:

```json
{
  "form_id": "your_form_id_here",
  "token": "your_api_token_here"
}
```

## 🔐 Note

Keep your API token secret — never expose it in frontend JavaScript!