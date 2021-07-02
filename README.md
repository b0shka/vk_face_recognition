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

##### To search for a person by photo, run the file check_photo_in_pickle.py
```
python3 ./check_photo_in_pickle.py
```
### Additionally
The received id will be stored in a file `users_id.txt`. The downloaded photos will be stored in the `data` folder. And the files created by pickle will be stored in the `pickle_files` folder
