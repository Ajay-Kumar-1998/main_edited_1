# Local Setup
- Clone the project
- Run `pip install -r requirements.txt` to install all dependencies

# Local Development Run
- `python main.py` It will start the flask app in `development`. Suited for local development. 

# Replit run
- Go to shell and run
    `pip install --upgrade poetry`
- Click on `main.py` and click button run
- The web app will be availabe at https://appName.userName.repl.co
- Format https://<replname>.<username>.repl.co

# Folder Structure

- `final_project.sqlite3` is the sqlite DB. It can be anywhere on the machine. Adjust the path in `__init__.py`. This app ships with one required for testing.
- `/` is where our application code is
- `static` - default `static` files folder. It serves at '/static' path.
- `templates` - Default flask templates folder
 

```
root folder/
├── main.py
├── requirements.txt
├── readme.md
├── main_folder/
    |── database_folder/
    ├── static/
    	|__css/
    	|__images/
    		|__logo.png
    |__templates/
    	|__dashboard.html
    	|__home_page.html
    	|__login.html
    	|__register.html
    	|__review.html
    ├── __init.py
    ├── api.py
    ├── controllers.py
    ├── final_project.sqlite3
    |__ models.py



```