import cv2
import pathlib
import serial #handles the serial ports
import QboController
cascade_path = pathlib.Path(cv2.__file__).parent.absolute()/"data/haarcascade_frontalface_default.xml"
clf = cv2.CascadeClassifier(str(cascade_path))

# port = '/dev/serial0'
# ser = serial.Serial(port, baudrate=115200, bytesize = serial.EIGHTBITS, stopbits = serial.STOPBITS_ONE, parity = serial.PARITY_NONE, rtscts = False, dsrdtr =False, timeout = 0)
# QBO = QboController.Controller(ser)


cap = cv2.VideoCapture(0)
success, img = cap.read()
rows, cols, _ = img.shape
center = int(cols/2)

xDefault = 511
yDefault = 450
xMax = 725
xMin = 290

# QBO.SetServo(1, xDefault, 100)#Axis,Angle,Speed (X Axis)
# QBO.SetServo(2, yDefault, 100)#Axis,Angle,Speed (Y Axis)

#command = False
while True:
    #command = audio.listen()
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
    )

    for (x,y,width,height) in faces:
        cv2.rectangle(img,(x,y),(x+width, y+height), (255,255,0),2)
        x_medium = int((x + x + width)/2)

    cv2.line(img, (x_medium, 0), (x_medium, 480), (0,255,0), 2)
    cv2.line(img, (center, 0), (center, 480), (255, 255, 0), 2)
    cv2.imshow("Faces", img)

    #command = audio.listen()
    try:
        print("Listening...")
        #command = audio.listen()
    except:
        print("Waiting...")

    #if(command == "Follow")
    if x_medium < center:
        xDefault += 1
    elif x_medium > center:
        xDefault -= 1
    #QBO.SetServo(1, xDefault, 100)
    #QBO.SetServo(2, yDefault, 100)
    print("X: ",xDefault)


    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
