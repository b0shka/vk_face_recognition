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
        other_face = []
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
                                for x in range(0, len(face_encodings_user)):
                                    result_equal = face_recognition.compare_faces([param], face_encodings_user[x])

                                    if True in result_equal:
                                        face_encodings_user.append(param)
                                        break
                                    else:
                                        other_face.append(param)
                                        break
                except IndexError as error:
                    pass
            print(len(face_encodings_user), len(other_face))
            if len(other_face) != 0:
                while True:
                    new_equal_face = []
                    new_other_face = []
                    for i in other_face:
                        if len(new_equal_face) == 0:
                            new_equal_face.append(i)
                        else:
                            for x in range(0, len(new_equal_face)):
                                result_equal = face_recognition.compare_faces([i], new_equal_face[x])

                                if True in result_equal:
                                    new_equal_face.append(i)
                                    break
                                else:
                                    new_other_face.append(i)
                                    break

                    if len(new_equal_face) > len(face_encodings_user):
                        face_encodings_user = new_equal_face
                        print('good', len(new_equal_face))
                        break
                    else:
                        if len(new_other_face) == 0 or len(new_other_face) < len(face_encodings_user):
                            break
                        else:
                            other_face = new_other_face
                            print('again', len(other_face))

            print(len(face_encodings_user))
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