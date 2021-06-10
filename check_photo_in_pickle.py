import face_recognition
import pickle
import sys
import h5py
import vk_api
from config import *

def check_face(img_path):
    print("[+] Searching...")
    session = vk_api.VkApi(token=token_vk)

    if not os.path.exists("pickle_files"):
        print("[ERROR] Not found dirictory pickle_files")
        sys.exit()

    img = face_recognition.load_image_file(img_path)
    img_param = face_recognition.face_encodings(img)

    folders = os.listdir("pickle_files")
    found_count = 0
    #file_data = h5py.File('data.h5', 'r')

    for param in img_param:
        # Read in .h5 file
        '''for i in file_data.keys():
            data = file_data[i]
            result_equal = face_recognition.compare_faces(data,  param)

            if True in result_equal:
                name = session.method("users.get", {"user_ids": data['name']})
                print(f"[+] Found in https://vk.com/id{data['name']} ({name[0]['first_name']} 
                found_count += 1'''

        for i in folders:
            data = pickle.loads(open(f"pickle_files/{i}", "rb").read())
            result_equal = face_recognition.compare_faces(data["encodings"],  param)

            if True in result_equal:
                name = session.method("users.get", {"user_ids": data['name']})
                print(f"[+] Found in https://vk.com/id{data['name']} ({name[0]['first_name']} {name[0]['last_name']})")
                found_count += 1

        if found_count == 0:
            print("[-] Not found")

    #file_data.close()

def main():
    check_face("img.jpg")

if __name__ == "__main__":
    main()