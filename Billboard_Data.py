from rauth import OAuth1Service
import billboard
import lyricsgenius
from datetime import timedelta, datetime
from dateutil import rrule
import re
from pymongo import MongoClient
import uuid
import requests



def add_unique_song(song_lookup_db,song,artist):
    '''
    The function will check if a unique id already exists in the song lookup database
    if it does it will return it, if not it will add the song with a new unique id in the database.
    
    Parameters:
        song_lookup_db (pymongo.collection): The song lookup database within mongo that
        will store the unique song id and song information.
        song (string): The title of the song to lookup.
        artist (string): The artist of the song to lookup.
        
    Return:
        (String) unique id
    
    '''
    uniq_id=uniq_song_id_exists(song_lookup_db,song,artist)
    if uniq_id==None:
        uniq_id=uuid.uuid4().hex
        song_lookup_db.insert_one({'_id':uniq_id,'title':song,'artist':artist})
    return uniq_id



def store_billboard_data(song_lookup_db,billboard_db,billboard_data,date):
    '''
    The function will search the Billboard Top 100 API given a specific date, 
    and will save each unique song to the song lookup database. It will
    also save the ranked list along with the date and year of the billboard top 100.
    
    Parameters:
        song_lookup_db (pymongo.collection): The song lookup database within mongo that
        will store the unique song id and song information.
        billboard_db (pymongo.collection): The billboard database within mongo that stores
        the billboard top 40 ranks.
        billboard_data (billboard.ChartData): The weekly chart data from the billboard API.
        date (datetime.datetime): The datetime object that contains the date you want to search
    
    Returns:
        Nothing
    
    '''
    song_title_regex_space=re.compile(r"[ ]?\(.+\)[ ]?")
    bboard_rank_dict={'date':date.strftime('%Y-%m-%d'),'year':date.year}
    temp_rank_list=[]
    for i,x in enumerate(billboard_data[0:40]):
        song_title=re.sub(song_title_regex_space,'',x.title).lower()
        artist_name=x.artist.lower()
        uniq_id=add_unique_song(song_lookup_db,song_title,artist_name)
        temp_rank_list.append({'rank':i+1,'songId':uniq_id})
    bboard_rank_dict['Rank_List']=temp_rank_list
    billboard_db.insert_one(bboard_rank_dict)
    

    
def uniq_song_id_exists(song_lookup_db,song,artist):
    '''
    The function will check if the song's unique ID already exists and will return it.
    
    Parameters:
        song_lookup_db (pymongo.collection): The song lookup database within mongo that
        will store the unique song id and song information.
        song (string): The title of the song to lookup.
        artist (string): The artist of the song to lookup.
        
    Returns:
        If the song is already in the song lookup database return the unique Id,
        otherwise return None.
    
    '''
    try:
        return song_lookup_db.find({'title':song,'artist':artist},{})[0]
    except IndexError:
        return None