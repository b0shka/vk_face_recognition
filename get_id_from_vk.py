import vk_api
import time
from config import *

def get_id_from_vk():
    session = vk_api.VkApi(token=token_vk)
    users_pickle_list = os.listdir("pickle_files/")
    file = open('users_id.txt', 'a')
    with open('users_id.txt', 'r') as f:
        all_id = f.readlines()

    city = "Пермь"
    count_result = 1000
    gender = 1
    age_min = 19
    age_max = 20

    while age_min <= age_max:
        month = 1
        while month <= 12:
            time.sleep(2)
            info_list = session.method("users.search", {
                "fields": "id",
                "count": count_result,
                "hometown": city,
                "sex": gender,
                "age_from": age_min,
                "age_to": age_max,
                "birth_month": month,
                "has_photo": 1
            })
            print('[+] Download ID: ' + str(age_min) + ' age, month ' + str(month) + ' (' + str(info_list['count']) + ')')

            for i in info_list['items']:
                if str(i['id']) + '\n' not in all_id:
                    if str(i['id']) + ".pickle" not in users_pickle_list:
                        file.write(str(i['id']) + "\n")

            month += 1
        age_min += 1

    file.close()
    print('[+] Success')

def main():
    get_id_from_vk()

if __name__ == '__main__':
    main()
