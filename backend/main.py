import os
from dotenv import load_dotenv
load_dotenv()
os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
from fastapi import FastAPI
from google.cloud import firestore
from google import genai


app = FastAPI()
db = firestore.Client()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))



from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # OK for local dev
    allow_methods=["*"],
    allow_headers=["*"],
)

def send_whatsapp(message):
    print("WhatsApp Alert:", message)

@app.post("/process")
async def process_complaint(data: dict):
    complaint_id = data["complaint_id"]
    text = data["text"]

    prompt = f"""
    Categorize the hostel complaint.
    Return:
    - category
    - priority (Low/Medium/High)

    Complaint: {text}
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    ai_result = response.text

    db.collection("complaints").document(complaint_id).update({
        "ai_analysis": ai_result,
        "ai_processed": True
    })

    send_whatsapp(f"New Hostel Complaint:\n{text}\n\n{ai_result}")

    return {"status": "ok"}
