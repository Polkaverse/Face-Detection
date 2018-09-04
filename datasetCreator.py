import cv2
import numpy as np
import sqlite3

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);


def insertOrUpdate(Id,Name,age,des):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM  Peoples WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0;
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE Peoples SET NAME="+str(Name)+" WHERE ID="+str(Id)
        cmd="UPDATE Peoples SET age="+str(age)+" WHERE ID="+str(Id)
        cmd="UPDATE Peoples SET designation="+str(des)+" WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO Peoples(ID,Name,age,designation) VALUES("+str(Id)+" ,"+str(Name)+","+str(age)+","+str(des)+")"
    
    conn.execute(cmd)
    conn.commit()
    conn.close()

id=raw_input("enter user id")
name=raw_input("enter your name")
age=raw_input("enter age")
des=raw_input("enter designation")
insertOrUpdate(id,name,age,des)
sampleNum=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        
        cv2.imwrite("dataSet/user."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.waitKey(100);
    cv2.imshow("FACE",img);
    cv2.waitKey(1);
    if(sampleNum>100):
            break
cam.release()
cv2.destroyAllWindows()
    
