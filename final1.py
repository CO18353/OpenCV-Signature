from tkinter import*
import time
import pymysql
import cv2
import numpy as np
from collections import deque
from PIL import Image
pic=0
url_sign=r"C:\\Users\\Tanveer\\Documents\\Python\\Sign"
url_pic=r"C:\\Users\\Tanveer\\Documents\\Python\\DP"
url_sign1=r"C:\Users\Tanveer\Documents\Python\Sign"
url_pic1=r"C:\Users\Tanveer\Documents\Python\DP"

fread= open("count.txt", "r")  
x= fread.read()
fread.close()
co=int(x,10)

root=Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Registration")
background_image=PhotoImage(file="wood2.gif")
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


localtime=time.asctime(time.localtime(time.time()))
lblinfo = Label(root, font=( 'Helvetica ' ,30, 'bold' ),bg='Black',text="Registration Form",fg="white",bd=0)
lblinfo.place(x=500,y=10)
lblinfo = Label(root, font=( 'Helvetica ' ,20 ),bg='Black',text=localtime,fg="white",bd=0)
lblinfo.place(x=513,y=70)

lblname = Label(root, font=( 'Helvetica' ,16, 'bold' ),text="FIRST NAME",bg='LightSalmon4',bd=0,fg="White",anchor='w')
lblname.place(x=20,y=204)
txtname = Entry(root,font=('Helvetica' ,16),fg='Gray20', bd=6,insertwidth=4,bg="white" ,justify='left')
txtname.place(x=225,y=200)

lbllname = Label(root, font=( 'Helvetica' ,16, 'bold' ),text="LAST NAME",bg='LightSalmon4',fg="White",bd=0,anchor='w')
lbllname.place(x=20,y=254)
txtlname = Entry(root,font=('Helvetica' ,16),  bd=6,fg='Gray20',insertwidth=4,bg="white" ,justify='left')
txtlname.place(x=225,y=250)

lbld= Label(root, font=( 'Helvetica' ,16, 'bold' ),text="DOB",bg='LightSalmon4',fg="White",bd=0,anchor='w')
lbld.place(x=20,y=304)
txtd = Entry(root,font=('Helvetica' ,16),fg='Gray20',  bd=6,insertwidth=4,bg="white" ,justify='left')
txtd.place(x=225,y=300)
txtd.insert(0,"dd/mm/yyyy")

lble = Label(root, font=( 'Helvetica' ,16, 'bold' ),text="EMAIL ID",bg='LightSalmon4',fg="White",bd=0,anchor='w')
lble.place(x=20,y=354)
txte = Entry(root,font=('Helvetica' ,16),fg='Gray20',  bd=6,insertwidth=4,bg="white" ,justify='left')
txte.place(x=225,y=350)

lblac = Label(root, font=( 'Helvetica' ,16, 'bold' ),text="AADHAR NUMBER",bg='LightSalmon4',fg="White",bd=0,anchor='w')
lblac.place(x=20,y=404)
txtac = Entry(root,font=('Helvetica' ,16),fg='Gray20',  bd=6,insertwidth=4,bg="white" ,justify='left')
txtac.place(x=225,y=400)
txtac.insert(0,"No spaces")

def exw():
    root.destroy()
