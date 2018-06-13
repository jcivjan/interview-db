[![Build Status](https://travis-ci.org/uw-it-aca/interview_db.svg?branch=0.0.0.b3)](https://travis-ci.org/uw-it-aca/interview_db)
[![Coverage Status](https://coveralls.io/repos/github/uw-it-aca/interview_db/badge.svg?branch=master)](https://coveralls.io/github/uw-it-aca/interview_db?branch=master)
# interview_db

App to collect and tag interview data, artifacts, and stories for publishing using the Django Admin app.

Prerequisites

    A Python installation (2.5 or greater)
    pip or easy_install
    git

Step-by-step

    If you don't have it already, install virtualenv:

    $ pip install virtualenv

    if you don't have pip, you may be able to:

    $ easy_install virtualenv

Checkout the master of the interview_db project:

    $ git clone git@github.com:jcivjan/interview_db.git

    OR https://github.com/jcivjan/interview_db.git
    
Turn interview_db into a virtualenv:

    $ virtualenv gradepage   

Activate your virtualenv:

    cd interview_db
    source bin/activate
    
Install required Python packages with pip:

    $ pip install -r requirements.txt

Create a django project in the interview_db dir:

    $ django-admin.py startproject project .

    That '.' at the end is important!

Modify at least the following settings in interview_db/settings.py:

    Add to your INSTALLED_APPS:

        'interview_db',

Create the intervies-db database

    $ python manage.py migrate

You should now be able to run your development server:

    $ python manage.py runserver 0.0.0.0:<your port>


