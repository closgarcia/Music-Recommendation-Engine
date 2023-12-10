# app.py
import os
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
import opendatasets as od

# Set Kaggle credentials (replace with your own)
os.environ['KAGGLE_USERNAME'] = 'closgarcia'
os.environ['KAGGLE_KEY'] = '2131ed1a4491e91b3fd6d40e6c718556'

# Download Kaggle dataset
dataset_url = 'https://www.kaggle.com/datasets/yamaerenay/spotify-dataset-19212020-600k-tracks'
od.download(dataset_url)
dataset = './spotify-dataset-19212020-600k-tracks'
tracks_df = pd.read_csv(dataset + '/tracks.csv')
artists_df = pd.read_csv(dataset + '/artists.csv')

# Merge dataframes based on 'id_artists'
merged_df = pd.merge(tracks_df, artists_df, left_on='id_artists', right_on='id', how='left')

# Drop unnecessary columns
merged_df = merged_df.drop(columns=['id_x', 'id_y', 'followers', 'genres', 'name_y'])

# Handle missing values if any
merged_df = merged_df.dropna()

# Merge relevant columns based on common keys ('id_artists' column)
merged_df = pd.merge(tracks_df, artists_df, left_on='id_artists', right_on='id', how='left')

# Convert lists in 'id_artists' column to tuples
tracks_df['id_artists'] = tracks_df['id_artists'].apply(tuple)

# Now, you can get unique values
unique_id_artists = tracks_df['id_artists'].unique()


# Convert lists in 'id_artists' column to tuples
tracks_df['id_artists'] = tracks_df['id_artists'].apply(lambda x: tuple(x) if isinstance(x, list) else (x,))

# Keep only the first artist ID in tuples with multiple elements
tracks_df['id_artists'] = tracks_df['id_artists'].apply(lambda x: x[0])

# Now, you can get unique values
unique_id_artists = tracks_df['id_artists'].unique()


tracks_df['release_date'] = pd.to_datetime(tracks_df['release_date'])
tracks_df['year'] = tracks_df['release_date'].apply(lambda time: time.year)
# Define features
features = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy',
            'explicit', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
            'popularity', 'speechiness', 'tempo']

def input_preprocessor(song_list, tracks_df, features):
    # Implementation of input_preprocessor function (Assumed)
    song_vectors = []

    for song in song_list:
        try:
            song_data = tracks_df[(tracks_df['name'] == song['name']) &
                                (tracks_df['year'] == song['year'])].iloc[0]

        except IndexError:
            song_data = None

        if song_data is None:
            print(f'Warning: {song["name"]} from {song["year"]} not found in the dataset.')
            continue

        song_vectors.append(song_data[features].values)

    return np.array(song_vectors)

def Music_Recommender(song_list, tracks_df, n_songs=10):
    # Implementation of Music_Recommender function (Assumed)
    song_vectors = input_preprocessor(song_list, tracks_df, features)

    if song_vectors.size == 0:
        st.warning("No matching songs found. Please try different input.")
        return pd.DataFrame()

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(tracks_df[features])
    scaled_song_center = scaler.transform(song_vectors.reshape(1, -1))

    ed_dist = euclidean_distances(scaled_song_center, scaled_data)

    index = list(np.argsort(ed_dist)[:,:n_songs][0])
    rec_output = tracks_df.iloc[index]

    return rec_output[['name', 'year', 'artists', 'popularity']]


def user_input():
    # Prompt the user to enter the song name
    song_name = st.text_input("Enter the song name:")

    # Prompt the user to enter the song year
    song_year = st.number_input("Enter the song year:", value=2020, min_value=1921, max_value=2020, step=1)
    
    return {'name': song_name, 'year': int(song_year)}


#def user_input():
    # Prompt the user to enter the song name
    #song_name = st.text_input("Enter the song name:")

    # Prompt the user to enter the song year
    #song_year = st.number_input("Enter the song year:", value=2020, min_value=1921, max_value=2020)
    #song_year = st.int(input("Enter the song year: "))
   # return {'name': song_name, 'year': int(song_year)}
    ###
def user_input():
    # Prompt the user to enter the song name
    song_name = st.text_input("Enter the song name:")

    # Prompt the user to enter the song year
    song_year = st.number_input("Enter the song year:", value=2020, min_value=1921, max_value=2020)

    return {'name': song_name, 'year': int(song_year)}

def display_recommendations(results):
    # Display recommendations in a nice format
    st.title('Music Recommender')
    st.write("Recommendations based on your input:")
    
    if not results.empty:
        # Use a table to display the recommendations
        st.table(results)
    else:
        st.warning("No matching songs found. Please try different input.")

if __name__ == '__main__':
    # Get user input
    user_song = user_input()

    # Generate recommendations based on user input
    results = Music_Recommender([user_song], tracks_df)

    # Drop duplicates based on 'name' and 'year'
    results = results.drop_duplicates(subset=['name', 'year'])

    # Display recommendations in Streamlit app
    display_recommendations(results)

