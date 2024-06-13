import gspread
from gspread.exceptions import APIError
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re
from textblob import TextBlob

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to remove emojis from text
def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642" 
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Function to preprocess a single text string
def preprocess_text(text):
    # Remove emojis
    text = remove_emojis(text)
    
    # Lowercase the text
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Removing punctuation
    tokens = [token for token in tokens if token not in string.punctuation]
    
    # Removing stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Stemming or Lemmatization
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    
    # Join tokens back into a string
    preprocessed_text = ' '.join(tokens)
    
    return preprocessed_text

def analyze_emotions(strings):
    emotions_count = {
        'joy': 0, 'sadness': 0, 'anger': 0, 'fear': 0, 'surprise': 0,
        'love': 0, 'disgust': 0, 'trust': 0, 'anticipation': 0, 'neutral': 0
    }
    
    for string in strings:
        blob = TextBlob(string)
        sentiment_polarity = blob.sentiment.polarity
        
        if sentiment_polarity > 0.5:
            emotions_count['joy'] += 1
        elif sentiment_polarity < -0.5:
            emotions_count['sadness'] += 1
        elif sentiment_polarity < -0.1:
            emotions_count['anger'] += 1
        elif sentiment_polarity < 0:
            emotions_count['fear'] += 1
        elif sentiment_polarity > 0:
            emotions_count['anticipation'] += 1
        else:
            emotions_count['neutral'] += 1

    total = sum(emotions_count.values())
    emotions_percentage = {key: (value / total) * 100 for key, value in emotions_count.items()}
    return emotions_percentage

try:
     # Initialize the Google Sheets client using service account credentials
    gc = gspread.service_account(filename="JSONDSP.json")

    # Open the specified Google Sheets document
    sheet = gc.open("POSThtML2").worksheet("Sheet2")

    # Retrieve all values in column B as a list
    column_b_values = sheet.col_values(2)

    # Remove empty values from the list (if any)
    column_b_values = [value for value in column_b_values if value]
    # Preprocess each text in the list
    preprocessed_texts = [preprocess_text(text) for text in column_b_values]

    # Analyze emotions in the preprocessed list
    emotions_result = analyze_emotions(preprocessed_texts)

    # Display all the values of emotions
    for emotion, percentage in emotions_result.items():
        print(f"{emotion.capitalize()}: {percentage:.2f}%")

except Exception as e:
    print("An error occurred:", e)
