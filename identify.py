import face_recognition
from PIL import Image,ImageDraw


image_of_obama=face_recognition.load_image_file('./knowen/obama.jpg')
obama_face_encoding=face_recognition.face_encodings(image_of_obama)[0]


image_of_trump=face_recognition.load_image_file('./knowen/trump.jpg')
trump_face_encoding=face_recognition.face_encodings(image_of_trump)[0]

#array of encoding and names
known_face_encodings=[obama_face_encoding,trump_face_encoding]

known_face_name=["barak obama","donald trump"]

#load test image
face_image=face_recognition.load_image_file("./groups/bushtouba.jpg")
#face_image=face_recognition.load_image_file("./groups/truoba.jpg")

#idntifieing faces in an image
face_loc=face_recognition.face_locations(face_image)
face_encodings=face_recognition.face_encodings(face_image,face_loc)


#coverting to PIL for the modification
pil_image=Image.fromarray(face_image)
draw=ImageDraw.Draw(pil_image)
for(top,right,bottom,left),face_encodings in zip(face_loc,face_encodings):
    matches=face_recognition.compare_faces(known_face_encodings,face_encodings)
    name="unkown"
    if True in matches:
        first_match_index=matches.index(True)
        name=known_face_name[first_match_index]

    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))

    text_wid,text_he=draw.textsize(name)
    draw.rectangle(((left,bottom - text_he - 10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6,bottom-text_he-5),name,fill=(255,255,255,255))

del draw

pil_image.show()
#to save : pil_image.save(./identification.jpg)