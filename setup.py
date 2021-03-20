#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

from setuptools import setup, find_packages

import versioneer


with open("README.md") as readme_file:
    readme = readme_file.read()

with open("HISTORY.md") as history_file:
    history = history_file.read()

setup(
    author="Manuel Holtgrewe",
    author_email="manuel.holtgrewe@bihealth.de",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    entry_points={"console_scripts": ("dash-dwd = dash_dwd.app:main",)},
    description="Dashboard for DWD Weather Data",
    install_requires=[
        "beautifulsoup4==4.7.1",
        "certifi==2020.4.5.1",
        "chardet==3.0.4",
        "click==7.1.1",
        "dash==1.11.0",
        "dash-bootstrap-components==0.9.2",
        "dash-core-components==1.9.1",
        "dash-html-components==1.0.3",
        "dash-renderer==1.4.0",
        "dash-table==4.6.2",
        "dwdweather2==0.12.0",
        "flask==1.1.2",
        "flask-compress==1.4.0",
        "future==0.18.2",
        "idna==2.8",
        "itsdangerous==1.1.0",
        "jinja2==2.11.3",
        "markupsafe==1.1.1",
        "plotly==4.6.0",
        "python-dateutil==2.8.1",
        "requests==2.22.0",
        "requests-cache==0.5.2",
        "retrying==1.3.3",
        "six==1.14.0",
        "soupsieve==2.0",
        "tqdm==4.32.2",
        "urllib3==1.25.8",
        "werkzeug==1.0.1",
    ],
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="weather",
    name="weather",
    packages=find_packages(include=["dash_dwd*"]),
    test_suite="tests",
    tests_require=[],
    url="https://github.com/holtgrewe/dash_dwd",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
