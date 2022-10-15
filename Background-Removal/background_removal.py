# Background Removal

# import library
import os
import cv2
import numpy as np
import mediapipe as mp


# inisialisasi mediapipe
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(
    model_selection=1)

# Buat  gambar menjadi list
image_path = 'images'
images = os.listdir(image_path)

image_index = 0
bg_image = cv2.imread(image_path+'/'+images[image_index])

# Membuat videocapture object untuk akses webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()

    # flip frame ke arah horizontal
    frame = cv2.flip(frame, 1)
    height, width, channel = frame.shape

    RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # hasil
    results = selfie_segmentation.process(RGB)

    # ekstrak segmented mask
    mask = results.segmentation_mask

    condition = np.stack(
        (results.segmentation_mask,) * 3, axis=-1) > 0.7

    # ubah background image menjadi frame awal
    bg_image = cv2.resize(bg_image, (width, height))

    # kombinasi frame dengan background dengan pengkondisian
    output_image = np.where(condition, frame, bg_image)

    # output
    cv2.imshow("Mask", mask)
    cv2.imshow("Output", output_image)
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    # if 'd' key is pressed then change the background image
    elif key == ord('d'):

        if image_index != len(images)-1:
            image_index += 1
        else:
            image_index = 0
        bg_image = cv2.imread(image_path+'/'+images[image_index])


# release the capture object and close all active windows
cap.release()
cv2.destroyAllWindows()
