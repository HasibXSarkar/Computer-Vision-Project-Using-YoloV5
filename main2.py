import cv2
import torch
import numpy as np
from tracker import *
import time
from Arduino import Arduino
board= Arduino("9600",port="COM6")
board.pinMode(2,"OUTPUT")
board.pinMode(3,"OUTPUT")
board.pinMode(4,"OUTPUT")
board.pinMode(5,"OUTPUT")
board.pinMode(6,"OUTPUT")
board.pinMode(7,"OUTPUT")
board.pinMode(8,"OUTPUT")
board.pinMode(9,"OUTPUT")
board.pinMode(10,"OUTPUT")
board.digitalWrite(2,"HIGH")
board.digitalWrite(5,"HIGH")
board.digitalWrite(8,"HIGH")

def cam1(val):
    board.digitalWrite(2,"LOW")
    start_time =time.time()
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    cap1=cv2.VideoCapture('traffic1.mp4')
    fps = cap1.get(cv2.CAP_PROP_FPS)
    count1=0
    tracker = Tracker()

    def POINTS(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE :  
            colorsBGR = [x, y]
            print(colorsBGR)
        

    cv2.namedWindow('FRAME')
    cv2.setMouseCallback('FRAME', POINTS)
    area3 =[(238,293),(206,321),(453,319),(450,286)]
    area_3=set()
    while True:
        elapsed_time=time.time()-start_time
        ret1,frame1=cap1.read()
        if not ret1:
            break
        count1 += 1
        if count1 % 3 != 0:
            continue
        frame1=cv2.resize(frame1,(1020,600))
        results1=model(frame1)
        list =[]
        for index,rows in results1.pandas().xyxy[0].iterrows():
            x=int(rows[0])
            y=int(rows[1])
            x1=int(rows[2])
            y1=int(rows[3])
            b=str(rows['name'])
            cv2.rectangle(frame1,(x,y),(x1,y1),(0,255,0),2)
            list.append([x,y,x1,y1])
        idx_bbox = tracker.update(list)
        for bbox in idx_bbox:
            x2,y2,x3,y3,id =bbox
            cv2.rectangle(frame1,(x2,y2),(x3,y3),(0,0,255),2)
            cv2.putText(frame1,str(id),(x2,y2),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
            cv2.circle(frame1,(x3,y3),4,(0,255,0),-1)   
            result1 = cv2.pointPolygonTest(np.array(area3,np.int32),((x3,y3)),False)
            if result1>0:
                area_3.add(id)
        cv2.polylines(frame1,[np.array(area3,np.int32)],True,(0,255,255),3)
        count1=len(area_3)
        cv2.putText(frame1,'Car Count :'+str(count1),(770,55),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.putText(frame1,'FPS:'+str(fps),(769,128),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.imshow("FRAME",frame1)
        if cv2.waitKey(1)& 0xFF==ord('d'):
            break
        if elapsed_time<=val:
            while True:
                board.digitalWrite(4,"HIGH")
                time.sleep(3)
                board.digitalWrite(4,"LOw")
                time.sleep(1)
                board.digitalWrite(3,"HIGH")
                time.sleep(2)
                board.digitalWrite(3,"LOW")
                time.sleep(1)

                break
            board.digitalWrite(2,"HIGH")
            cam2(10)

            break
    cap1.release()
    cv2.destroyAllWindows()
def cam2(val):
    board.digitalWrite(5,"LOW")
    start_time=time.time()
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    cap2=cv2.VideoCapture('traffic2.mp4')
    fps = cap2.get(cv2.CAP_PROP_FPS)
    count2=0
    tracker = Tracker()

    def POINTS(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE :  
            colorsBGR = [x, y]
            print(colorsBGR)
        

    cv2.namedWindow('FRAME')
    cv2.setMouseCallback('FRAME', POINTS)
    area3 =[(207,408),(196,439),(634,454),(599,410)]
    area_3=set()
    while True:
        elapsed_time=time.time()-start_time
        ret2,frame2=cap2.read()
        if not ret2:
            break
        count2 += 1
        if count2 % 3 != 0:
            continue
        frame2=cv2.resize(frame2,(1020,600))
        results2=model(frame2)
        list =[]
        for index,rows in results2.pandas().xyxy[0].iterrows():
            x=int(rows[0])
            y=int(rows[1])
            x1=int(rows[2])
            y1=int(rows[3])
            b=str(rows['name'])
            cv2.rectangle(frame2,(x,y),(x1,y1),(0,255,0),2)
            list.append([x,y,x1,y1])
        idx_bbox = tracker.update(list)
        for bbox in idx_bbox:
            x2,y2,x3,y3,id =bbox
            cv2.rectangle(frame2,(x2,y2),(x3,y3),(0,0,255),2)
            cv2.putText(frame2,str(id),(x2,y2),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
            cv2.circle(frame2,(x3,y3),4,(0,255,0),-1)   
            result2 = cv2.pointPolygonTest(np.array(area3,np.int32),((x3,y3)),False)
            if result2>0:
                area_3.add(id)
        cv2.polylines(frame2,[np.array(area3,np.int32)],True,(0,255,255),3)
        count2=len(area_3)
        cv2.putText(frame2,'Car Count :'+str(count2),(770,55),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.putText(frame2,'FPS:'+str(fps),(769,128),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.imshow("FRAME",frame2)
        if cv2.waitKey(1)& 0xFF==ord('d'):
            break
        if elapsed_time<=val:
            while True:
                board.digitalWrite(7,"HIGH")
                time.sleep(3)
                board.digitalWrite(7,"LOw")
                time.sleep(1)
                board.digitalWrite(6,"HIGH")
                time.sleep(2)
                board.digitalWrite(6,"LOW")
                time.sleep(1)
                
                break
            board.digitalWrite(5,"HIGH")
            cam3(10)
            break
    cap2.release()
    cv2.destroyAllWindows()
def cam3(val):
    board.digitalWrite(8,"LOW")
    start_time=time.time()
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    cap3=cv2.VideoCapture('traffic3.mp4')
    fps = cap3.get(cv2.CAP_PROP_FPS)
    count3=0
    tracker = Tracker()

    def POINTS(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE :  
            colorsBGR = [x, y]
            print(colorsBGR)
        

    cv2.namedWindow('FRAME')
    cv2.setMouseCallback('FRAME', POINTS)
    area3 =[(250,362),(213,385),(442,427),(460,378)]
    area_3=set()
    while True:
        elapsed_time=time.time()-start_time
        ret3,frame3=cap3.read()
        if not ret3:
            break
        count3 += 1
        if count3 % 3 != 0:
            continue
        frame3=cv2.resize(frame3,(1020,600))
        results3=model(frame3)
        list =[]
        for index,rows in results3.pandas().xyxy[0].iterrows():
            x=int(rows[0])
            y=int(rows[1])
            x1=int(rows[2])
            y1=int(rows[3])
            b=str(rows['name'])
            cv2.rectangle(frame3,(x,y),(x1,y1),(0,255,0),2)
            list.append([x,y,x1,y1])
        idx_bbox = tracker.update(list)
        for bbox in idx_bbox:
            x2,y2,x3,y3,id =bbox
            cv2.rectangle(frame3,(x2,y2),(x3,y3),(0,0,255),2)
            cv2.putText(frame3,str(id),(x2,y2),cv2.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
            cv2.circle(frame3,(x3,y3),4,(0,255,0),-1)   
            result3 = cv2.pointPolygonTest(np.array(area3,np.int32),((x3,y3)),False)
            if result3>0:
                area_3.add(id)
        cv2.polylines(frame3,[np.array(area3,np.int32)],True,(0,255,255),3)
        count3=len(area_3)
        cv2.putText(frame3,'Car Count :'+str(count3),(770,55),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.putText(frame3,'FPS:'+str(fps),(769,128),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv2.imshow("FRAME",frame3)
        if cv2.waitKey(1)& 0xFF==ord('d'):
            break
        if elapsed_time<=val:
            while True:
                board.digitalWrite(10,"HIGH")
                time.sleep(3)
                board.digitalWrite(10,"LOw")
                time.sleep(1)
                board.digitalWrite(9,"HIGH")
                time.sleep(2)
                board.digitalWrite(9,"LOW")
                time.sleep(1)
                break
            board.digitalWrite(8,"HIGH")
            cam1(10)
            break
    cap3.release()
    cv2.destroyAllWindows()
cam1(10)


