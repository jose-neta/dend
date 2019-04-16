# DEND - Project 1

## Discussion

### On `time` table

Yes that's it, there can be duplicated `timestamps` for `song_plays`. Two different users
can be listening musice at the same start time, hence after removing the primary key for 
`time.start_time` and also removing the reference to it on `song_plays` table the 
diagram for the star schema changed a tad.

#### before removing PK

![before](start_before_removing_pk.png | width=250)

#### after removing PK

![after](start_after_removing_pk.png | width=250)

### There are no songplays

TODO Need to elaborate on this one

## On `song_plays` table

`etl.py` from 6820 records has all (`song_id`, `artist_id`) equal to `NULL`, that means that there is no match between `data/song files` and the log files.