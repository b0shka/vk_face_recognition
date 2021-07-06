# vk_face_recognition
A program for creating a database with human biometrics based on photos. 
Photos will be automatically downloaded from [VKontakte](https://vk.com). 
Subsequently, it will be possible to search for a person using the created database. 
The program was created based on the `face_recognition` and `vk_api` libraries

[![PyPI](https://img.shields.io/pypi/v/vk_face_recognition)](https://pypi.org/project/vk-face-recognition/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/vk-face-recognition)](https://pypi.org/project/vk-face-recognition/)

____
## Installation

#### Requirements
* Python 3.8+
* Linux, Windows or macOS

#### Installing on Linux or Mac
```
pip3 install vk_face_recognition
```

#### Installing on Windows
```
pip install vk_face_recognition
```


## Usage

#### Initial setup
To get started, you need to add your token_vk received on the [site](https://vkhost.github.io/), to the file `main.py` to a string

```
self.session = vk_api.VkApi(token='your_token')
```

#### Using the Library
```
from vk_face_recognition import Vk_recognition

vk_recognition = Vk_recognition()
vk_recognition.start_recognition(age_min=25, age_max=26, gender=1, city='Moscow')
```

When running this code, a file will be created first `users_id.txt` with the user id according to the specified parameters of `age_min`, `age_max`, `gender` and `city`. Then the user's photos will be downloaded to the `data` folder. And then these photos will be used to recognize faces and create face parameters and write them to a separate file in the `pickle_files` folder

#### Search by photo
After creating the database you need, you can search through the photo in the following way

```
from vk_face_recognition import Vk_recognition

search = Vk_recognition()
search.find_people('path to the photo')
```

A search will be performed on the database you created and, if it matches, it will report this
