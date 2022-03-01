import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
img_counter =0

while True:
	_, frm = cap.read()

	cv2.imshow("window", frm)

	k= cv2.waitKey(1)

	if k%256==27:
		old_gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)
		break

	elif k%256==32:
		image_name =("C:\E.D.I.T.H\Camera\opencv_frame_{}.png" .format(img_counter))
		cv2.imwrite(image_name,frm)
		img_counter+=1


cv2.realse()
cv2.destroyAllWindows()