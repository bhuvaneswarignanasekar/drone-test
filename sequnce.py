import cv2
from PIL import Image
from Tello import Tello

def action():
    print("start action")
    t=Tello()
    print("tello initialized")
    print(t.connect())
    
    t.streamon()
    t.takeoff()
    counter=0
    img=[]
    
    
    while True:
        if(counter==10000):
            t.land()
        try:
            
            frame_read=t.get_frame_read()
            a= frame_read.frame
            
            im = Image.fromarray(a)
            im.save("your_file_"+str(counter)+".jpeg")
            t.rotate_clockwise(10)
        except:
            e = sys.exc_info()[0]
            write_to_page( "<p>Error: %s</p>" % e )
        counter=counter+1
    cv2.destroyAllWindows() 
    #video.release()       
    out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    for i in range(len(img)):
        out.write(img_array[i])
        out.release()
    