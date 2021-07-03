import face_recognition
import pickle
import sys
import os
import vk_api

def find_face(img_path):
    print("[+] Searching...")

    if not os.path.exists("pickle_files"):
        print("[ERROR] Not found dirictory pickle_files")
        sys.exit()

    img = face_recognition.load_image_file(img_path)
    img_param = face_recognition.face_encodings(img)

    folders = os.listdir("pickle_files")
    found_count = 0

    for param in img_param:
        for i in folders:
            data = pickle.loads(open(f"pickle_files/{i}", "rb").read())
            result_equal = face_recognition.compare_faces(data["encodings"],  param)

            if True in result_equal:
                session = vk_api.VkApi(token=os.environ['token_vk'])
                name = session.method("users.get", {"user_ids": data['name']})
                print(f"[+] Found in https://vk.com/id{data['name']} ({name[0]['first_name']} {name[0]['last_name']})")
                found_count += 1

        if found_count == 0:
            print("[-] Not found")
