# Twister
Twitter clone built with Django and Bootstrap

## Requirements

* Python 3.7+
* Postgres

## Quick start

1. Create your virtual environment. I totally recommend to user [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) because of its simplicity. Once you've installed it, you can start typing the following:

    ```sh
    $ mkvirtualenv twister
    ```

    When you already have your virtual environment created, you can deactivate it like this:

    ```sh
    $ deactivate
    ```

    And, if you wanna activate it again:

    ```sh
    $ workon twister
    ```

2. Install requirements from your virtual env, like this.

    First, move to project's directory

    ```sh
    $ cd twister_project
    ```

    Now, install all your dependencies

    ```sh
    $ pip install -r requirements/local.txt
    ```

3. Now, you must set the following environmental variables

    * PYTHON_PATH: This must be the absolute path to this project
    * DJANGO_SETTINGS_MODULE: config.settings.local for default development settings
    * SECRET_KEY: You won't be able to run a server without a secret key
    * DEBUG: If not set, you won't be able to see debugging options
    * DATABASE_URL:  Something like this *postgres://postgres:postgres@localhost:5432/twister*

    > You can start these variables in your postactivate script if you are using virtualenvwrapper, but remember to unset them in your predeactivate script.

4. Finally, you can start typing the following:
    

    ```sh
    $ django-admin makemigrations
    $ django-admin migrate
    $ django-admin runserver
    ```

5. It's done!

    If you are running into problems, you can send me an email at mauricio@klatus.com
