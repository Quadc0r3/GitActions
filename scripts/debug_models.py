import os
import google.generativeai as genai

API_KEY = os.environ.get("GOOGLE_API_KEY")

if not API_KEY:
    print("Kein GOOGLE_API_KEY gefunden!")
else:
    genai.configure(api_key=API_KEY)
    print("--- Verfügbare Modelle ---")
    try:
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(f"Name: {m.name}")
    except Exception as e:
        print(f"Fehler beim Auflisten der Modelle: {e}")
