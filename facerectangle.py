import face_recognition
import cv2
from PIL import Image,ImageDraw
shah_image = face_recognition.load_image_file("shah.jpeg")
rosh_image = face_recognition.load_image_file("rosh.jpg")

shah_encoding = face_recognition.face_encodings(shah_image)[0]
rosh_encoding = face_recognition.face_encodings(rosh_image)[0]
known_face_encodings=[shah_encoding,rosh_encoding]
known_face_names=["khan","roshan"]
test_image=face_recognition.load_image_file('stijob.jpg')
face_locations=face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image,face_locations)
pil_image=Image.fromarray(test_image)
draw=ImageDraw.Draw(pil_image)
for (top,right,bottom,left) ,face_encoding in zip(face_locations,face_encodings):
    matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
    name="Unknown Person"
    if True in matches:
        first_match_index=matches.index(True)
        name=known_face_names[first_match_index]
    draw.rectangle(((left+2,top+2),(right+2,bottom+2)),outline=(0,255,255))
    text_width,text_height=draw.textsize(name)
    draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left+6,bottom-text_height-5),name,fill=(255,255,255,255))
del draw
pil_image.save('detected.jpg')

