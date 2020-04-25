import cv2

ndown = 2       
nbilateral = 70

cap = cv2.VideoCapture(0)

i = 1

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

    cv2.imshow("cartoon", icartoon)

    if cv2.waitKey(1) == ord('s'):
        cv2.imwrite('anim_'+str(i)+'.jpg',icartoon)
        i+=1
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
