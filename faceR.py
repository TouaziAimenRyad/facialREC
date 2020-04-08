import face_recognition

image=face_recognition.load_image_file('./groups/team2.jpg')
face_locations=face_recognition.face_locations(image)           #array of coordinates of each face
print(face_locations)
print(f'there are {len(face_locations)} faces')
