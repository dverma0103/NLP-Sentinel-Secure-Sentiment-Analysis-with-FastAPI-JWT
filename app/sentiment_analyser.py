from sqlalchemy.orm import Session
from schemas import Analyser, AnalyserCreate
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('punkt')             
nltk.download('stopwords')         
nltk.download('wordnet')           
nltk.download('omw-1.4')           
nltk.download('vader_lexicon')

stop_words = stopwords.words("english")
lemmatizer = WordNetLemmatizer()
sia = SentimentIntensityAnalyzer()

def text_cleaner(text:str):
    tokens = word_tokenize(text)
    filetered_tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
    lemmatized_tokens = [lemmatizer.lemmatize(word.lower(), pos="v") for word in filetered_tokens]
    return " ".join(lemmatized_tokens)

def sentiment_creater(text:str):
    scores = sia.polarity_scores(text)
    return "Positive" if scores["compound"] > 0.05 else "Negative" if scores["compound"] < -0.05 else "Neutral"

def create_analyser(db:Session, analyser:AnalyserCreate, user_id: int):
    cleaned_text = text_cleaner(analyser.inputs)
    sentiments = sentiment_creater(cleaned_text)
    analyser_db = Analyser(inputs = analyser.inputs, sentiment = sentiments, owner_id=user_id)
    db.add(analyser_db)
    db.commit()
    db.refresh(analyser_db)
    return analyser_db

def get_all_analysis(db:Session, user_id:int):
    return db.query(Analyser).filter(Analyser.owner_id == user_id).all()

def get_analysis(db:Session, analyser_id:int, user_id:int):
    return db.query(Analyser).filter(Analyser.id == analyser_id, Analyser.owner_id == user_id).first()

def delete_analysis(db:Session, analyser_id: int, user_id: int):
    analyser = get_analysis(db, analyser_id, user_id)
    if analyser:
        db.delete(analyser)
        db.commit()
