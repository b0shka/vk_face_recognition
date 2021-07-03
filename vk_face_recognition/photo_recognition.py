import face_recognition
import pickle
import os
import sys

def recognition(user_id):
    if not os.path.exists("data"):
        print("[ERROR] Not found dirictory data")
        sys.exit()

    users_pickle_list = os.listdir("pickle_files/")
    num = 1

    face_encodings_user = []
    other_face = []
    if str(user_id) + ".pickle" not in users_pickle_list:
        images = os.listdir(f"data/{user_id}")
        for (i, image) in enumerate(images):
            try:
                img = face_recognition.load_image_file(f"data/{user_id}/{image}")
                img_param = face_recognition.face_encodings(img)

                if len(img_param) != 0:
                    for param in img_param:
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
            except IndexError:
                pass
            except Exception as error:
                print(f'[ERROR] (traning_model) {error}\n')

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
                    break
                else:
                    if len(new_other_face) == 0 or len(new_other_face) < len(face_encodings_user):
                        break
                    else:
                        other_face = new_other_face

        if len(face_encodings_user) != 0:
            data = {
                "name" : user_id,
                "encodings" : face_encodings_user
            }

            with open(f"pickle_files/{user_id}.pickle", "wb") as file:
                file.write(pickle.dumps(data))
                print(f"[INFO] File {user_id}.pickle successfully created\n")
        else:
            print(f"[INFO] In folder data/{user_id} not found face\n")

        num += 1
