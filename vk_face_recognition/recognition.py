import requests
import vk_api
import face_recognition
import pickle
import os
import sys
import h5py
from photo_recognition import Traning_model
from search_by_photo import Find_face

class Recognition_face:
    def __init__(self):
        self.traning_class = Traning_model()
        self.find_class = Find_face()

        self.session = vk_api.VkApi(token=os.environ['token_vk'])
        if not os.path.exists('users_id.txt'):
            file = open('users_id.txt', 'w')
            file.close()

        if not os.path.exists('data'):
            os.mkdir('data')

        if not os.path.exists('pickle_files'):
            os.mkdir('pickle_files')


    def get_id_from_vk(self, age=None, month=None, gender=None, city=None):
        try:
            with open('users_id.txt', 'w') as file:
                info_list = self.session.method("users.search", {
                    "fields": "id",
                    "count": 1000,
                    "hometown": city,
                    "sex": gender,
                    "age_from": age,
                    "age_to": age,
                    "birth_month": month,
                    "has_photo": 1
                })

                for i in info_list['items']:
                    if str(i['id']) + ".pickle" not in os.listdir("pickle_files/"):
                        file.write(f"{i['id']}\n")

                print(f"[+] Download ID: {age} age, month {month} ({info_list['count']})\n")
        except Exception as error:
            print(f'[ERROR] (get_id_from_vk) {error}\n')


    def download_photo(self, user_id=None):
        try:
            if user_id == None:
                print('[ERROR] Вы не указали user_id')
            else:
                request_result = self.session.method("photos.getAll", {
                    "owner_id": user_id,
                    "count": 10,
                    "no_service_albums": 0
                })
                count_photo = 1

                for i in request_result['items']:
                    url = i['sizes'][-3]['url']
                    r = requests.get(url)

                    with open(f'data/{user_id}/{count_photo}.jpg', 'wb') as file:
                        file.write(r.content)
                    count_photo += 1
        except Exception as error:
            print(f'[ERROR] (download_photo) {error}\n')


    def find_people_from_db(self, url_photo):
        self.find_class.find(url_photo)


    def start_recognition(self, age_min=None, age_max=None, gender=None, city=None):
        try:
            while age_min <= age_max:
                month = 1
                while month <= 12:
                    num = 0
                    self.get_id_from_vk(age_min, month, gender, city)

                    with open('users_id.txt', 'r') as file:
                        list_id = file.readlines()
                        count_all_id = len(list_id)

                        for i in list_id:
                            num += 1
                            print(f"[+] Processing {num}/{count_all_id} ({i[:-1]})")
                            if str(i[:-1]) not in os.listdir('data/'):
                                if str(i[:-1]) not in os.listdir("pickle_files/"):
                                    os.mkdir(f'data/{i[:-1]}')

                                    self.download_photo(i[:-1])
                                    count_photo = os.listdir(f"data/{i[:-1]}")

                                    if len(count_photo) != 0:
                                        self.traning_class.traning(i[:-1])
                            else:
                                count_photo = os.listdir(f"data/{i[:-1]}")

                                if len(count_photo) != 0:
                                    self.traning_class.traning(i[:-1])

                            for j in os.listdir(f'data/{i[:-1]}'):
                                os.remove(f'data/{i[:-1]}/{j}')
                            os.rmdir(f'data/{i[:-1]}')

                    month += 1
                age_min += 1

            print('[+] Success')
        except TypeError:
            print('[ERROR] Вы указали не все параметры функции\n')
        except Exception as error:
            print(f'[ERROR] (main) {error}\n')



test = Recognition_face()
test.start_recognition(age_min=24, age_max=25, gender=1, city='Perm')