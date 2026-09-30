import cv2
face_finder = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")  # 1. Load the face finder
camera = cv2.VideoCapture(0)                                     # 2. Turn on the camera
while True:                                                      # Repeat again and again
    ok, picture = camera.read()                                  # 3. Take a picture
    faces = face_finder.detectMultiScale(cv2.cvtColor(picture, cv2.COLOR_BGR2GRAY), 1.3, 6)  # 4. Make it gray, then find faces
    for x, y, w, h in faces: cv2.rectangle(picture, (x, y), (x + w, y + h), (255, 0, 0), 2)  # 5. Draw a blue box (x=left, y=top, w=width, h=height)
    cv2.imshow("Face Detection", picture)                        # 6. Show the picture
    if cv2.waitKey(40) & 0xFF == ord("q"): break                 # 7. Press q to stop
camera.release(); cv2.destroyAllWindows()                        # 8. Turn off the camera