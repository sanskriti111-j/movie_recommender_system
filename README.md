This project is a Content-Based Movie Recommender System that suggests movies based on the similarity of content features. If you've ever wanted a system that recommends movies similar to one you liked — this is it!

Built using feature extraction, data cleaning, and vectorization techniques, this system processes movie data and returns recommendations based on textual similarity. A simple user input (movie title) gives you a list of similar movies you may enjoy!

**Features**
Recommends movies based on a movie you liked.

Uses NLP techniques like Stemming, Tokenization, and Vectorization.

Data cleaning, stop word removal, and feature engineering included.

Built using Python and standard libraries.

Can be deployed or integrated into a movie streaming website or platform




**How It Works**
Data Cleaning: Removed unnecessary columns, null values, and duplicates.

Feature Extraction:

Combined important features like genres, overview, keywords, cast, and crew.

Applied text normalization techniques like lowercasing and punctuation removal.

Text Preprocessing:

Tokenization: Split text into tokens.

Stemming: Reduced words to their root forms (e.g., "playing" → "play").

Removed stop words and irrelevant tokens.

Vectorization:

Used CountVectorizer to convert text into numeric vectors.

Measured similarity using cosine similarity between vectors.

Recommendation Logic:

Takes a movie title as input.

Finds the vector of that movie.

Calculates similarity scores with all other movies.

Returns the top N most similar movies.


**Technologies Used**
Python

Pandas

Numpy

Scikit-learn

NLTK

Streamlit 


 Streaming Website
🖥️ You can try the system live here: https://movierecommendersystem-kq7pvjnnangxhnxxkkm6ml.streamlit.app/

