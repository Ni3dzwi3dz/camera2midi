from camera.capture import ScreenCapture
from midi.midi import MidiController

import os
from time import sleep
import threading
import numpy

class cameraMidiController:

    def __init__(self, interval: float):

        faceXML = os.path.join(os.getcwd() + "\\camera\\haarcascade_frontalface_default.xml")
        palmXML = os.path.join(os.getcwd() + "\\camera\\palm.xml")

        self.camera = ScreenCapture(5, 50, faceXML, palmXML)
        self.midi = MidiController()

        self.interval = interval

    def normalize(self, note: numpy.ndarray) -> numpy.ndarray:

        width = self.camera.video_capture.get(3)
        height = self.camera.video_capture.get(4)

        for i, number in enumerate(note):
            if i % 2 == 0:
                note[i] = (number / width) * 128
            else:
                note[i] = (number / height) * 128

        return note

    def check_notes(self) -> None:

        while True:
            for note in self.camera.palms:
                new_note = self.normalize(note)

                midi_message = [0x90, new_note[1], new_note[0]]
                self.midi.send_note(midi_message)


            sleep(self.interval)

    def run(self):

        threads = list()

        threads.append(threading.Thread(target=self.camera.run))
        threads.append(threading.Thread(target=self.check_notes))

        for thread in threads:
            print('Starting thread')
            thread.start()

        for thread in threads:
            thread.join()





if __name__ == '__main__':
    control = cameraMidiController(0.5)

    control.run()


