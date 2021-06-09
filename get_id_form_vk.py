import os

import vk_api
import time
import codecs
from config import *

def get_id_from_vk():
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()

    age = 19
    age_max = 20
    city_number = 108
    gender = 1

    file = codecs.open('users_id.txt', 'w', encoding='utf8')
    users_pickle_list = os.listdir("pickle_files/")

    while age <= age_max:
        month = 1
        while month <= 12:
            time.sleep(2)
            peoples = vk.users.search(count=1000,
                                fields='id, has_photo',
                                city=city_number,
                                sex=gender,
                                age_from=age,
                                age_to=age,
                                birth_month=month)
            print('[+] Download ID: ' + str(age) + ' age, month ' + str(month) + ' (' + str(peoples['count']) + ')')
            for i in peoples['items']:
                if i['has_photo'] == 1:
                    if str(i['id']) + ".pickle" not in users_pickle_list:
                        file.write(str(i['id']) + '\n')
            month += 1
        age += 1

    file.close()
    print('[+] Success')

def main():
    get_id_from_vk()

if __name__ == '__main__':
    main()
