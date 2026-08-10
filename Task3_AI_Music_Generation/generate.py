import random
import pickle
import numpy as np

from music21 import note, stream, chord
from tensorflow.keras.models import load_model


# Load existing model
model = load_model("model.h5")

# Load notes
with open("notes.pkl", "rb") as file:
    notes = pickle.load(file)

pitchnames = sorted(set(notes))

note_to_int = {
    n: i for i, n in enumerate(pitchnames)
}

int_to_note = {
    i: n for n, i in note_to_int.items()
}

sequence_length = 100
n_vocab = len(pitchnames)

# IMPORTANT: existing model expects 512
model_vocab = model.input_shape[-1]

print("Notes in notes.pkl:", n_vocab)
print("Model expects:", model_vocab)

# Create starting pattern
start = random.randint(
    0,
    len(notes) - sequence_length - 1
)

pattern = [
    note_to_int[n]
    for n in notes[start:start + sequence_length]
]

prediction_output = []

print("Generating music...")

for i in range(200):

    # Create 512-feature input
    prediction_input = np.zeros(
        (1, sequence_length, model_vocab),
        dtype=np.float32
    )

    # Put our 326 notes into the first 326 positions
    for j, value in enumerate(pattern):

        if value < model_vocab:
            prediction_input[0, j, value] = 1.0

    # Predict
    prediction = model.predict(
        prediction_input,
        verbose=0
    )[0]

    # Only choose from the 326 notes we actually have
    valid_prediction = prediction[:n_vocab]

    index = np.argmax(valid_prediction)

    result = int_to_note[index]

    prediction_output.append(result)

    # Move pattern
    pattern = pattern[1:]
    pattern.append(index)


print("Notes generated!")

# Convert to MIDI
output_notes = []
offset = 0

for pattern_note in prediction_output:

    try:

        if "." in pattern_note:

            chord_notes = []

            for current_note in pattern_note.split("."):

                new_note = note.Note(
                    int(current_note)
                )

                chord_notes.append(new_note)

            new_chord = chord.Chord(
                chord_notes
            )

            new_chord.offset = offset
            output_notes.append(new_chord)

        else:

            new_note = note.Note(pattern_note)

            new_note.offset = offset

            output_notes.append(new_note)

    except:
        pass

    offset += 0.5


# Save MIDI
midi_stream = stream.Stream(output_notes)

midi_stream.write(
    "midi",
    fp="generated_music.mid"
)

print()
print("==============================")
print("Music Generated!")
print("==============================")
print("File: generated_music.mid")
print("==============================")