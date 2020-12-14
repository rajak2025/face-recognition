import cv2
import face_recognition



img1 = face_recognition.load_image_file('Images/img.jpg')
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Images/test.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
 
faceLoc = face_recognition.face_locations(img1)[0]
encodeElon = face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)
 
faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)
 
results = face_recognition.compare_faces([encodeElon],encodeTest)
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),10)

im1resized = cv2.resize(img1, (500,500))
im2resized = cv2.resize(imgTest, (500, 500))

cv2.imshow('First Image',im1resized)
cv2.imshow('Test Image',im2resized)
cv2.waitKey(0)