def ttnw():
    roo = Toplevel()
    roo.title("Photo & Signature")
    w1, h1 = roo.winfo_screenwidth(), roo.winfo_screenheight()
    roo.geometry("%dx%d+0+0" % (w1, h1-100))
    background_image1=PhotoImage(file="wood2.gif")
    background_label1= Label(roo, image=background_image)
    background_label1.place(x=0, y=0, relwidth=1, relheight=1)
    def exitw():
        roo.destroy()
    def signw():
        pic=0
        fread= open("count.txt", "r")  
        x= fread.read()
        fread.close()
        co=int(x,10)
        start=1
        count=0
        done = 0
        found=0
        plot=0

        if __name__ == '__main__':

            img = 255*np.ones((512,512,3), np.uint8)
            cap = cv2.VideoCapture(0)
            points = deque(maxlen=1024)
            #points2 = deque(maxlen=512)

            kernel = np.ones((5, 5), np.uint8)
            while True:
                ret, frame = cap.read()
                frame = cv2.flip(frame, 1)

                if done!=1:
                    roi=frame[90:470]
                    #roi2 = frame[100:350, 60:600]

                colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
                frame = cv2.rectangle(frame, (1, 160), (65, 255), colors[2], -1)
                frame = cv2.rectangle(frame, (570, 160), (635, 255), colors[2], -1)
                frame = cv2.rectangle(frame, (85,100),(540,350), colors[2],3)
                frame = cv2.rectangle(frame, (250, 410), (380, 470), colors[2], -1)

                cv2.putText(frame, "START", (10, 185), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "DONE", (580,185), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "RETAKE", (270, 440), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

                if not ret:
                    break

                lower_green = np.array([56, 75, 46])
                upper_green = np.array([98, 255, 171])

                '''lower_green = np.array([13, 76, 59])
                upper_green = np.array([101, 255, 138])'''

                '''lower_blue = np.array([69, 94, 196])
                upper_blue = np.array([179, 255, 255])
                '''

                lower_blue = np.array([110, 153, 69])
                upper_blue = np.array([179, 255, 255])

                # a threshold for the hsv image to get only green colours
                mask_green = cv2.inRange(hsv, lower_green, upper_green)
                mask_green = cv2.erode(mask_green, kernel, iterations=2)
                mask_green = cv2.morphologyEx(mask_green, cv2.MORPH_OPEN, kernel)
                mask_green = cv2.dilate(mask_green, kernel, iterations=1)

                #bue mask
                mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
                mask_blue = cv2.erode(mask_blue, kernel, iterations=2)
                mask_blue = cv2.morphologyEx(mask_blue, cv2.MORPH_OPEN, kernel)
                mask_blue = cv2.dilate(mask_blue, kernel, iterations=1)

                #green contour
                contours, hier = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

               #blue contour
                contours_blue, hier2 = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                center = None
                center_blue = None

                if len(contours) > 0:
                    # Sort the contours and find the largest one -- we
                    # will assume this contour correspondes to the area of the bottle cap
                    cnt = sorted(contours, key=cv2.contourArea, reverse=True)[0]
                    # Get the radius of the enclosing circle around the found contour
                    #find the circumcircle of an object using the function cv2.minEnclosingCircle().It is a circle which completely covers the object with minimum area.
                    ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                    # Draw the circle around the contour
                    cv2.circle(roi, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    # Get the moments to calculate the center of the contour (in this case Circle)
                    #function cv2.moments() gives a dictionary of all moment values calculated
                    M = cv2.moments(cnt)
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))
                    points.appendleft(center)

                if count == 1:
                    if start == 1:
                        while len(points) > 1:
                            points.pop()
                            points.popleft()
                            start = 0

                    else:
                        for i in range(1, len(points)):
                            if points[i - 1] is None or points[i] is None:
                                continue
                            elif (points[i - 1][0] <= 130 and points[i][0] <= 130) or (points[i - 1][0] >= 500 and points[i][0] >= 500):
                                continue
                            else:
                                cv2.line(roi, points[i - 1], points[i], (0, 0, 0), 3)
                                cv2.line(img, points[i - 1], points[i], (0, 0, 0), 3)
                                plot=1


                if len(contours_blue) > 0:
                    cnt2 = sorted(contours_blue, key=cv2.contourArea, reverse=True)[0]
                    ((x_b, y_b), radius_b) = cv2.minEnclosingCircle(cnt2)
                    cv2.circle(roi, (int(x_b), int(y_b)), int(radius_b), (0, 255, 255), 2)
                    found=1
                    M_b = cv2.moments(cnt2)
                    cx_b = int(M_b['m10'] / M_b['m00'])
                    cy_b = int(M_b['m01'] / M_b['m00'])
                    center = (int(M_b['m10'] / M_b['m00']), int(M_b['m01'] / M_b['m00']))

                    if cx_b >= 260 and cx_b <= 410 and cy_b >= 300 and cy_b <= 350:
                        if start!=1:
                            '''while len(points)>0:
                                points.pop()
                                points.popleft()
                            '''
                            #cap.release()
                            #cv2.destroyAllWindows()
                            start=1
                            img = 255*np.ones((512, 512, 3), np.uint8)
                            frame = cv2.resize(frame, (640, 480))
                            img = cv2.resize(img, (640, 480))
                            Signature = np.concatenate((frame, img), axis=1)
                            cv2.imshow("Signature", Signature)


                    if cx_b >= 0 and cx_b <= 100 and cy_b >= 70 and cy_b <= 150:
                        if start == 1:
                            count = 1

                    elif cx_b >= 570 and cx_b <= 635 and cy_b >= 160 and cy_b <= 255:
                        if start != 1:
                            done = 1
                            cv2.imwrite("Sign{}.png".format(co),img)
                            x=str(co)
                            image2 = Image.open(url_sign1+x+".png")
                            wpercent = (250/float(image2.size[0]))
                            hsize = int((float(image2.size[1])*float(wpercent)))
                            image2 = image2.resize((250,hsize), Image.ANTIALIAS)
                            image2.save(url_sign1+x+".gif")
                            pic=pic+1
                            if pic>0:
                                logo2 = PhotoImage(file=url_sign1+x+".gif")
                                w2 = Label(roo, image=logo2)
                                w2.image = logo2 # keep a reference!
                                w2.place(x=750,y=100)
                                roo.update_idletasks()
                            co=co+1
                            x=str(co)
                            fwrite=open("count.txt","w")
                            fwrite.write(x)
                            fwrite.close()
                            cap.release()
                            cv2.destroyAllWindows()

                if found == 1 and start == 0 and plot == 1:
                    while len(points) > 1:
                        points.pop()
                        points.popleft()
                        found=0

                frame = cv2.resize(frame, (640, 480))
                img = cv2.resize(img, (640, 480))
                Signature = np.concatenate((frame, img), axis=1)
                cv2.imshow("Signature", Signature)
                key = cv2.waitKey(1)
                if key == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
    def picw():
        pic=0
        video_capture = cv2.VideoCapture(0)
        cv2.namedWindow("Smile!")
        while True: 
        # Captures video_capture frame by frame 
                ret, frame = video_capture.read()
                frame = cv2.flip(frame, 1)
                cv2.imshow("Smile!", frame)
                if not ret: 
                    break
                # The control breaks once q key is pressed
                k=cv2.waitKey(1)
                if k%256 == 32:
                # SPACE pressed
                    cv2.imwrite("DP{}.png".format(co), frame)                 
                    break

        # Release the capture once all the processing is done. 
        video_capture.release()								 
        cv2.destroyAllWindows()
        
        image = Image.open(url_pic1+x+".png")
        wpercent = (250/float(image.size[0]))
        hsize = int((float(image.size[1])*float(wpercent)))
        image = image.resize((250,hsize), Image.ANTIALIAS)
        image.save(url_pic1+x+".gif")                
        pic=pic+1
        if pic>0:
            logo = PhotoImage(file=url_pic1+x+".gif")
            w1 = Label(roo, image=logo)
            w1.image = logo #keep a reference!
            w1.place(x=300,y=100)
            roo.update_idletasks()
    def nxtw():
        db=pymysql.connect("localhost","root","","ccet")
        cursor=db.cursor()
        sql="INSERT INTO STUDENT VALUES('%s','%s','%s','%s','%s','%s','%s')" % (txtname.get(),txtlname.get(),txtd.get(),txtac.get(),txte.get(),url_pic+x+".png",url_sign+x+".png");
        cursor.execute(sql)
        db.commit()
        db.close()
        las = Toplevel()
        las.title("Your Details")
        w2, h2 =las.winfo_screenwidth(), roo.winfo_screenheight()
        las.geometry("%dx%d+0+0" % (w2, h2))
        background_image1=PhotoImage(file="wood2.gif")
        background_label1= Label(las, image=background_image)
        background_label1.place(x=0, y=0, relwidth=1, relheight=1)
        #
        lbldet=Label(las, font=( 'Helvetica' ,30, 'bold' ),text="Details of "+txtname.get()+":",bg='Black',fg="White",bd=0,anchor='w')
        lbldet.place(x=500,y=10)
        lblname1 = Label(las, font=( 'Helvetica' ,16, 'bold' ),text="FIRST NAME",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        lblname1.place(x=20,y=204)
        txtname1 = Label(las,font=('Helvetica' ,16),fg='Gray20', bd=6,text=txtname.get(),bg="white")
        txtname1.place(x=225,y=200)

        lbllname1 = Label(las, font=( 'Helvetica' ,16, 'bold' ),text="LAST NAME",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        lbllname1.place(x=20,y=254)
        txtname2 = Label(las,font=('Helvetica' ,16),fg='Gray20', bd=6,text=txtlname.get(),bg="white")
        txtname2.place(x=225,y=250)

        lbld1= Label(las, font=( 'Helvetica' ,16, 'bold' ),text="DOB",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        lbld1.place(x=20,y=304)
        txtd1 = Label(las,font=('Helvetica' ,16),fg='Gray20', bd=6,text=txtd.get(),bg="white")
        txtd1.place(x=225,y=300)
        
        lble1 = Label(las, font=( 'Helvetica' ,16, 'bold' ),text="EMAIL ID",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        lble1.place(x=20,y=354)
        txte1 = Label(las,font=('Helvetica' ,16),fg='Gray20', bd=6,text=txte.get(),bg="white")
        txte1.place(x=225,y=350)

        lblac1 = Label(las, font=( 'Helvetica' ,16, 'bold' ),text="AADHAR NUMBER",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        lblac1.place(x=20,y=404)
        txtac1 = Label(las,font=('Helvetica' ,16),fg='Gray20', bd=6,text=txtac.get(),bg="white")
        txtac1.place(x=225,y=400)

        piclbl= PhotoImage(file=url_pic1+x+".gif")
        p1 = Label(las, image=piclbl)
        p1.place(x=500,y=250)
        pictxt1=Label(las, font=( 'Helvetica' ,16, 'bold' ),text="PHOTO",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        pictxt1.place(x=560,y=510)
        piclb2= PhotoImage(file=url_sign1+x+".gif")
        p2 = Label(las, image=piclb2)
        p2.place(x=804,y=250)
        pictxt2=Label(las, font=( 'Helvetica' ,16, 'bold' ),text="SIGNATURE",bg='LightSalmon4',fg="White",bd=0,anchor='w')
        pictxt2.place(x=850,y=510)
        #
        def byew():
            las.destroy()
        btnsub=Button(las,padx=20,pady=16, bd=10 ,fg="RED4",font=(50),width=10, text="Exit", bg="Snow",command=byew)
        btnsub.place(x=600, y=550)
        las.mainloop()

    
    roo.update_idletasks()
    btnph=Button(roo,padx=20,pady=16, bd=10 ,fg="Green",font=(50),width=10, text="Take Photo", bg="Snow",command=picw)
    btnph.place(x=350,y=400)
    btnsi=Button(roo,padx=20,pady=16, bd=10 ,fg="Green",font=(50),width=10, text="Put Signature", bg="Snow",command=signw)
    btnsi.place(x=800,y=400)
    btnnxt=Button(roo,padx=20,pady=16, bd=10 ,fg="RED4",font=(50),width=10, text="Submit", bg="Snow",command=nxtw)
    btnnxt.place(x=700,y=550)
    btnexit=Button(roo,padx=20,pady=16, bd=10 ,fg="RED4",font=(50),width=10, text="Exit", bg="Snow",command=exitw)
    btnexit.place(x=500,y=550)
    roo.mainloop()
###########################################################################################################################################################
    
btnex=Button(root,padx=20,pady=16, bd=10 ,fg="Green",font=(50),width=10, text="Next", bg="Snow",command=ttnw)
#btnex.grid(row=0, column=3)
btnex.place(x=700,y=550)
btnexit=Button(root,padx=20,pady=16, bd=10 ,fg="RED4",font=(50),width=10, text="Exit", bg="Snow",command=exw)
#btnexit.grid(row=0, column=5)
btnexit.place(x=500,y=550)
root.mainloop()
###########################################################################################################################################################
