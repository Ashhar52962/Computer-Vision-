import cv2

video = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(r"C:\Users\Dell\PycharmProjects\Computer Vision\FaceDetection\Files")

while True:
    check,frame = video.read()
    cv2.imshow("Capture",frame)
    k = cv2.waitKey(5)
    if k == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
