const BACKEND_URL = "https://hostel-connect-4q25.onrender.com/process";

window.addEventListener("DOMContentLoaded", () => {
  const statusEl = document.getElementById("status");
  const submitBtn = document.getElementById("submitBtn");

  submitBtn.addEventListener("click", async () => {
    const studentName = document.getElementById("hostel").value.trim();
    const roomNumber = document.getElementById("room").value.trim();
    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value.trim();

    // Basic validation
    if (!studentName || !roomNumber || !description) {
      showStatus("Please fill all required fields", "error");
      return;
    }

    submitBtn.disabled = true;
    submitBtn.innerText = "Submitting...";

    try {
      const res = await fetch(BACKEND_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          studentName,
          roomNumber,
          category,
          description,
        }),
      });

      if (!res.ok) {
        throw new Error("Server error");
      }

      const data = await res.json();

      if (data.status === "ok") {
        showStatus(
          `✅ Complaint submitted successfully! (ID: ${data.complaint_id})`,
          "success"
        );

        // Clear form
        document.getElementById("hostel").value = "";
        document.getElementById("room").value = "";
        document.getElementById("description").value = "";
      } else {
        throw new Error("Unexpected response");
      }
    } catch (err) {
      console.error(err);
      showStatus("❌ Failed to submit complaint. Please try again.", "error");
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerText = "Submit Complaint";
    }
  });

  function showStatus(message, type) {
    statusEl.innerText = message;
    statusEl.className = "";
    statusEl.classList.add(type);
  }
});