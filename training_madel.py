import face_recognition
import pickle
import os
import sys

def traning_modal_img():
    if not os.path.exists("data"):
        print("[ERROR] Not found dirictory data")
        sys.exit()

    folders = os.listdir("data")

    for i in folders:
        known_encodings = []
        images = os.listdir(f"data/{i}")
        name = i
        for (j, image) in enumerate(images):
            try:
                print(f"[+] Processing image {j+1}/{len(images)}")

                img_param = get_param_face(f"data/{i}/{image}")

                if len(known_encodings) == 0:
                    known_encodings.append(img_param)
                else:
                    for x in range(0, len(known_encodings)):
                        result_equal = face_recognition.compare_faces([img_param], known_encodings[x])
                        if result_equal[0]:
                            known_encodings.append(img_param)
                            break
                        else:
                            break
            except IndexError:
                pass

        data = {
            "name" : name,
            "encodings" : known_encodings
        }

        with open(f"pickle_files/{name}.pickle", "wb") as file:
            file.write(pickle.dumps(data))

        print(f"[INFO] File {name}.pickle successfully created")


def get_param_face(img_path):
    img = face_recognition.load_image_file(img_path)
    img_param = face_recognition.face_encodings(img)[0]

    return img_param

def main():
    traning_modal_img()

if __name__ == "__main__":
    main()