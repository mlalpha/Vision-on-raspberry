import random as rand
import requests
from time import sleep
# from PIL import Image
import datetime
import eye
import snippets


def ask_server():
    try:
        r = requests.get('https://us-central1-my-eye-b8444.cloudfunctions.net/askAnyPhotoNeed')
        print(r.json())
        return r.json()['photoRequest']
    except:
        return False


def upload_photo():
    file_name = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    eye. take_photo()
    print('Uploading photo')
    snippets.upload_blob('my-eye-b8444.appspot.com', 'img/tmp.png', file_name)

    # url = 'https://us-central1-my-eye-b8444.cloudfunctions.net/uploadImage'
    # # url = 'http://localhost:5000/my-eye-b8444/us-central1/uploadImage'
    # file_path = 'test.png'
    # files = {'fileToUpload': (file_path, open(file_path, 'rb'), 'image/png')}
    # try:
    #     r = requests.post(
    #         url,
    #         files=files
    #     )
    #     print(r.text)
    # except:
    #     return


while True:
    if ask_server() is True:
        upload_photo()
    sleep(0.2)