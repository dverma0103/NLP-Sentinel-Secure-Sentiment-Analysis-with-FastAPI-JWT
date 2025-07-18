
# 🧠 Text Sentiment Analysis API

A scalable and secure Text Sentiment Analysis REST API built with **FastAPI**, integrated with **NLTK** for natural language processing, **SQLAlchemy** for database interaction, and **JWT Authentication** for secure user access.

---

## 🚀 Features

- 🔐 **JWT Authentication** (Login/Register Protected Endpoints)  
- 📊 **Sentiment Analysis** using `nltk.sentiment.SentimentIntensityAnalyzer`  
- 🧹 Text Preprocessing: Tokenization, Stopword Removal, Lemmatization  
- 🗃️ Persistent storage using **SQLAlchemy** ORM  
- 🧪 Token-based User-specific Sentiment Logs  
- ⚡ FastAPI framework for high performance  

---

## 🛠️ Tech Stack

- **FastAPI** – High-performance web framework  
- **SQLAlchemy** – ORM for PostgreSQL / SQLite  
- **NLTK** – Natural Language Toolkit for text preprocessing & sentiment  
- **JWT** – Authentication using JSON Web Tokens  
- **Pydantic** – Data validation and serialization  

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py                # FastAPI application
│   ├── schemas.py             # SQLAlchemy models and Pydantic models
│   ├── user.py                # User authentication and registration
│   ├── database.py            # DB session / engine
│   ├── auth.py                # JWT auth utils
│   └── sentiment_analyser.py  # Sentiment analysis logic
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-api.git
cd sentiment-analysis-api
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Download NLTK Resources

Create a separate setup script or run the following in Python:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('vader_lexicon')
```

---

## 🧪 Run the API Server

```bash
uvicorn app.main:app --reload
```

---

## 🔑 Authentication Flow

- `POST /register` – Create new user  
- `POST /login` – Get JWT token  
- Authenticated routes require a token in the header:  
  `Authorization: Bearer <your_token>`  

---

## 📝 Sample Request

### Analyze Sentiment

**Endpoint:**

```http
POST /analyze
```

**Headers:**

```http
Authorization: Bearer <your_token>
Content-Type: application/json
```

**Body:**

```json
{
  "text": "The product was good, but delivery was delayed."
}
```

**Response:**

```json
{
  "label": "Neutal"
}
```

---

## 📚 Future Enhancements

- 🔍 Add user-level sentiment history logs  
- 📊 Dashboard with sentiment trends  
- 🌍 Multi-language support  
- 🧠 Train custom sentiment model (optional)  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)  
- [NLTK](https://www.nltk.org/)  
- [Uvicorn](https://www.uvicorn.org/)  
- [JWT.io](https://jwt.io/)
