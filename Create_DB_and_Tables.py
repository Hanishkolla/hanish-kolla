import sqlite3

conn=sqlite3.connect("Elections2024India.db")
cursor=conn.cursor()
cursor.execute("create table states (state_code varchar(250), state_name varchar(250), primary key(state_code))")
cursor.execute("create table constituencies (constituency_code varchar(250), constituency_name varchar(250),state_code varchar(250), primary key(constituency_code), foreign key(state_code) references states(state_code))")
cursor.execute("create table candidates (candidate_code varchar(250),candidate_name varchar(250),candidate_party varchar(250),status varchar(50),votes_secured int,votes_difference int,constituency_code varchar(250),primary key(candidate_code),foreign key(constituency_code) references constituencies(constituency_code))")

conn.commit()
conn.close()

