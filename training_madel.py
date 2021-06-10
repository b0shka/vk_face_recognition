import face_recognition
import pickle
import os
import sys
import h5py

def traning_modal_img():
    if not os.path.exists("data"):
        print("[ERROR] Not found dirictory data")
        sys.exit()

    folders = os.listdir("data")
    users_pickle_list = os.listdir("pickle_files/")
    num = 1

    for i in folders:
        face_encodings_user = []
        name = i
        if str(i) + ".pickle" not in users_pickle_list:
            print(f"[+] Training {i} ({num}/{len(folders)})")
            images = os.listdir(f"data/{i}")
            for (j, image) in enumerate(images):
                try:
                    print(f"[+] Processing image {j+1}/{len(images)}")

                    img = face_recognition.load_image_file(f"data/{i}/{image}")
                    img_param = face_recognition.face_encodings(img)

                    if len(img_param) != 0:
                        for param in img_param:
                            #face_encodings_user.append(param)

                            if len(face_encodings_user) == 0:
                                face_encodings_user.append(param)
                            else:
                                for x in range(0, len(face_encodings_user)+1):
                                    result_equal = face_recognition.compare_faces(param,  face_encodings_user[x])
                                    if True in face_encodings_user:
                                        face_encodings_user.append(param)
                except IndexError:
                    pass

            if len(face_encodings_user) != 0:
                data = {
                    "name" : name,
                    "encodings" : face_encodings_user
                }

                # Write to .h5 file
                '''with h5py.File('data.h5', 'a') as file:
                    if name not in file.keys():
                        file.create_dataset(f'{name}', data=face_encodings_user)'''

                with open(f"pickle_files/{name}.pickle", "wb") as file:
                    file.write(pickle.dumps(data))
                    print(f"[INFO] File {name}.pickle successfully created\n")
            else:
                for photo in os.listdir(f"data/{i}"):
                    os.remove(f"data/{i}/{photo}")
                os.rmdir(f"data/{i}")
                print(f"[INFO] In folder data/{i} not found face\n")

        num += 1

def main():
    traning_modal_img()

if __name__ == "__main__":
    main()