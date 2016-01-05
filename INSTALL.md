#Installation Instructions (http://einsteinish.com)

*Make sure you have Python 2.7.6, virtualenv, pip and sqlite3 installed*

1. Download or clone this repo.

2. Go to project home folder and run these commands:

    cp einsteinish/example_local.py einsteinish/local_settings.py
    virtualenv venv
    source venv/bin/activate

3. This will create a virtual environment and activate it. Now use pip to install dependencies with:

    pip install -r dev-requirements.txt
    
    (note) May need to install postgresql-server, postgresql-devel

4. Now we have to prepare a database:

    python manage.py syncdb

5. It will ask us to provide username, email and password. Give them and run following migrations:

    python manage.py migrate guardian
    python manage.py migrate resources
    python manage.py migrate profiles

5. Run django server and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (dev only)

6. Create Resource Types.

7. To access MySQL from local machine : ssh -L 9001:localhost:80 -l sfvue 45.79.90.218
   Use localhost:9001/phpmyadmin 

