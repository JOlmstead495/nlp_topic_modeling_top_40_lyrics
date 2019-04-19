import re
import pandas as pd
import numpy as np
import spacy
from sklearn.feature_extraction.text import CountVectorizer

def word_processing(word):
    '''
    This function will perform various cleaning processes on the passed in word and will return 
    a lower case version of that word.
    
    Parameters:
        word (string): The word to get cleaned
    
    Returns:
        word (string)
    
    '''
    word=re.sub(r"\n",' ',word)
    word=re.sub(r"{.+?}",'',word)
    word=re.sub(r"in'",'ing',word)
    return word.lower()

def create_topic_word_cloud(model, feature_names, no_top_words,num_topics,topic_names=None):
    '''
    This function will create a list of the top x number of words per each topic to a list that can be turned
    into a dataframe.
    Parameters:
    model (sklearn, Truncated SVD) : The model that was fit on the data and holds the topic information.
    feature_names (list): The list of words used in the count vectorizer.
    no_top_words (int): Number of topics wanted.
    topic_names (list): The list of topic names to print out, if not passed will be set to None.
    
    Return:
    List of tuples that includes the topic number, the word, and the vector magnitude of the word.
    
    '''
    word_cloud_list=[]
    for ix, topic in enumerate(model.components_[0:num_topics]):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix) 
        else:
            print("\nTopic: '",topic_names[ix],"'")
        word_cloud_list.append('Topic '+str(ix),feature_names[i],topic[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1])
    return word_cloud_list


def display_topics(model, feature_names, no_top_words,num_topics,topic_names=None):
    '''
    This function will print the number of topics and words specificed for each topic.
    
    Parameters:
    model (sklearn, Truncated SVD) : The model that was fit on the data and holds the topic information.
    feature_names (list): The list of words used in the count vectorizer.
    no_top_words (int): Number of topics wanted.
    topic_names (list): The list of topic names to print out, if not passed will be set to None.
    
    Return:
    Nothing
    
    '''
    for ix, topic in enumerate(model.components_[0:num_topics]):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix) 
        else:
            print("\nTopic: '",topic_names[ix],"'")
        temp_string=", ".join(feature_names[i]
                        for i in topic.argsort()[:-no_top_words - 1:-1])
        print(temp_string)