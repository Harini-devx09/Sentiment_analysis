# 🛍️ Amazon Product Review Sentiment Analysis

This project performs sentiment analysis on Amazon product reviews using machine learning. The application classifies user reviews as **Positive** or **Negative**, helping businesses and users gain insights into customer feedback.

## 🚀 Features

- Clean, minimal Flask web app
- Text preprocessing using `TfidfVectorizer`
- Classification using Logistic Regression
- Real-time prediction from user input
- WordCloud visualization of sentiments


## 🧠 How It Works

1. Dataset is preprocessed and vectorized using TF-IDF.
2. Logistic Regression is trained to classify review sentiment.
3. The trained model is saved as `sentiment_model.pkl`.
4. Flask app takes user input, applies preprocessing, and predicts sentiment in real-time.

## 📊 Example

> **Input:** "Loved the design and quality, worth the price!"  
> **Predicted Sentiment:** ✅ **Positive**

> **Input:** "Very poor quality and terrible service."  
> **Predicted Sentiment:** ❌ **Negative**

## 🔧 Installation

```bash
git clone https://github.com/Harini-devx09/Sentiment_analysis.git
cd Sentiment_analysis
pip install -r requirements.txt
python app.py


