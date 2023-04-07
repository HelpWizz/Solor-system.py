import cv2

img =  cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20, 300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Mercury", (100, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Venus", (200, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Earth", (290, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Mars", (380, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Jupiter", (570, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Saturn", (770, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Urnaus", (970, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.putText(img, "Neptune", (1100, 280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (243, 54, 234))
cv2.imshow("output",img)
cv2.imwrite("Solar_system.jpg",img)
cv2.waitKey(0)