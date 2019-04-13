# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_plays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

# fact table
songplay_table_create = ("""
  CREATE TABLE song_plays(
    songplay_id int PRIMARY KEY, 
    start_time bigint REFERENCES time (start_time), 
    user_id int REFERENCES users (user_id),
    song_id text REFERENCES songs (song_id),
    artist_id text REFERENCES artists (artist_id),
    level text,
    session_id int,
    location text,
    user_agent text);
""")

# dim table
user_table_create = ("""
  CREATE TABLE users(
    user_id int PRIMARY KEY,
    first_name text,
    last_name text,
    gender char,
    level text);
""")

# dim table
song_table_create = ("""
  CREATE TABLE songs(
  	song_id text primary key,
  	title text,
  	artist_id text,
  	year int,
  	duration DECIMAL(13,6)
  );
""")

# dim table
artist_table_create = ("""
  CREATE TABLE artists(
  	artist_id text primary key,
  	name text,
  	location text,
  	lattitude DECIMAL(13,6),
  	longitude DECIMAL(13,6)
  );
""")

# dim table
time_table_create = ("""
  CREATE TABLE time(
    start_time bigint primary key,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
  );
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
  INSERT INTO public.songs(song_id, title, artist_id, year, duration) 
  VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
  INSERT INTO public.artists(artist_id, name, location, lattitude, longitude)
  VALUES(%s, %s, %s, %s, %s);
""")

time_table_insert = ("""
  INSERT INTO public.time(start_time, hour, day, week, month, year, weekday)
  VALUES(%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]