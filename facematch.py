import face_recognition



image_of_bill=face_recognition.load_image_file('./knowen/gates.jpg')
bill_face_encoding=face_recognition.face_encodings(image_of_bill)[0]

image_unkown=face_recognition.load_image_file('./unknowen/im2.jpg')
unkown_encoding=face_recognition.face_encodings(image_unkown)[0]


#comparing faces
results= face_recognition.compare_faces([bill_face_encoding],unkown_encoding)
print(results)