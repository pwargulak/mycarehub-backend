myCareHub API
==============

Field Reporting Database for the mycarehub care delivery projects.

![Linting and Tests](https://github.com/savannahghi/mycarehub-backend/actions/workflows/ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/savannahghi/mycarehub-backend/badge.svg?branch=main)](https://coveralls.io/github/savannahghi/mycarehub-backend?branch=main)

Environment variables
---------------------

In order to work out the environment variables you need to run this project,
please examine the main CI workflow file - `.github/workflows/ci.yml`. If a
variable is set there, you need it locally too.

Pre-Commit Hooks
-----------------

Code quality checks are run via <https://pre-commit.com/> . You'll have a better
experience if you install Pre-Commit and set up the Git hook.

GPG Signing
------------

As a contributor, you need to sign your commits:
<https://docs.github.com/en/github/authenticating-to-github/managing-commit-signature-verification/signing-commits> .

Running
--------

In order to serve static assets for local development, you need to set up an `npm` development server:

First, you need to install `npm`. We recommend `nvm`: <https://github.com/nvm-sh/nvm> .

```bash
> npm install
> npm run dev
```

Settings
--------

This project was bootstrapped with <https://cookiecutter-django.readthedocs.io/en/latest/>.
The standard settings are documented at <http://cookiecutter-django.readthedocs.io/en/latest/settings.html>.

Setting Up Your Users
---------------------

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

```bash
> python manage.py createsuperuser
```

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar),
so that you can see how the site behaves for both kinds of users.

Bootstrap
---------

The Boostrap CSS is set up for live reloading and SASS compliation.

See:

* <http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html>
* <https://github.com/twbs/bootstrap/blob/v4-dev/scss/_variables.scss>

Email Server
------------

In development, it is often nice to be able to see emails that are being sent from your application.
For that reason local SMTP server <https://github.com/mailhog/MailHog> with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check <https://cookiecutter-django.readthedocs.io/en/latest/> for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open
your browser and go to ``http://127.0.0.1:8025``

Deployment
----------

This application is deployed via Google Cloud Build ( <https://cloud.google.com/build> ) to Google Cloud Run ( <https://cloud.google.com/run> ).
There's a `cloudbuild.yaml` file in the home folder. Secrets (e.g production settings) are managed with Google Secret Manager ( <https://cloud.google.com/secret-manager> ).

Changing OAuth Token Behavior
------------------------------
The following environment variables are available:

```python
ACCESS_TOKEN_EXPIRE_SECONDS = env.int("ACCESS_TOKEN_EXPIRE_SECONDS", default=3600)
ALLOWED_REDIRECT_URI_SCHEMES = env.list("ALLOWED_REDIRECT_URI_SCHEMES", default=["http", "https"])
AUTHORIZATION_CODE_EXPIRE_SECONDS = env.int("AUTHORIZATION_CODE_EXPIRE_SECONDS", default=600)
REFRESH_TOKEN_EXPIRE_SECONDS = env.int("REFRESH_TOKEN_EXPIRE_SECONDS", default=3600)
REFRESH_TOKEN_GRACE_PERIOD_SECONDS = env.int("REFRESH_TOKEN_GRACE_PERIOD_SECONDS", default=600)
```

The indicated defaults can be overidden during deployment by setting those variables.
