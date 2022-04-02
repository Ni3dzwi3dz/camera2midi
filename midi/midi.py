import time
import rtmidi as rt

class MidiController:

    def __init__(self):
        self.midiOut = rt.MidiOut()
        self.port = self.set_port()

        if self.port != -1:
            self.midiOut.open_port(self.port)
        else:
            self.midiOut.open_virtual_port('That`s only thing we`ve got')

    def set_port(self) -> int:

        avaiablePorts = self.midiOut.get_ports()

        for i, port in enumerate(avaiablePorts):
            if 'loop' in port:
                print(f'Setting port to {i}')
                return i
        # in case, that loopMidi is not running, i`m returning -1, as a note, that we need to open virtual port

        return -1

    def send_note(self, note: list) -> None:
        self.midiOut.send_message(note)
        
        
if __name__ == '__main__':
    control = MidiController()

    while True:
        control.send_note([0x90, 60, 112])
        time.sleep(0.5)
        control.send_note([0x90, 60, 0])
        time.sleep(0.5)
