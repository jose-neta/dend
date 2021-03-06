import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """Reads a json file from the song_data folder.

    Reads information of songs and artists and saves them to songs and
    artists tables in the database.

    Parameters:
        cur: DB cursor

    Returns:
        None
    """

    # open song file
    df = pd.read_json(filepath, typ='series')

    # insert song record
    song_data = [df.values[6], df.values[7],
                 df.values[1], df.values[9], df.values[8]]
    cur.execute(song_table_insert, song_data)

    # insert artist record
    artist_data = [df.values[6], df.values[7],
                   df.values[1], df.values[9], df.values[8]]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    """Reads a json file from the log_data folder.

    Filters all songs logs, reads information of artist, time occurence
    and user playing the song and save them to song_plays and time tables
    in the database.

    Parameters: 
        cur: DB cursor
        filepath (str): file path for log file

    Returns:
        None
    """

    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    is_song = df['page'] == 'NextSong'
    df = df[is_song]

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')

    # insert time data records
    time_data = (df['ts'].tolist(), t.dt.hour.tolist(), t.dt.day.tolist(),
                 t.dt.dayofweek.tolist(), t.dt.month.tolist(),
                 t.dt.year.tolist(), t.dt.dayofweek.tolist())
    column_labels = ("timestamp", "hour", "day",
                     "week", "month", "year", "weekday")
    dictionary = dict(zip(column_labels, time_data))
    time_df = df.from_dict(dictionary, orient='columns')

    for i, row in time_df.iterrows():
        print(row)
        cur.execute(time_table_insert, list(row))

    # load user table
    user_data = (df.userId.tolist(), df.firstName.tolist(), df.lastName.tolist(),
                 df.gender.tolist(), df.level.tolist())
    column_labels = ("user_id", "first_name", "last_name", "gender", "level")
    dictionary = dict(zip(column_labels, user_data))
    user_df = time_df = df.from_dict(dictionary, orient='columns')

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        results = cur.execute(song_select, (row.song, row.artist, row.length))
        songid, artistid = results if results else None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, songid, artistid,
                         row.level, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    """Process a directory of files.

    Walk through all files inside each sub directory 
    of given root directory given and process each file 
    with the given `func` callback.

    Parameters: 
        cur: DB cursor
        conn: DB connection
        filepath (str): file path directory containing json files
        func: callback which will process the files

    Returns:
        None
    """

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    """Does ETL files.

    Given two root directories of data in json format, namely log and 
    songs data, will load them onto a Database after transforming them 
    in a suitable format.

    Parameters: None
    Returns: None
    """
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
