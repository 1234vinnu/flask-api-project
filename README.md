Flask API Project Documentation
1. Setup and Running the Application
1.1. Prerequisites
    You need Python 3.11 and pip installed.

1.2. Environment Setup
	1	Clone the Repository: git clone [https://github.com/1234vinnu/flask-api-project.git](https://github.com/1234vinnu/flask-api-project.git)
		cd flask-api-project
  2 Create and Activate Virtual Environment: python3 -m venv venv
		source venv/bin/activate  # On macOS/Linux
		# venv\Scripts\activate   # On Windows

  3.Install Dependencies: (Assuming your dependencies are listed in a requirements.txt file)
	  pip install -r requirements.txt
1.3. Running the Server
	  Start the Flask development server. It will run on http://127.0.0.1:5000/.
	  flask run


2. Database and Schema
2.1. Database Schema (users table)
    This application uses a single table for user registration.
   
   Field Name                 Datatype                       Description                          Constraints
    id                          Integer                       Unique identifier                     Primary Key
    name                       VARCHAR(45)                    User's unique name.                   Unique, Not Null      
    email                      VARCHAR(45)                    User's unique email address.          Unique, Not Null

2.2. Database Setup and Population
The application is configured to connect to your local MySQL database (assuming connection details are in app.py).
Set your Database details in app.py file.
	DB_CONFIG = {
		    'user': 'root',    // Here Database User Id to enter.
		    'password': '240424',   //Database User Password to enter.
		    'host': '127.0.0.1', 		//Host Address URL
		    'database': 'users' 		//Database table name
		}
SQL Queries: 1.) SELECT id, name, email, role FROM users
			 2.) INSERT INTO users (name, email, role) VALUES (%s, %s, %s)
			 3.) SELECT id, name, email, role FROM users WHERE id = %s
		
3. Git Workflow and Contribution
This project follows the Feature Branch Workflow to manage contributions.
3.1. Contribution Steps
	1	Sync Local Main: Ensure your local main branch is up-to-date with the remote main. git checkout main
	2	git pull origin main

  3      Create a assignment Branch: Create a branch for your specific task. git checkout -b assignment
  4     Commit Changes: Implement your features, making small, descriptive commits. 	git add .

  5   git commit -m "feat: Add new model for user profile."

  6      Push and Open PR: Push your feature branch to the remote repository. 	 git push -u origin feature/new-task

  7      Create Pull Request (PR): Go to GitHub, create a PR from your new branch (assignment) targeting the main branch.
  8       Review and Merge: Wait for review (if applicable). Once approved, merge the PR to incorporate your changes into the main codebase.
