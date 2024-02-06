import streamlit as st
from textblob import TextBlob

# Set Streamlit page configuration
st.set_page_config(page_title="Sentiment Analysis App", page_icon=":sparkles:")

# Function for sentiment analysis with TextBlob
def perform_sentiment_analysis(user_input):
    # Create a TextBlob object
    blob = TextBlob(user_input)

    # Get the sentiment polarity
    sentiment_polarity = blob.sentiment.polarity

    # Interpret the sentiment
    if sentiment_polarity > 0:
        sentiment = 'Positive'
        color = 'green'
    elif sentiment_polarity < 0:
        sentiment = 'Negative'
        color = 'red'
    else:
        sentiment = 'Neutral'
        color = 'gray'

    return sentiment, sentiment_polarity, color

# Main function for Streamlit app
def main():
    st.title("Sentiment Analysis with LLM")

    # User input for the sentence
    user_input = st.text_input("Enter a sentence:")

    # Perform sentiment analysis on button click
    if st.button("Perform Sentiment Analysis"):
        sentiment, sentiment_polarity, color = perform_sentiment_analysis(user_input)
        st.markdown(f"Sentiment: {sentiment} {':smile:' if sentiment == 'Positive' else ':disappointed:'}")
        st.markdown(f"Sentiment Polarity: {sentiment_polarity}")

if __name__ == "__main__":
    main()
