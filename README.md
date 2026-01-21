# 🔗 URL Shortener API

A RESTful URL Shortening Service built using **Python (Flask)** and **MySQL**.  
This project allows users to shorten long URLs, use custom aliases, redirect users, track access statistics, and manage links efficiently.

---

## 🚀 Features

- Create short URLs from long URLs
- Support for **custom short codes (nicknames)**
- Redirect to original URL using short code
- Update existing short URLs
- Delete short URLs
- Track access count (analytics)
- Swagger API documentation
- RESTful design with proper HTTP status codes

---

## 🛠️ Tech Stack

- **Backend:** Python 3.11, Flask
- **Database:** MySQL
- **ORM:** SQLAlchemy
- **API Documentation:** Flask-RESTX (Swagger)
- **Environment Management:** python-dotenv

---

## 📂 Project Structure

url-shortener/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
├── .env
│
├── routes/
│ └── shorten.py
│
└── utils/
└── code_generator.py


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/url-shortener-api.git
cd url-shortener-api

2️⃣ Create Virtual Environment (Python 3.11)
py -3.11 -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file:

DB_USER=root
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_NAME=url_shortener

5️⃣ Create Database (MySQL)
CREATE DATABASE url_shortener;


Tables will be created automatically by SQLAlchemy.

▶️ Run the Application
python app.py


Server will start at:

http://127.0.0.1:5000


Swagger API Docs:

http://127.0.0.1:5000/docs

🔌 API Endpoints
Create Short URL
POST /shorten

{
  "url": "https://www.example.com",
  "customCode": "example"
}

Retrieve Original URL
GET /shorten/{shortCode}

Redirect to Original URL
GET /{shortCode}

Update Short URL
PUT /shorten/{shortCode}

Delete Short URL
DELETE /shorten/{shortCode}

Get URL Statistics
GET /shorten/{shortCode}/stats

📊 Example Use Cases

Marketing campaign links

Referral and affiliate systems

SMS and social media sharing

QR code redirection

Temporary promotional links

🧠 Key Learnings

RESTful API design

HTTP methods & status codes

Database modeling with ORM

URL redirection handling

Analytics tracking

Environment-based configuration

🚧 Future Improvements

URL expiry feature

Redis caching for faster redirects

Authentication & authorization

Rate limiting

Docker support

Cloud deployment

## 🌐 Solution URL

- **GitHub Repository:**  
  https://github.com/jaiprathap26/url-shortener-api

- **Local API Base URL:**  
  http://127.0.0.1:5000

- **Swagger API Documentation:**  
  http://127.0.0.1:5000/docs





