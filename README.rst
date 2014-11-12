What is it?
===========

Django testing application

Based on PyDanny guidelines found in 2 scoops of django: Best practices for Django 1.6.

Summary
=======

1. prerequisites
1. create a virtual environment
1. use the virtual environment
1. install requirements
1. Run the server

prerequisites
=============

This tutorial is based on python3.

    # aptitude install python3

You must install either virtualenv or virtualenvwrapper

Install virtualenv
------------------

- install virtualenv

    # pip install virtualenv

Install virtualenvwrapper
-------------------------

- install virtualenvwrapper

    # pip install virtualenvwrapper

- Add this 3 lines at the end of ~/.bashrc

    export WORKON_HOME = /.virtualenvs
    mkdir -p $WORKON_HOME
    source ~/.local/bin/virtualenvwrapper.sh

Create a virtual environment
============================

When using virtualenv, you may want to create a virtual environment for each project

- with virtualenv

    $ virtualenv -p python3 my_virtualenv_name

- with virtualenvwrapper

    $ mkvirtualenv -p python3 my_virtualenv_name

Using virtual environment
=========================

Each time you want to use the project, you must use the virtual environment

- with virtualenv

    $ source my_virtualenv_name/bin/activate

- with virtualenvwrapper

    $ workon your_virtual_env_name

Install requirements
====================

In order to use your project for the first time, you must install all requirements

    $ pip install -r requirements/base.txt

How to run the Server
=====================

Now, run the server and enjoy it !

    $ ./manage.py runserver
