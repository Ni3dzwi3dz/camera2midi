import time
import rtmidi as rt

midiOut = rt.MidiOut()
avaiablePorts = midiOut.get_ports()

print(avaiablePorts)