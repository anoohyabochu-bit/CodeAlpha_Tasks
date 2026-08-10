import numpy as np
import pickle

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

print("Loading notes...")

sequence_length = 100

notes = pickle.load(open("notes.pkl", "rb"))

pitchnames = sorted(set(notes))
note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

network_input = []
network_output = []

print("Preparing data...")

for i in range(len(notes) - sequence_length):
    sequence_in = notes[i:i + sequence_length]
    sequence_out = notes[i + sequence_length]

    network_input.append([note_to_int[n] for n in sequence_in])
    network_output.append(note_to_int[sequence_out])

n_vocab = len(pitchnames)

network_input = np.reshape(
    network_input,
    (len(network_input), sequence_length, 1)
)

network_input = network_input / float(n_vocab)
network_output = to_categorical(network_output)

print("Building model...")

model = Sequential()

model.add(LSTM(
    128,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))

model.add(Dropout(0.3))

model.add(LSTM(128))

model.add(Dense(128, activation="relu"))

model.add(Dropout(0.2))

model.add(Dense(n_vocab, activation="softmax"))

model.compile(
    loss="categorical_crossentropy",
    optimizer="adam",
    metrics=["accuracy"]
)

print("Starting training...")

model.fit(
    network_input,
    network_output,
    epochs=50,
    batch_size=64,
    verbose=1
)

model.save("model.h5")

print("Training completed!")
print("Model saved as model.h5")