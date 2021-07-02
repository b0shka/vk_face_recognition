# vk_face_recognition
A program for creating a database of face parameters from photos downloaded from VKontakte and searching for it
____
### Install everything you need and run
#### Installation
```
git clone https://github.com/b0shka/vk_face_recognition.git
cd vk_face_recognition
pip3 install -r requirements.txt
```
#### Run
```
python3 ./main.py
```
##### To search for a person by photo, run the file check_photo_in_pickle.py
```
python3 ./check_photo_in_pickle.py
```
### Additionally
In the file `main.py` at the very bottom, you need to specify the parameters for searching for people. The accepted ID will be saved in a file `users_id.txt`. The uploaded photos will be stored in the `data` folder. And the files created by pickle will be stored in the `pickle_files` folder.
