from MidiData import MidiData
import matplotlib.pyplot as plt
import numpy as np

__FILENAME__ = "135_epochs_reduced_notes.mid"

midiData = MidiData(__FILENAME__)
trackData = midiData.getTrack(0)

notes = trackData.notes
note_dict = {}

for note in notes:
    note_pitch = note.PITCH_DICTIONARY[note.pitch]
    if note_pitch not in note_dict:
        note_dict[note_pitch] = 1
    else:
        note_dict[note_pitch] += 1

print("# of Notes " + str(len(trackData.notes)))

# plot
fig, ax = plt.subplots()

plt.bar(range(len(note_dict)), list(note_dict.values()), align='center')
plt.xticks(range(len(note_dict)), list(note_dict.keys()))

plt.show()

import music21
score = music21.converter.parse(__FILENAME__)
key = score.analyze('key')

print(key.tonic.name, key.mode)
print(score[music21.meter.TimeSignature][0])
