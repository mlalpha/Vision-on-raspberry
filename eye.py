import picamera


def take_photo(file_name = 'tmp.png'):
    camera = picamera.PiCamera()
    camera.capture("img/%s"%file_name)
    camera.close()
