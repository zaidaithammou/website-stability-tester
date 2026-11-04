# 🌐 Web Stability Tester

A lightweight, modern web application built with **Flask** and **Vanilla JavaScript** that enables users to test the real-time connectivity and uptime stability of any website URL.

## ✨ Features

* **Real-Time Uptime Monitoring:** Instantly checks whether a target URL is online or offline with a built-in 5-second timeout safeguard.
* **Modern Glassmorphic UI:** Features a sleek, dark-mode dashboard styled with custom CSS variables, status badges, and smooth animations.
* **Asynchronous Requests:** Utilizes the JavaScript `Fetch API` for non-blocking status updates and seamless user interaction.
* **Automatic Protocol Handling:** Intelligently prepends `https://` if users omit the protocol in their input.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Requests
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 📂 Project Structure

```text
web-stability-tester/
│
├── app.py              # Main Flask application and backend routing
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── templates/
    └── index.html      # Frontend dashboard interface