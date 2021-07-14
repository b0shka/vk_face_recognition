#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'face-recognition==1.3.0',
    'vk-api==11.9.4'
]

setup(
    name='vk_face_recognition',
    version='1.1.5',

    description='Creating a database with biometrics of persons and subsequent search on it',
    long_description=readme,
    long_description_content_type='text/markdown',
    license="MIT license",

    packages=['vk_face_recognition'],
    install_requires=requirements,

    author='b0shka',
    author_email='user.b0shka@gmail.com',
    url='https://github.com/b0shka/vk_face_recognition',

    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers'
    ]
)
