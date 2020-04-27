import cv2
import numpy as np
from matplotlib import pyplot as plt

ndown = input("Enter number of downsampling steps:")
if ndown == '':
    ndown = 2
else:
    ndown = int(ndown)

nbilateral = input("Enter number of bilateral filtering steps: ")
if nbilateral == '':
    nbilateral = 70
else:
    nbilateral = int(nbilateral)

scale = input("Enter scaling:")
if scale == '':
    scale = 2
else:
    scale = float(scale)


ip = str(input("Enter IP: "))
if ip == "0":
    cap = cv2.VideoCapture(0)
elif ip == "":
    cap = cv2.VideoCapture("https://192.168.0.130:8080/video")
else:
    cap = cv2.VideoCapture("https://" + ip + "/video")

com = input("Enter number of images: ")
if com == '':
    com = 7
else:
    com = int(com)


i = 1
k = 0

c_w = [255, 255, 255]
c_b = [0, 0, 0]
bt = 5
wt = 5

pressedKey = cv2.waitKey(1)

while cap.isOpened():

    _,  irgb = cap.read()

    icolor = irgb
    for _ in range(ndown):
        icolor = cv2.pyrDown(icolor)

    for _ in range(nbilateral):
        icolor = cv2.bilateralFilter(icolor, d=9, sigmaColor=9, sigmaSpace=7)

    for _ in range(ndown):
        icolor = cv2.pyrUp(icolor)

    gray = cv2.cvtColor(irgb, cv2.COLOR_RGB2GRAY)
    blur = cv2.medianBlur(gray, 7)

    iedge = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=5,C=2)

    iedge = cv2.cvtColor(iedge, cv2.COLOR_GRAY2RGB)
    icartoon = cv2.bitwise_and(icolor, iedge)

    cv2.namedWindow('cartoon',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('cartoon', int(icartoon.shape[0]/scale), int(icartoon.shape[1]/scale))
    cv2.imshow('cartoon', icartoon)

    if cv2.waitKey(1) == ord('s'):
        if i <= com:
            cv2.imwrite('anim_'+str(i)+'.jpg', icartoon)
            if i != 0:
                if i == 1:
                    anim1 = cv2.imread("anim_1.jpg")
                    border_b = cv2.copyMakeBorder(anim1, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim1 = border_w
                if i == 2:
                    anim2 = cv2.imread("anim_2.jpg")
                    border_b = cv2.copyMakeBorder(anim2, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim2 = border_w
                if i == 3:
                    anim3 = cv2.imread("anim_3.jpg")
                    border_b = cv2.copyMakeBorder(anim3, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim3 = border_w
                if i == 4:
                    anim4 = cv2.imread("anim_4.jpg")
                    border_b = cv2.copyMakeBorder(anim4, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim4 = border_w
                if i == 5:
                    anim5 = cv2.imread("anim_5.jpg")
                    border_b = cv2.copyMakeBorder(anim5, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim5 = border_w
                if i == 6:
                    anim6 = cv2.imread("anim_6.jpg")
                    border_b = cv2.copyMakeBorder(anim6, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim6 = border_w
                if i == 7:
                    anim7 = cv2.imread("anim_7.jpg")
                    border_b = cv2.copyMakeBorder(anim7, bt, bt, bt, bt, cv2.BORDER_CONSTANT, value = c_b)
                    border_w = cv2.copyMakeBorder(border_b, wt, wt, wt, wt, cv2.BORDER_CONSTANT, value = c_w)
                    anim7 = border_w
        else:
            print("yay")
            if k == 0:
                print("smh")
            if k == 1:
                cv2.imwrite('comic.jpg', anim1)
            if k == 2:
                hor2_1 = np.hstack((anim1, anim2))
                cv2.imwrite('comic.jpg', hor2_1)
            if k == 3:
                hor3_1 = np.hstack((anim1, anim2))
                width = int(hor3_1.shape[1])
                height = int(width/anim3.shape[1]*anim3.shape[0])
                dim = (width, height)
                resized = cv2.resize(anim3, dim, interpolation = cv2.INTER_AREA)
                ver3_1 = np.vstack((hor3_1, resized))
                cv2.imwrite('comic.jpg', ver3_1)
            if k == 4:
                hor4_1 = np.hstack((anim1, anim2))
                hor4_2 = np.hstack((anim3, anim4))
                ver4_1 = np.vstack((hor4_1, hor4_2))
                cv2.imwrite('comic.jpg', ver4_1)
            if k == 5:
                hor5_1 = np.hstack((anim1, anim2))
                hor5_2 = np.hstack((anim3, anim4))
                width = int(hor5_1.shape[1])
                height = int(width/anim5.shape[1]*anim5.shape[0])
                dim = (width, height)
                resized = cv2.resize(anim5, dim, interpolation = cv2.INTER_AREA)
                ver5_1 = np.vstack((hor5_1, hor5_2, resized))
                cv2.imwrite('comic.jpg', ver5_1)
            if k == 6:
                hor6_1 = np.hstack((anim1, anim2))
                hor6_2 = np.hstack((anim3, anim4))
                hor6_3 = np.hstack((anim5, anim6))
                ver6_1 = np.vstack((hor6_1, hor6_2, hor6_3))
                cv2.imwrite('comic.jpg', ver6_1)
            if k == 7:
                hor7_1 = np.hstack((anim1, anim2))
                hor7_2 = np.hstack((anim3, anim4))
                hor7_3 = np.hstack((anim5, anim6))
                width = int(hor7_1.shape[1])
                height = int(width/anim7.shape[1]*anim7.shape[0])
                dim = (width, height)
                resized = cv2.resize(anim7, dim, interpolation = cv2.INTER_AREA)
                ver7_1 = np.vstack((hor7_1, hor7_2, hor7_3, resized))
                cv2.imwrite('comic.jpg', ver7_1)
        i+=1
        k = i - 1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
