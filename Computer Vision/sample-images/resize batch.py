import cv2
import glob

image = glob.glob(r"C:\Users\Dell\PycharmProjects\Computer Vision\sample-images\*.jpg")




for img in image:
    file = img[60:]
    img1 = cv2.imread(img)
    resize_image = cv2.resize(img1,(480,640))
    cv2.imshow("a", resize_image)
    cv2.waitKey(1000)
    cv2.imwrite(r"C:\Users\Dell\PycharmProjects\Computer Vision\sample-images\resized_{}".format(file),resize_image)
    print("Image Saved Succesfully with new size")
