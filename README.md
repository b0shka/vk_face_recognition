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
##### To get the user id, run the file get_id_from_vk.py
```
python3 ./get_id_from_vk.py
```
##### To download photos from accounts by id, run the file download_photo.py
```
python3 ./download_photo.py
```
##### To get the face parameters and create it .pickle file run the file training_madel.py
```
python3 ./training_madel.py
```
##### To search for a person by photo, run the file check_photo_in_pickle.py
```
python3 ./check_photo_in_pickle.py
```
### Additionally
The received id will be stored in a file `users_id.txt`. The downloaded photos will be stored in the `data` folder. And the files created by pickle will be stored in the `pickle_files` folder
