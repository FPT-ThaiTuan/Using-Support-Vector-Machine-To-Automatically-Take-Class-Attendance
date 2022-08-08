import cv2
import os

video = cv2.VideoCapture(0)

count = 0

nameID = str(input("Enter name: ")).lower()

path = 'Dataset/' + nameID

isExist = os.path.exists(path)

os.makedirs(path)

while True:
    ret, frame = video.read()
    count += 1
    name = './Dataset/' + nameID + "/" + str(count) + ".jpg"
    print("Creating Images : " + name)
    cv2.imwrite(name, frame)
    cv2.imshow("WindowFrame", frame)
    cv2.waitKey(0)
    if count >= 100:
        break

video.release()
cv2.destroyAllWindows()
