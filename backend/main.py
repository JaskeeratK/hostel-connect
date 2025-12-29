import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import firestore
from google import genai

from whatsapp import send_whatsapp  # ✅ import your real function

app = FastAPI()
db = firestore.Client()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/process")
async def process_complaint(data: dict):
    complaint_id = data["complaint_id"]
    text = data["text"]
    phone_no = data.get("phone_no")  # 📌 Pass the student's phone number

    # Fix model
    response = client.models.generate_content(
        model="gemini-2.5-flash",  # ✅ use available model
        contents=f"""
        Categorize the hostel complaint.
        Return:
        - category
        - priority (Low/Medium/High)
        Complaint: {text}
        """
    )

    ai_result = response.text

    db.collection("complaints").document(complaint_id).set({
        "ai_analysis": ai_result,
        "ai_processed": True
    })

    if phone_no:
        send_whatsapp(
            f"New Hostel Complaint:\n{text}\n\n{ai_result}",
            to_number=phone_no
        )
    else:
        print("No phone number provided, WhatsApp not sent")


    return {"status": "ok"}


