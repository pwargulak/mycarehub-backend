"""Package setup."""
from setuptools import find_packages, setup

name = "mycarehub_django"

setup(
    name=name,
    version="0.0.17",
    packages=find_packages(exclude=["tests", "tests.*"]),
    description="Field Reporting Database for the mycarehub care delivery projects.",
    long_description="Description",
    url="https://github.com/savannahghi/mycarehub-backend",
    author="SIL",
    author_email="developers@savannahinformatics.com",
    license="MIT License",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    include_package_data=True,
    install_requires=[
        "psycopg2-binary~=2.9.1",
        "Fraction~=2.1.1",
        "Pillow~=8.4.0",
        "argon2-cffi~=21.1.0",
        "coveralls~=3.3.0",
        "django-extensions~=3.1.3",
        "django-allauth~=0.45.0",
        "django-anymail[mailgun]~=8.4",
        "django-compressor~=2.4.1",
        "django-cors-headers~=3.10.0",
        "django-crispy-forms~=1.13.0",
        "django-environ~=0.8.1",
        "django-filter>=2.2,<3.0",
        "django-mjml[requests]~=0.11.0",
        "django-taggit~=1.5.1",
        "django-modelcluster~=5.2",
        "django-model-utils~=4.2.0  ",
        "django-oauth-toolkit~=1.5.0",
        "django-phonenumber-field~=5.2.0",
        "django-storages[google]~=1.12.3  ",
        "djangorestframework-datatables~=0.6.0",
        "djangorestframework~=3.12.4  ",
        "django-rest-framework-braces~=0.3.4",
        "drf-generators~=0.5.0",
        "django~=3.2.6",
        "google-api-core~=2.2.2",
        "google-api-python-client~=2.29.0",
        "google-auth~=2.3.3",
        "google-cloud-secret-manager~=2.7.0",
        "google-cloud-storage~=1.42.3",
        "gcloud~=0.18.3",
        "graphene-django~=2.15.0",
        "openpyxl~=3.0.7",
        "phonenumbers~=8.12.29",
        "python-slugify~=5.0.2",
        "pytz~=2021.1",
        "rcssmin~=1.0.6",
        "requests~=2.26.0",
        "uvicorn[standard]~=0.15.0",
        "whitenoise~=5.3.0",
        "wagtail~=2.15.1",
        "Wand~=0.6.7",
        "opencv_python~=4.5.4.58",
        "rustface~=0.1.0",
        "wagtailvideos~=2.10.9",
        "wagtailmedia~=0.8.0",
        "wagtail-readinglevel~=3.5.0",
        "wagtailfontawesome~=1.2.1",
        "wagtail-quick-create~=1.0.7",
        "wagtail-automatic-redirects~=1.1.5",
    ],
    # entry_points={
    #     'console_scripts': [
    #         'mycarehub-backend = mucarehub:main',
    #     ],
    # },
    scripts=["manage.py"],
)