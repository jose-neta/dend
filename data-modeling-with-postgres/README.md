# DEND - Project 1

## Discussion

### On `time` table and on timestamps being duplicated

Note that I'm assuming that timestamps are uniques, and that's why the column `timestamp` from 
`time` table is primary key and the `time_table_insert` query is `doing nothing` on conflict.
What all this means is that I'm ignoring every subsequents duplicated timestamps. 

In conclusion I think that I should instead **not assume** that timestamps are unique but instead 
allow for duplicated timestamps and for that I should remove the `primary key` constraint on `time` table.

Loading data onto `time` table I found that there is 2 duplicated timestamps `1542984111796`. Here are the 
duplicated timestamps found on file `data/log_data/2018/11/2018-11-23-events.json`.

```
Line 119:{"artist":"Shawn McDonald","auth":"Logged In","firstName":"Devin","gender":"M","itemInSession":0,"lastName":"Larson","length":358.89587,"level":"free","location":"Tampa-St. Petersburg-Clearwater, FL","method":"PUT","page":"NextSong","registration":1541045604796.0,"sessionId":765,"song":"Lovely","status":200,"ts":1542984111796,"userAgent":"Mozilla\/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko\/20100101 Firefox\/31.0","userId":"60"}
Line 120:{"artist":"El Cuarteto De Nos","auth":"Logged In","firstName":"Avery","gender":"F","itemInSession":2,"lastName":"Watkins","length":241.44934,"level":"paid","location":"San Jose-Sunnyvale-Santa Clara, CA","method":"PUT","page":"NextSong","registration":1540871783796.0,"sessionId":691,"song":"Invierno Del 92","status":200,"ts":1542984111796,"userAgent":"Mozilla\/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko\/20100101 Firefox\/31.0","userId":"30"}
```

### There are no songplays

TODO Need to elaborate on this one
