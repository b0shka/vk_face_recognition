import os

import vk_api
import time
import codecs
from config import *

def get_id_from_vk():
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    vk = vk_session.get_api()

    age = 18
    age_max = 25
    city_number = 108
    gender = 1

    file = codecs.open('users_id.txt', 'w', encoding='utf8')
    users_pickle_list = os.listdir("pickle_files/")

    while age <= age_max:
        month = 1
        while month <= 12:
            time.sleep(3)
            z = vk.users.search(count=1000,
                                fields='id, has_photo',
                                city=city_number,
                                sex=gender,
                                age_from=age,
                                age_to=age,
                                birth_month=month)
            month = month + 1
            print('[+] Download ID: ' + str(age) + ' age, month ' + str(month) + ' (' + str(z['count']) + ')')
            for x in z['items']:
                if x['has_photo'] == 1:
                    if str(x['id']) + ".pickle" not in users_pickle_list:
                        file.write(str(x['id']) + '\n')
        age = age + 1

    file.close()
    print('[+] Success')

def main():
    get_id_from_vk()

if __name__ == '__main__':
    main()
