import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import firestore
from google import genai

from whatsapp import send_whatsapp

app = FastAPI()
db = firestore.Client()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ✅ MUST EXIST
def add_complaint(data):
    return db.collection("complaints").add({
        "studentName": data["studentName"],
        "roomNumber": data["roomNumber"],
        "category": data["category"],
        "description": data["description"],
        "createdAt": datetime.utcnow(),
        "status": "pending",
        "summary": "",
        "whatsappSent": False,
        "aiProcessed": False
    })

@app.post("/process")
async def process_complaint(data: dict):
    print("Incoming data:", data)

    # 1️⃣ Store complaint
    doc_ref = add_complaint(data)
    complaint_id = doc_ref[1].id

    # 2️⃣ Run Gemini AI
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
    Categorize the hostel complaint.

    Room Number: {data["roomNumber"]}

    Return EXACTLY in this format (with labels):
    - priority: <Low/Medium/High>
    - short summary: <one line>

    Complaint: {data["description"]}
    """
    )

    ai_result = response.text

    # 3️⃣ Update Firestore
    db.collection("complaints").document(complaint_id).update({
        "summary": ai_result,
        "aiProcessed": True
    })

    # 4️⃣ WhatsApp 
    registered_number = os.getenv("REGISTERED_NUMBER")  

    try:
        message = f"""
📢 *New Hostel Complaint*

👤 Student: {data['studentName']}
🏠 Room: {data['roomNumber']}
📂 Category: {data['category']}

📝 Issue:
{data['description']}

Short Summary:
{ai_result}

⏰ Reported at: {datetime.utcnow().strftime('%d %b %Y, %I:%M %p')} UTC

✅ To update status, reply with one of:
- DONE 
- IN PROGRESS 
- NOT DONE 
"""

        send_whatsapp(
            message.strip(),
            to_number=registered_number
        )

        db.collection("complaints").document(complaint_id).update({
            "whatsappSent": True
        })
    except Exception as e:
        print("WhatsApp failed:", e)
        db.collection("complaints").document(complaint_id).update({
            "whatsappSent": False,
            "whatsappError": str(e)
        })

    return {
        "status": "ok",
        "complaint_id": complaint_id
    }
