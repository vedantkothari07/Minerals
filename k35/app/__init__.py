"""
JAVA: Aidan Wong, Vedant Kothari
SoftDev
K35: Now Again for the First Time
2024-03-12
Time Spent: 2
"""

from flask import Flask, request, redirect, url_for, render_template, session
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(32)

# Database setup
def init_db():
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS stories (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL,
                        author TEXT NOT NULL)''')
        c.execute('''CREATE TABLE IF NOT EXISTS contributions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        story_id INTEGER NOT NULL,
                        username TEXT NOT NULL,
                        contribution TEXT NOT NULL,
                        FOREIGN KEY(story_id) REFERENCES stories(id),
                        FOREIGN KEY(username) REFERENCES users(username))''')
        conn.commit()

init_db()

@app.route('/')
def landing_page():
    if 'username' in session:
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('''SELECT DISTINCT stories.title 
                         FROM stories 
                         JOIN contributions ON stories.id = contributions.story_id 
                         WHERE contributions.username = ?''', (session['username'],))
            user_stories = [row[0] for row in c.fetchall()]

            c.execute('''SELECT title FROM stories 
                         WHERE id NOT IN (SELECT story_id FROM contributions WHERE username = ?)''', (session['username'],))
            available_stories = [row[0] for row in c.fetchall()]

        return render_template('index.html', user_stories=user_stories, available_stories=available_stories)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username = ?', (username,))
            if c.fetchone() is None:
                c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
            if c.fetchone():
                session['username'] = username
                return redirect(url_for('landing_page'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/create_story', methods=['GET', 'POST'])
def create_story():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO stories (title, content, author) VALUES (?, ?, ?)', (title, content, session['username']))
            story_id = c.lastrowid
            c.execute('INSERT INTO contributions (story_id, username, contribution) VALUES (?, ?, ?)', (story_id, session['username'], content))
            conn.commit()
        return redirect(url_for('landing_page'))
    return render_template('create_story.html')

@app.route('/contribute/<story_title>', methods=['GET', 'POST'])
def contribute(story_title):
    with sqlit1434e3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT id, content FROM stories WHERE title = ?', (story_title,))
        story = c.fetchone()
        if not story:
            return redirect(url_for('landing_page'))
        story_id, story_content = story
        c.execute('SELECT * FROM contributions WHERE story_id = ? AND username = ?', (story_id, session['username']))
        if c.fetchone():
            return redirect(url_for('landing_page'))
        latest_update = story_content
        c.execute('SELECT contribution FROM contributions WHERE story_id = ? ORDER BY id DESC LIMIT 1', (story_id,))
        latest_contribution = c.fetchone()
        if latest_contribution:
            latest_update = latest_contribution[0]

    if request.method == 'POST':
        contribution = request.form['contribution']
        with sqlite3.connect('database.db') as conn:
            c = conn.cursor()
            c.execute('INSERT INTO contributions (story_id, username, contribution) VALUES (?, ?, ?)', (story_id, session['username'], contribution))
            c.execute('UPDATE stories SET content = content || " " || ? WHERE id = ?', (contribution, story_id))
            conn.commit()
        return redirect(url_for('landing_page'))

    return render_template('contribute.html', story_title=story_title, latest_update=latest_update)

@app.route('/story/<story_title>')
def view_story(story_title):
    with sqlite3.connect('database.db') as conn:
        c = conn.cursor()
        c.execute('SELECT content FROM stories WHERE title = ?', (story_title,))
        story = c.fetchone()
        if not story:
            return redirect(url_for('landing_page'))
        contributions = [row[0] for row in c.execute('SELECT contribution FROM contributions WHERE story_id = (SELECT id FROM stories WHERE title = ?) ORDER BY id', (story_title,))]
        story_content = " ".join([contribution if contribution[-1] in '.!?;' else contribution + '.' for contribution in contributions])
        c.execute('SELECT contribution FROM contributions WHERE story_id = (SELECT id FROM stories WHERE title = ?) ORDER BY id', (story_title,))
        contributions = [row[0] for row in c.fetchall()]
    return render_template('view_story.html', story_title=story_title, story_content=story_content, contributions=contributions)

if __name__ == '__main__':
    app.run(debug=True)