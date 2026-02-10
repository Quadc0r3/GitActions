import os
from google import genai
from dotenv import load_dotenv

# Load .env file for local testing
load_dotenv()

API_KEY = os.environ.get("GOOGLE_API_KEY")

if not API_KEY:
    print("Kein GOOGLE_API_KEY gefunden! Bitte stelle sicher, dass die .env Datei existiert und korrekt befüllt ist.")
else:
    print(f"API Key gefunden (endet auf ...{API_KEY[-4:] if len(API_KEY) > 4 else '***'})")
    try:
        client = genai.Client(api_key=API_KEY)
        print("--- Verfügbare Modelle ---")
        # In the new SDK, listing models is slightly different
        for m in client.models.list():
            print(f"Name: {m.name} (Methods: {m.supported_generation_methods})")
    except Exception as e:
        print(f"Fehler beim Zugriff auf Gemini: {e}")
