import datetime
import sqlite3

def create_db():
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE blogs (id INTEGER PRIMARY KEY, subject TEXT, content TEXT, created TEXT)")
        print('Blogs table created')
    except:
        print('Blogs table exists.')
    try:
        cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, email TEXT)")
        print('Users table created.')
    except:
        print('Users table exists.')
    con.close()

##### BLOG DB FUNCTIONS #####
def add_entry(subject,content):
    now = datetime.datetime.now() # Get current datetime
    con = sqlite3.connect('blogs.db') # connect to database
    cur = con.cursor() #set cursor
    cur.execute("INSERT INTO blogs (subject,content,created) values (?,?,?)", (subject,content,now))
    print('Database entry added.')
    con.commit()
    con.close()

def del_entry(id):
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    cur.execute("DELETE FROM blogs WHERE id={}".format(id))
    con.commit()
    print('Record {} was deleted from the database.'.format(id))
    con.close()

def get_blogpost(num):
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM blogs WHERE id='+str(num))
    blogpost = cur.fetchone()
    if not blogpost:
        blogpost=(str(num),"Ruh roh","Error: Entry does not exist")
    return blogpost

def get_last_blogpost():
    entryid = get_blogposts()[0][0]
    return get_blogpost(entryid)

def get_blogposts(num=10):
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM blogs ORDER BY created desc limit '+str(num))
    blogposts = cur.fetchall()
    return blogposts

##### USER DB FUNCTIONS #####
def add_user(username,password,email):
    con = sqlite3.connect('blogs.db') # connect to database
    cur = con.cursor() #set cursor
    cur.execute("INSERT INTO users (username,password,email) values (?,?,?)", (username,password,email))
    print('User added.')
    con.commit()
    con.close()

def lookup_user_by_username(username):
    con = sqlite3.connect('blogs.db') # connect to database
    cur = con.cursor() #set cursor
    cur.execute("SELECT * FROM users WHERE username='{}'".format(username))
    result = cur.fetchone()
    con.close()
    return result

def lookup_user_by_id(userid):
    con = sqlite3.connect('blogs.db') # connect to database
    cur = con.cursor() #set cursor
    cur.execute("SELECT * FROM users WHERE id='{}'".format(userid))
    result = cur.fetchone()
    con.close()
    return result


def del_user(username):
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    cur.execute("DELETE FROM users WHERE username='{}'".format(username))
    con.commit()
    print('Record {} was deleted from the database.'.format(username))
    con.close()
