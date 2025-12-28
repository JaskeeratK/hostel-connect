import { db } from "./firebase.js";
import {
  collection,
  addDoc,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";

console.log("APP.JS LOADED");

const BACKEND_URL = "http://127.0.0.1:8000/process";

window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("submitBtn").addEventListener("click", async () => {
    console.log("Button clicked");

    const hostel = document.getElementById("hostel").value;
    const room = document.getElementById("room").value;
    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value;

    try {
      const docRef = await addDoc(collection(db, "complaints"), {
        hostel,
        room,
        category,
        description,
        status: "pending",
        created_at: serverTimestamp()
      });

      await fetch(BACKEND_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          complaint_id: docRef.id,
          text: description
        })
      });

      document.getElementById("status").innerText =
        "Complaint submitted successfully!";
    } catch (err) {
      console.error(err);
      document.getElementById("status").innerText =
        "Error submitting complaint";
    }
  });
});
