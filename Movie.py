import sqlite3

conn = sqlite3.connect("movie.db")

c = conn.cursor()

c.execute("""
CREATE TABLE movies (
    movie_name text,
    lead_actor text,
    lead_actress,
    year_of_release integer,
    director_name text
)
""")
conn.commit()
many_movies = [
    ('KGF chapter 2','Yash','Srinidhi','2022','Prashanth Neel'),
    ('KGF chapter 1','Yash','Srinidhi','2018','Prashanth Neel'),
    ('Ala Vaikunthapurramuloo','Allu Arjun','Pooja Hegde','2020','Trivikram Srinivas'),
    ('Chhichhore','Sushant Singh Rajput','Shraddha Kapoor','2019','Notesh Tiwari')
   ]
c.executemany("INSERT INTO movies VALUES (?,?,?,?,?)",many_movies)
conn.commit()

print("movie_name","\t\t","lead_actor","\t","lead_actress","\t","year_of_release","\t","director_name")
print("--------------","\t\t","----------","\t","----------","\t","----------""\t","-----------")

c.execute("SELECT * FROM movies")
#print(c.fetchall())
items = (c.fetchall())
for item in items:
    print(item[0] + "\t\t" + item[1] + "\t\t" + item[2] + "\t\t" + str(item[3]) + "\t\t" + item[4])
conn.commit()
print("\n")
print("Selection based on the lead actor (Yash)")
c.execute("SELECT DISTINCT movie_name FROM movies where lead_actor = 'Yash'")
list1 = (c.fetchall())
for i in list1:
    print(i[0])
conn.commit()

conn.close()