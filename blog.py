from bottle import route, run, request, redirect, template, static_file
import datetime
import sqlite3

def create_db():
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE blogs (id INTEGER PRIMARY KEY, subject TEXT, content TEXT, created TEXT)")
        print('Database created.')
    except:
        print('Database exists.')
    con.close()

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

def render_newpost(subject="",content="",error=""):
    return template('newpost', subject=subject, content=content, error=error)

def render_blog(blogposts=""):
    return template('blog', blogposts=blogposts)

def get_blogposts(num=10):
    con = sqlite3.connect('blogs.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM blogs ORDER BY created desc')
    blogposts = cur.fetchall()
    blogposts = blogposts[:num]
    return blogposts

@route('/blog', method='GET')
def blog():
    blogposts = get_blogposts()
    return render_blog(blogposts)

@route('/blog', method='POST')
def blog():
    pass

@route('/newpost', method='GET')
def newpost():
    return render_newpost()

@route('/newpost', method='POST')
def newpost():
    user_subject = request.POST.get('subject')
    user_content = request.POST.get('content')

    if not (user_subject and user_content):
        error="You done goofed."
        return render_newpost(user_subject,user_content, error)
    else:
        add_entry(user_subject,user_content)
        return redirect('blog')

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

create_db()

run(host='0.0.0.0', port=8080)
