import cv2
import numpy as np
import smtplib


#defining mse
def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

#read the images 
original = cv2.imread("opencv_frame_0.png")

cam = cv2.VideoCapture(0)

cv2.namedWindow("face verification")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "compare.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        compare= cv2.imread("compare.png")
        m=mse(original,compare) 
        print(m)
        if(m<15000):
                message="face matched"
                print(message)
		
        else:
                message="face did not matched, someonr is trying to enter in your house"
                print(message)
                
    
cam.release()

cv2.destroyAllWindows()



