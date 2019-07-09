from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import mysql.connector
from mysql.connector import Error

def database():
    try:
        mySQLconnection = mysql.connector.connect(host='localhost',
                                                  database='dnb_database',
                                                  user='root',
                                                  password='')
        sql_select_Query = "select * from isync"
        cursor = mySQLconnection .cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of rows in python_developers is - ", cursor.rowcount)
        print ("Printing each row's column values i.e.  developer record")
        for row in records:
            print("Id = ", row[0], )
            print("Name = ", row[1])
            print("JoiningDate  = ", row[2])
            print("Salary  = ", row[3], "\n")
    except Error as e :
         print ("Error while connecting to MySQL", e)

    return records
    cursor.close()
def decode(im,records):
    
    decodedObjects = pyzbar.decode(im)
    for obj in decodedObjects:
        for row in records:
            str3 =str(row[0])
            str4 =str(row[1])
            str5 =str(row[3])+"'"
            str1 =str(obj.data)
            strlen = len(str1)
            str6 = str1[ strlen-8: ]
            
            
            
            str2 = str6
           
            
            
            if(str2 == str5):
                print("your name is:"+str3+" "+str4)
                break
         
       
    
           
            
    
    return decodedObjects  
def display(im,deocdedObjects):
    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        points = decodedObject.polygon
 
    # If the points do not form a quad, find convex hull
        if len(points) > 4 : 
          hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
          hull = list(map(tuple, np.squeeze(hull)))
        else : 
          hull = points;
     
    # Number of points in the convex hull
        n = len(hull)
 
    # Draw the convext hull
        for j in range(0,n):
          cv2.line(im, hull[j], hull[ (j+1) % n], (255,0,0), 3)
   
    # Display results 
    


if __name__ == '__main__':
        cap = cv2.VideoCapture(0)
        records = database()
            
        while (True):
            ret,frame = cap.read()
            im = frame
            cv2.imshow("Results", im)
            decodedObjects= decode(im,records)
            
            
            #print("it reaches here")
            display(im,decodedObjects)
           #print("this reaches here")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cap.release()
                cap.destroyAllWindows()
     
