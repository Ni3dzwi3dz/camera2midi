import cv2 as cv
import os

class ScreenCapture:

    def __init__(self, neighbors: int, size: int, faceXML: str = r'haarcascade_frontalface_default.xml',
                 palmXML: str = r'palm.xml' ):
        self.neighbors = neighbors
        self.size = size

        self.faces=[]
        self.palms=[]

        self.faceCascade = faceCascade = cv.CascadeClassifier(faceXML)
        self.palmCascade = palmCascade = cv.CascadeClassifier(palmXML)

        self.video_capture = cv.VideoCapture(0)


    def run(self) -> None:

        while True:
            ret, frame = self.video_capture.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            self.faces = self.faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=self.neighbors,
                minSize=(self.size, self.size)
            )

            for (x, y, w, h) in self.faces:
                cv.rectangle(frame, (x, y,), (x+w, y+h), (0, 255, 0), 2)

            self.palms = self.palmCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=self.neighbors,
                minSize=(int(self.size/10), int(self.size/10))
            )

            for (x, y, w, h) in self.palms:
                cv.rectangle(frame, (x, y,), (x+w, y+h), (0, 0, 255), 2)
            cv.imshow("Video", frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv.destroyAllWindows()

if __name__ == '__main__':
    capture = ScreenCapture(5,50)
    capture.run()