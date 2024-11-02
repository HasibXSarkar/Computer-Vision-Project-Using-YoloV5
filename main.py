import cv2
import torch
import numpy as np
from tracker import *
import time
device = torch.device('cpu')
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, device= device)
cap=cv2.VideoCapture('traffic3.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
count=0
tracker = Tracker()
strat_time=time.time()



def POINTS(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE :  
        colorsBGR = [x, y]
        print(colorsBGR)
        
cv2.namedWindow('FRAME')
cv2.setMouseCallback('FRAME', POINTS)
area3 =[(250,362),(213,385),(442,427),(460,378)]
area_3=set()
while True:
    elapsed_time=time.time()-strat_time
    ret,frame=cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue
    frame=cv2.resize(frame,(1020,600))
    results=model(frame)
    list =[]
    for index,rows in results.pandas().xyxy[0].iterrows():
        x=int(rows[0])
        y=int(rows[1])
        x1=int(rows[2])
        y1=int(rows[3])
        b=str(rows['name'])
        cv2.rectangle(frame,(x,y),(x1,y1),(0,255,0),2)
        list.append([x,y,x1,y1])
    idx_bbox = tracker.update(list)
    for bbox in idx_bbox:
        x2,y2,x3,y3,id =bbox
        cv2.rectangle(frame,(x2,y2),(x3,y3),(0,0,255),2)
        cv2.putText(frame,str(id),(x2,y2),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv2.circle(frame,(x3,y3),4,(0,255,0),-1)   
        result = cv2.pointPolygonTest(np.array(area3,np.int32),((x3,y3)),False)
        if result>0:
            area_3.add(id)
    cv2.polylines(frame,[np.array(area3,np.int32)],True,(0,255,255),3)
    count=len(area_3)
    cv2.putText(frame,'Car Count :'+str(count),(770,55),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
    cv2.putText(frame,'FPS:'+str(fps),(769,128),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)& 0xFF==ord('d'):
        break
    if elapsed_time<=100:
        while True:
            time.sleep(0.1)
            print("Inside second while")
            break
cap.release()
cv2.destroyAllWindows()
    