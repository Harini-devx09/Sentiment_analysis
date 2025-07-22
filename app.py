import streamlit as st
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit App
st.set_page_config(page_title="Amazon Sentiment Analyzer", layout="centered")
st.title("🛒 Amazon Review Sentiment Analyzer")

st.markdown("""
Enter any Amazon product review and click **Analyze Sentiment** to see if it's **Positive**, **Negative**, or **Neutral**.
""")

# Input text
review = st.text_area("✍️ Enter a review here:")

if st.button("Analyze Sentiment"):
    if not review.strip():
        st.warning("Please enter a review before analyzing.")
    else:
        # Sentiment analysis
        score = analyzer.polarity_scores(review)
        compound = score['compound']

        if compound >= 0.05:
            sentiment = "POSITIVE 😊"
        elif compound <= -0.05:
            sentiment = "NEGATIVE 😞"
        else:
            sentiment = "NEUTRAL 😐"

        st.markdown(f"### Predicted Sentiment: **{sentiment}**")

        # Display scores
        st.write("**Detailed Scores:**")
        st.json(score)

        # Generate WordCloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(review)
        st.write("**Review WordCloud:**")
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)
