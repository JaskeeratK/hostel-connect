const BACKEND_URL = "http://127.0.0.1:8000/process";

window.addEventListener("DOMContentLoaded", () => {
  document.getElementById("submitBtn").addEventListener("click", async () => {

    const studentName = document.getElementById("hostel").value;
    const roomNumber = document.getElementById("room").value;
    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value;

    try {
      const res = await fetch(BACKEND_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          studentName,
          roomNumber,
          category,
          description,
        })
      });

      const data = await res.json();

      document.getElementById("status").innerText =
        "Complaint submitted successfully!";
    } catch (err) {
      console.error(err);
      document.getElementById("status").innerText =
        "Error submitting complaint";
    }
  });
});

