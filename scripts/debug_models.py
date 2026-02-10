import os
from google import genai
from dotenv import load_dotenv

# Load .env file for local testing
load_dotenv()

API_KEY = os.environ.get("GOOGLE_API_KEY")

if not API_KEY:
    print("Kein GOOGLE_API_KEY gefunden!")
else:
    print(f"API Key gefunden (endet auf ...{API_KEY[-4:]})")
    try:
        client = genai.Client(api_key=API_KEY)
        print("--- Verfügbare Modelle ---")
        for m in client.models.list():
            print(f"MODEL_ENTRY|{m.name}")
    except Exception as e:
        print(f"Fehler beim Zugriff auf Gemini: {e}")
