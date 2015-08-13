# Sudoku Web Application
A basic Sudoku Solver

### Introduction
This is a basic Sudoku Solver based on Python and developed with Flask.



### Getting Started <a name="getting-started"></a>
#### System Requirements <a name="system-requirements"></a>
1. [Python](https://www.python.org/downloads/)(v2.7+) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.

#### Setup <a name="environment-setup"></a>
1. [Fork](https://github.com/stormpython/insightfl/fork) the project and clone the repository.

  **Note:** It is helpful to change the repository name **before** cloning. In Github, click on `Settings` on the right-hand
  side of your screen. Within the Settings box at the top of the screen, rename the repository and click `Rename`.

  ```
  git clone git@github.com:<username>/<project>.git
  ```

2. **Recommended:** Install virtualenv and fire up a virtual environment.

  ```
  # cd into your InsightFL project folder
  # Install virtualenv
  sudo pip install virtualenv

  # Create virtualenv folder `venv`
  virtualenv venv

  # Activate the virtual environment
  source venv/bin/activate
  ```

3. Install Python project dependencies.

  ```
  pip install -r requirements.txt
  ```

4. To test your application, run the manage.py file: `python manage.py runserver`, and open your web browser to
`localhost:5000`.

That's it! You are ready to start building your web application.

**Note**: *`manage.py` uses the builtin server for development. You should not use the builtin development server
in production (i.e. when you're launching your web application). To run in production, use `gunicorn manage:app` at
the command line.*

### Application Structure
#### Philosophy
InsightFL's project layout mimics that of large Flask applications. This is done intentionally. Despite the
fact that most Insight projects are small applications, utilizing this structure allows you to separate your development 
concerns more effectively. Instead of having all your web app code in one file, it can be broken up into separate, 
smaller chunks, which makes for cleaner code and easier debugging.

#### Project Layout
- **[app](app)** - Where your Flask web application lives. This is where you'll spend the majority of your time
- **.gitignore** - [Git ignore file](https://help.github.com/articles/ignoring-files)
- **config.py** - Project configuration file for storing sensitive or dynamic settings, e.g. database settings 
- **LICENSE.md** - Project license
- **manage.py** - Entry point to your Flask application during development, click [here](http://flask-script.readthedocs.org/en/latest/) for more info.
- **README.md** - You're looking at it! :)
- **requirements.txt** - Tracks all your Python dependencies using [pip](http://pip.readthedocs.org/en/latest/user_guide.html#requirements-files)
- **schema.sql** - Your SQL database schemas

