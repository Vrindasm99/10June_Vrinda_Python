from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "vsm123"

# ---------- Database ----------
def init_db():
    conn = sqlite3.connect('taskbuddy.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id INTEGER PRIMARY KEY, title TEXT, desc TEXT, user TEXT, due_date TEXT, status TEXT, admin_status TEXT)''')


    # insert admin if not exists
    c.execute("SELECT * FROM users WHERE username=?", ('admin',))
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  ('admin', 'admin123', 'admin'))

    # insert a sample user
    c.execute("SELECT * FROM users WHERE username=?", ('user1',))
    if not c.fetchone():
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                  ('user1', 'user123', 'user'))
    conn.commit()
    conn.close()

# ---------- Routes ----------
@app.route('/')
def home():
    if 'username' in session:
        if session['role'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('taskbuddy.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['username'] = username
            session['role'] = user[3]  # role column
            flash("Login successful!", "success")
            if user[3] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('dashboard'))
        else:
            flash("Invalid username or password!", "danger")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session and session['role'] == 'user':
        conn = sqlite3.connect('taskbuddy.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks WHERE user=?", (session['username'],))
        tasks = c.fetchall()
        conn.close()
        return render_template('dashboard.html', tasks=tasks)
    return redirect(url_for('home'))

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'username' in session and session['role'] == 'admin':
        conn = sqlite3.connect('taskbuddy.db')
        c = conn.cursor()
        c.execute("SELECT * FROM tasks")
        tasks = c.fetchall()
        c.execute("SELECT * FROM users WHERE role='user'")
        users = c.fetchall()  # get all normal users to assign tasks
        conn.close()
        return render_template('admin_dashboard.html', tasks=tasks, users=users)
    return redirect(url_for('home'))

@app.route('/admin_decision/<int:task_id>/<decision>', methods=['POST'])
def admin_decision(task_id, decision):
    if 'username' in session and session['role'] == 'admin':
        conn = sqlite3.connect('taskbuddy.db')
        c = conn.cursor()
        c.execute("UPDATE tasks SET admin_status=? WHERE id=?", (decision, task_id))
        conn.commit()
        conn.close()
        flash(f"Task {task_id} {decision} successfully!", "success")
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('home'))

@app.route('/upload_task/<int:task_id>', methods=['POST'])
def upload_task(task_id):
    if 'username' in session and session['role'] == 'user':
        conn = sqlite3.connect('taskbuddy.db')
        c = conn.cursor()
        c.execute("UPDATE tasks SET status='Uploaded' WHERE id=? AND user=?", (task_id, session['username']))
        conn.commit()
        conn.close()
        flash(f"Task {task_id} marked as Uploaded!", "success")
        return redirect(url_for('dashboard'))
    return redirect(url_for('home'))


@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' in session and session['role'] == 'admin':
        title = request.form['title']
        desc = request.form['desc']
        user = request.form['user']
        status = request.form['status']
        due_date = "Not Set"  # Simple version; you can add a date input later

        conn = sqlite3.connect('taskbuddy.db')
        c = conn.cursor()
        c.execute("INSERT INTO tasks (title, desc, user, due_date, status) VALUES (?, ?, ?, ?, ?)",
                  (title, desc, user, due_date, status))
        conn.commit()
        conn.close()

        flash(f"Task '{title}' assigned to {user} successfully!")
        return redirect(url_for('admin_dashboard'))
    return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out!", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
