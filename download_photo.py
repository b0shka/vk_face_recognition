import shutil
import os
import requests
import codecs
import vk_api
from config import *

def load_file(name, url, name_folder):
    if not os.path.exists(f'data/{name_folder}/{name}.jpg'):
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(f'data/{name_folder}/{name}.jpg', 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

def get_photo(user_id_):
    try:
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        vk = vk_session.get_api()

        os.mkdir(f"data/{user_id_}")
        request_result = vk.photos.getAll(owner_id=user_id_,
                                          count=50,
                                          no_service_albums=0)
        prev = ''
        flag = 0
        photos = []
        for item in request_result['items']:
            for size in item['sizes']:
                url_ = str(size['url'])
                mas_ = url_.split('/')
                ident = mas_[4]
                if prev != ident:
                    prev = ident
                    flag = 0
                else:
                    flag += 1
                    if flag == 3:
                        photos.append(url_)
        count_photo = 0
        for photo in photos:
            count_photo += 1
            if count_photo <= 10:
                load_file(count_photo, photo, user_id_)
    except Exception as error:
        print(error)

def main():
    if not os.path.exists("pickle_files"):
        os.mkdir("pickle_files")
    if not os.path.exists("data"):
        print("[ERROR] Not found dirictory data")
    else:
        file = codecs.open(u'users_id.txt', 'r', encoding='utf8')
        users_pickle_list = os.listdir("pickle_files/")
        num = 0
        with open("users_id.txt", "r") as f:
            a = f.readlines()
            count_all_id = len(a)
        for i in file:
            if str(i[:-1]) + ".pickle" not in users_pickle_list:
                num += 1
                print(f"[+] Processing {num}/{count_all_id}")
                get_photo(i[:-1])
                count_photo = os.listdir(f"data/{i[:-1]}")
                if len(count_photo) == 0:
                    os.rmdir(f"data/{i[:-1]}")

        file.close()

if __name__ == '__main__':
    main()
