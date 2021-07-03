from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
      name='vk_face_recognition',
      version='1.0.0',

      description='A program for creating a database of face parameters from photos downloaded from VKontakte and searching for it',

      long_description=long_description,
      long_description_content_type='text/markdown',

      packages=['vk_face_recognition'],
      install_requires=['vk_api'],

      author_email='user.b0shka@gmail.com',
      url='https://github.com/b0shka/vk_face_recognition'
)
