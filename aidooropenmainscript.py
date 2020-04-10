import face_recognition
import pickle
import numpy as np
import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont
import pickle
import smtpmail as d
import ledblink as y
import aiservo as z
import aiservo2 as a
import spee  as e
m=1
t=None
l=[]
r=[]
b=[]
u=[]
fonts = cv2.FONT_HERSHEY_SIMPLEX 
p=0  
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 1
   
# Blue color in BGR 
color = (255, 255, 0) 
  
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.putText() method 




# Load face encodings
with open('dataset_papa.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)
known_face_names = list(all_face_encodings.keys())
known_face_encodings = np.array(list(all_face_encodings.values()))

n=10;
q=10;
i=0
cap=cv2.VideoCapture(0)
while True:
    ret,img=cap.read()
    s=[]
    i=i+1
    print(i)
    cv2.imwrite("stijo3.jpg", img) 
    test_image=face_recognition.load_image_file('stijo3.jpg')
    face_locations=face_recognition.face_locations(test_image)
    face_encodings = face_recognition.face_encodings(test_image,face_locations)
    pil_image=Image.fromarray(test_image)
    draw=ImageDraw.Draw(pil_image)
    font = ImageFont.truetype("Arial.ttf",10)


# Using cv2.putText() method 



    for (top,right,bottom,left) ,face_encoding in zip(face_locations,face_encodings):
      matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
      name="Unknown Person"
      if True in matches:
        first_match_index=matches.index(True)
        name=known_face_names[first_match_index]
      draw.rectangle(((left+2,top+2),(right+2,bottom+2)),outline=(255,255,0))
      text_width,text_height=draw.textsize(name)
      draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(255,255,0),outline=(255,255,0))
      draw.text((left+6,bottom-text_height-5),name,fill=(255,255,255,0),font=font)
      l.append(left)
      r.append(right)
      u.append(text_height)
      b.append(bottom)
      print(name)
      s.append(name)
      p=p+1
    del draw
    img = np.array(pil_image)
    img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   # print(s)
    for t in s:
        print(t)

    
     
    if t is not None :
     for h in range(0,p):
       print(t)
       img= cv2.putText(img,s[h],(l[h]+6,b[h]-u[h]-5), fonts,  
                   fontScale, color, thickness,cv2.LINE_AA)
    
        
    
    
   
    cv2.imshow("test",img)
     
    i=i+1
    print(i)
    t=None
    p=0
    if i==100:
        i=0
        cv2.destroyAllWindows()
    key=cv2.waitKey(1)
    if key ==ord('q') & 0xFF:
        break
     
    for o in s:
        
        if o=="stijo":
          n=n+1
          #print("got")
          if n==0 or n>6:
           y.ledh()
           e.speakout("access ..granted.. door unlocked welcome home")

           a.ser()
           z.ser()
           
           m=2
           n=1
        elif o=="Unknown Person"or o=="salimma" or "papa":
            q=q+1
            if q==0 or q>4:
             cv2.imwrite("intruder.jpg", img) 
             d.mails()
             y.ledblink()
             e.speakout("access.. denied .. door cannot be opened")
             q=1
    if (m%2)==0:
        m=m+2
        if m==10:
            m=1
            y.ledlow()
            z.ser2()
            a.ser2()
            
    s.clear()
    l.clear()
    b.clear()
    u.clear() 
cv2.destroyAllWindows()