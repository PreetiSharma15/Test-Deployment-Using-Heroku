import numpy as np
import pandas as pd
import csv
from PIL import Image

from datetime import datetime
from datetime import date


import tensorflow as tf

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

from tensorflow.keras.models import load_model

def prediction():

    train_data = pd.read_csv("tweet_emotions.csv")
    train_data.head()

    training_sentences = []

    for i in range(len(train_data)):
        sentence = train_data.loc[i, "content"]
        training_sentences.append(sentence)


    model = load_model("Tweets_Text_Emotion.h5")

    vocab_size = 40000
    max_length = 100
    trunc_type = "post"
    padding_type = "post"
    oov_tok = "<OOV>"
    
    tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
    tokenizer.fit_on_texts(training_sentences)


    sentence = ["Today I went out for shopping", "It was very boring today"]


    sequences = tokenizer.texts_to_sequences(sentence)


    padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    testing_padded = np.array(padded)

    predicted_class_label = np.argmax(model.predict(testing_padded), axis=-1)
    return predicted_class_label
            