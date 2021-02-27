from flask import Flask, render_template, request, redirect
import sqlite3
from flask import g

DATABASE = 'muz.db'
app = Flask(__name__)


def connect_db():
    return sqlite3.connect(DATABASE)


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()


@app.route('/')
def index():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM songs")

    songs = cursor.fetchall()
    return render_template('index.html', songs=songs)


@app.route('/add_song/', methods=['GET', 'POST'])
def add_song():
    connection = connect_db()
    if request.method == 'POST':
        query = f"INSERT INTO songs (name, artist, duration) VALUES ('{request.form['name']}','{request.form['artist']}'," \
                f"'{request.form['duration']}')"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return redirect('/')
    return render_template('add_song.html')


@app.route('/delete_song/', methods=['GET', 'POST'])
def delete_song():
    connection = connect_db()
    if request.method == 'POST':
        query = f"DELETE FROM songs WHERE id={request.form['song_id']}"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)

