import cv2

#Reading Images
img = cv2.imread("galaxy.jpg",0)

#resizing images
resize_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imwrite("Galaxy_resize.jpg",resize_image)
#Showing Images
cv2.imshow("Galaxy",resize_image)# this cant be visible until you write next statement
cv2.waitKey()# windows will close when user press any button

# cv2.waitKey(1000)# windows will close after 1000ms

cv2.destroyAllWindows()# this will destroy all windows which we created after user press any button





