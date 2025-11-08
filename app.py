from flask import Flask, render_template, request, redirect, url_for

# Import the MySQL Connector for database interaction
import mysql.connector

# Initialize the Flask application
app = Flask(__name__)

DB_CONFIG = {
    'user': 'root',
    'password': '240424',
    'host': '127.0.0.1',
    'database': 'users' 
}

def get_db_connection():
    """Helper function to get a database connection."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None
    



# --- Routes Implementation ---

# 1.Route /hello
@app.route('/hello')
def hello_world():
    return "Hello World!"

# 2. Route /users
@app.route('/users')
def list_users():
    """Retrieves a list of users and displays them as an HTML table."""
    conn = get_db_connection()
    if conn is None:
        return "Database Connection Error", 500
        
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email, role FROM users") 
    users = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    # You will need to create a 'users.html' file in a 'templates' folder.
    return render_template('users.html', users=users)

# 3. Route /new_user
from flask import flash 

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    """Renders a form to accept user input and stores the information."""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        
        conn = get_db_connection()
        if conn is None:
            return "Database Connection Error", 500
            
        cursor = conn.cursor()
        insert_query = "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)"
        user_data = (name, email, role)
        
        try:
            cursor.execute(insert_query, user_data)
            conn.commit()
            return redirect(url_for('list_users')) 
        except mysql.connector.Error as err:
            conn.rollback()
            flash(f"Error inserting user: {err}")
            return redirect(url_for('new_user')) 
        finally:
            cursor.close()
            conn.close()
            
    return render_template('new_user.html')


# 4.Route /users/<id>

@app.route('/users/<int:user_id>')
def user_details(user_id):
    conn = get_db_connection()
    if conn is None:
        return "Database Connection Error", 500

    cursor = conn.cursor(dictionary=True)
    select_query = "SELECT id, name, email, role FROM users WHERE id = %s"
    
    cursor.execute(select_query, (user_id,))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user is None:
        return "User not found", 404 
    return render_template('user_detail.html', user=user)

# ... Your route code will go here ...





if __name__ == '__main__':
    # You can set debug=True during development
    app.run(debug=True)