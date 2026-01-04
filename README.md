# 🏠 Connstel

A comprehensive hostel management system designed to streamline hostel operations and enhance communication between hostel administrators, wardens, and residents.

---
## Live Demo at [Connstel](https://hostel-connect-frontend.onrender.com/)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Contributors](#contributors)

## 🌟 Overview

Hostel Connect is a full-stack web application that simplifies hostel management by providing tools for room allocation, resident management, complaint handling, and administrative tasks. The platform aims to reduce paperwork and improve efficiency in hostel operations.

## ✨ Features

- Students can submit hostel complaints with details like name, room number, category, and description.
-  All complaints are securely stored in Google Firestore with timestamps.
- Gemini AI automatically analyzes complaints to generate priority levels and short summaries.
- Helps authorities quickly understand the nature and urgency of each issue.
- Instant WhatsApp alerts notify hostel authorities when a new complaint is registered.
- Built with FastAPI, enabling easy integration with future dashboards or mobile apps.

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python

### Database
- Firebase(Cloud)

## 📁 Project Structure

```
hostel-connect/
├── backend/
│   ├── main.py
|   ├── whatsapp.py
│   └── requirements.txt     # Python dependencies
│
├── frontend/
│   ├── style.css             # Stylesheets
│   ├── app.js                # JavaScript files
│   ├── firebase.js              
│   └── index.html            # Main HTML files
│
├── .gitignore
└── README.md
```

## 👥 Contributors

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/JaskeeratK">
        <img src="https://github.com/JaskeeratK.png" width="100px;" alt="JaskeeratK"/>
        <br />
        <sub><b>Jaskeerat</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Muskan-kaur133">
        <img src="https://github.com/Muskan-kaur133.png" width="100px;" alt="Muskan-kaur133"/>
        <br />
        <sub><b>Muskan Kaur</b></sub>
      </a>
    </td>
  </tr>
</table>


**Made with ❤️ for better hostel management**
