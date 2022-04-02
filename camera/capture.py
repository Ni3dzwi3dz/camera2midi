import cv2 as cv

class ScreenCapture:

    def __init__(self, neighbors: int, size: int, faceXML: str = r'haarcascade_frontalface_default.xml',
                 palmXML: str = r'palm.xml' ):
        self.neighbors = neighbors
        self.size = size

        self.faces=[]
        self.palms=[]

        self.faceCascade = faceCascade = cv.CascadeClassifier(faceXml)
        self.palmCascade = palmCascade = cv.CascadeClassifier(palmXml)


    def run(self):

palmXml =


video_capture = cv.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y,), (x+w, y+h), (0, 255, 0), 2)

    palms = palmCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(5, 5)
    )

    for (x, y, w, h) in palms:
        cv.rectangle(frame, (x, y,), (x+w, y+h), (0, 0, 255), 2)
    cv.imshow("Video", frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv.destroyAllWindows()
