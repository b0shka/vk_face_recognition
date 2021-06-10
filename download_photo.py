import shutil
import os
import requests
import vk_api
from config import *

def get_photo(user_id):
    try:
        session = vk_api.VkApi(token=token_vk)
        os.mkdir(f"data/{user_id}")

        request_result = session.method("photos.getAll", {
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
        print(f"[ERROR] {error}")

def main():
    if not os.path.exists("pickle_files"):
        os.mkdir("pickle_files")
    if not os.path.exists("data"):
        print("[ERROR] Not found dirictory data")
    else:
        users_pickle_list = os.listdir("pickle_files/")
        with open("users_id.txt", "r") as f:
            count_all_id = len(f.readlines())
        num = 0
        file = open('users_id.txt', 'r')
        for i in file:
            if str(i[:-1]) + ".pickle" not in users_pickle_list:
                num += 1
                print(f"[+] Processing {num}/{count_all_id}")
                get_photo(i[:-1])
                count_photo = os.listdir(f"data/{i[:-1]}")
                if len(count_photo) == 0:
                    os.rmdir(f"data/{i[:-1]}")

        file.close()
        print('[+] Success')

if __name__ == '__main__':
    main()
