import cv2
import glob

#reading  all file
image = glob.glob(r"C:\Users\Dell\PycharmProjects\Computer Vision\FaceDetection\Face Image\*.jpg")
face_cascade = cv2.CascadeClassifier(r"C:\Users\Dell\PycharmProjects\Computer Vision\FaceDetection\Files\haarcascade_frontalface_default.xml")


for img in image:
    image1 = cv2.imread(img)
    gray_image = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=2)
    for x,y,w,h in faces:
        show_image = cv2.rectangle(image1,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow("image",show_image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()




