from rauth import OAuth1Service
import billboard
import lyricsgenius
from datetime import timedelta, datetime
from dateutil import rrule
import re
from pymongo import MongoClient
import uuid
import requests


def reformat_song_artist(song_title,artist):
    '''
    The function will clean various aspects of the song title and artist strings.
    Parameters:
        song_title (string): The title of the song.
        artist (string): The artist of the song.
    
    Returns:
        song_title (string)
        artist (string)
    
    '''
    artist=artist.lower()
    song_title=song_title.lower()
    artist=re.sub(r"[ ]and.+",'',artist)
    artist=re.sub(r"[ ]?&.+",'',artist)
    artist=re.sub(r"[ ]feat.+",'',artist)
    artist=re.sub(r"^miss +",'',artist)
    song_title=re.sub(r"[ ]?\(.+\)[ ]?",'',song_title)
    return song_title,artist


def add_song_to_lyric_db(genius_lyrics,artist,unique_id,lyrics_db):
    '''
    This function will add the the genius API's song lyrics dictionary object, the 
    song artist, and the song's unique id to the lyrics database.
    
    Parameters:
        genius_lyrics (lyricsgenius.song.Song object): The returned song object from the
        genius search API.
        artist (string): Artist of the song
        unique_id (string): Unique ID for the song in our song_lookup database
        lyrics_db (pymongo.collection): Collection to store the lyric data
        
    Returns: Nothing
    '''
    temp_dict=genius_lyrics.to_dict()
    temp_dict['artist']=artist
    temp_dict['song_id']=unique_id
    lyrics_db.insert_one(temp_dict)
    

def u_lyric_exists(lyric_db,song_id):
    '''
    This function will look check the lyrics collection to check if the song
    is already in the collection.
    Parameters:
        lyrics_db(pymongo.collection): Collection that holds lyric data.
    
    Returns:
        Song Id (Dict) if the song already exists in the database, otherwise
        None
        
    '''
    try:
        return lyric_db.find({'song_id':song_id})[0]
    except IndexError:
        return None