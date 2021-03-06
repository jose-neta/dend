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
    songplay_id serial PRIMARY KEY,
    start_time bigint NOT NULL, 
    user_id int NOT NULL REFERENCES users (user_id),
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
    start_time bigint,
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
  INSERT INTO public.song_plays(start_time, user_id, song_id, artist_id, level, session_id, location, user_agent)
  VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
  INSERT INTO public.users(user_id, first_name, last_name, gender, level)
  VALUES(%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level;
""")

song_table_insert = ("""
  INSERT INTO public.songs(song_id, title, artist_id, year, duration) 
  VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

artist_table_insert = ("""
  INSERT INTO public.artists(artist_id, name, location, lattitude, longitude)
  VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

time_table_insert = ("""
  INSERT INTO public.time(start_time, hour, day, week, month, year, weekday)
  VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING; 
""")

# FIND SONGS

# get songid and artistid from song and artist tables
song_select = ("""
  SELECT s.song_id, s.artist_id FROM songs s 
    JOIN artists a on s.artist_id = a.artist_id
  WHERE 1 = 1
    AND s.title = %s
    AND a.name = %s
    AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create,
                        artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
