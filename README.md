# Tesla Clone – Backend (Flask)

This is the Flask backend for the Tesla Clone project. It serves the main homepage, Cybertruck product page, and handles 404 errors. The backend is deployed using [Render](https://render.com/), and is designed to work in tandem with a static frontend hosted on [Vercel](https://vercel.com/).

---

## 🚀 Live Demo

Backend URL (Render): [https://tesla-clone-56tq.onrender.com](https://tesla-clone-56tq.onrender.com)  
Frontend URL (Vercel): [https://tesla-clone-frontend.vercel.app](https://tesla-clone-frontend.vercel.app)

---
# Tesla Clone Frontend Repository (Vercel)

[https://github.com/NikhitaRachael/Tesla-clone-Frontend](https://github.com/NikhitaRachael/Tesla-clone-Frontend)

---
## 📁 Project Structure
```
Tesla-clone/
├── app.py
├── requirements.txt
├── templates/
│ ├── index.html
│ ├── cybertruck.html
│ └── 404.html
└── static/
└── css/
└── style.css
```

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Jinja2
- **Hosting**: Render (Web Service)
- **Frontend**: HTML/CSS hosted separately on Vercel

---

## 🧪 Local Development

### Prerequisites:
- Python 3.9+
- `pip` installed

### Setup Instructions:

```bash
# Clone the repo
git clone https://github.com/NikhitaRachael/Tesla-clone.git
cd Tesla-clone

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
Access it locally at http://127.0.0.1:5000/

## 🌐 Deployment (Render)
Connect your GitHub repo to Render

Choose “Web Service” → Python

Build command: pip install -r requirements.txt
Start command: python app.py

Set Python version in render.yaml or environment

Deploy!

## 📄 License
This project is licensed for educational and portfolio use. Not affiliated with Tesla, Inc.

## 👩‍💻 Author
Nikhita Rachael
GitHub
