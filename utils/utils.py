from datetime import datetime
import numpy as np
import cv2


def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


def get_black_background():
    return np.zeros((500, 500))


def generate_time_image_bytes(dt):
    text = convert_time_to_string(dt)
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0]*0.35), int(image.shape[1]*0.5)), font, 1.5, (255, 255, 0), 2, cv2.LINE_AA)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()
