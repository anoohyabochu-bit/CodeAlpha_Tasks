# 🎵 AI Music Generation using LSTM

## 📌 Project Description

This project is an **AI-based Music Generation System** that uses a deep learning model called **LSTM (Long Short-Term Memory)** to learn musical patterns from MIDI files and generate new music.

The project uses `music21` to preprocess MIDI files, extracts musical notes, trains an LSTM neural network, and generates a new MIDI file.

The generated music is saved as:

```text
generated_music.mid


🎯 Objective
The main objectives of this project are:
Collect MIDI music data.
Preprocess MIDI files using music21.
Extract musical notes and chords.
Store the extracted notes in a file.
Create sequences of musical notes for training.
Build an LSTM deep learning model.
Train the model on musical sequences.
Generate new musical notes.
Convert generated notes into a MIDI file.
Save and play the generated music.


🧠 Technologies Used
Python
TensorFlow
Keras
LSTM (Long Short-Term Memory)
music21
NumPy
Pickle
MIDI


📂 Project Structure
alpha_Musicgeneration/
│
├── dataset/
│   ├── song1.mid
│   ├── song2.mid
│   ├── song3.mid
│   └── ...
│
├── preprocess.py
├── train.py
├── generate.py
├── notes.pkl
├── model.h5
├── generated_music.mid
└── README.md


📄 File Description
File
Description
dataset/
Contains MIDI music files used for training
preprocess.py
Extracts notes from MIDI files
notes.pkl
Stores extracted musical notes
train.py
Builds and trains the LSTM model
model.h5
Saved trained AI model
generate.py
Generates new musical notes
generated_music.mid
AI-generated MIDI music
README.md
Project documentation


⚙️ How the Project Works
The project follows this workflow:
MIDI Dataset
     ↓
preprocess.py
     ↓
Extract Notes and Chords
     ↓
notes.pkl
     ↓
train.py
     ↓
LSTM Model
     ↓
model.h5
     ↓
generate.py
     ↓
Generate New Notes
     ↓
Convert Notes to MIDI
     ↓
generated_music.mid


📥 1. Collect MIDI Dataset
MIDI music files are collected and placed inside the dataset folder.
Example:
dataset/
├── song1.mid
├── song2.mid
├── song3.mid
└── song4.mid
MIDI files contain musical information such as:
Notes
Chords
Pitch
Timing
Duration


🎼 2. Preprocess MIDI Data
The preprocess.py program uses the music21 library to read MIDI files and extract musical notes and chords.
The extracted notes are saved into:
notes.pkl
Run preprocessing
Open the VS Code terminal and run:
python preprocess.py
Example output:
Starting MIDI preprocessing...
MIDI files found: 10
Processing: dataset/song1.mid
Processing: dataset/song2.mid
Processing: dataset/song3.mid

Total notes: 5000
Preprocessing completed!
Notes saved as notes.pkl
The notes.pkl file is then used by the training program.


🧠 3. Create the LSTM Model
The project uses an LSTM (Long Short-Term Memory) neural network.
LSTM is a type of Recurrent Neural Network (RNN) that is useful for sequential data.
Music is sequential because one note follows another.
For example:
C → E → G → C
The LSTM learns relationships between previous notes and predicts the next musical note.


🏗️ Model Architecture
Input Sequence
      ↓
LSTM (128 units)
      ↓
Dropout (0.3)
      ↓
LSTM (128 units)
      ↓
Dense (128 units)
      ↓
Dropout (0.2)
      ↓
Output Layer
      ↓
Next Musical Note


🏋️ 4. Train the Model
After preprocessing the MIDI files, run:
python train.py
The training program:
Loads notes.pkl.
Converts musical notes into numbers.
Creates sequences of 100 notes.
Creates training input and output.
Builds the LSTM model.
Trains the model.
Saves the trained model as model.h5.
Example:
Loading notes...
Total notes: 5000
Preparing data...
Building model...
Starting training...

Training completed!
Model saved as model.h5


🎵 5. Generate New Music
After the model has been trained, run:
python generate.py
The program:
Loads the trained model.h5.
Loads notes.pkl.
Selects a starting sequence.
Predicts new musical notes.
Repeatedly predicts the next note.
Converts the generated notes into MIDI format.
Saves the generated music.
The output file is:
generated_music.mid
Example output:
Loading model...
Loading notes...
Different notes: 326
Generating music...
Notes generated!

==============================
Music Generated!
==============================
File: generated_music.mid
==============================


▶️ 6. Play the Generated Music
After running generate.py, open the project folder:
alpha_Musicgeneration/
Find:
generated_music.mid
Double-click the MIDI file and open it with a MIDI-compatible music player.
The generated music can then be listened to.


📦 Installation
Make sure Python is installed on your computer.
Install the required libraries using:
pip install numpy tensorflow music21
If TensorFlow is already installed, you do not need to install it again.


🚀 How to Run the Complete Project
Follow these steps in order.
Step 1: Open the project
Open the alpha_Musicgeneration folder in VS Code.
Step 2: Install libraries
pip install numpy tensorflow music21
Step 3: Add MIDI files
Place your MIDI files inside:
dataset/
Step 4: Preprocess the MIDI files
Run:
python preprocess.py
This creates:
notes.pkl
Step 5: Train the AI model
Run:
python train.py
This creates:
model.h5
Step 6: Generate music
Run:
python generate.py
This creates:
generated_music.mid
Step 7: Play the generated music
Open:
generated_music.mid
using a MIDI-compatible music player.


🔄 Complete Project Flow
       MIDI Files
           ↓
     MIDI Dataset
           ↓
     preprocess.py
           ↓
    Extract Notes
           ↓
       notes.pkl
           ↓
       train.py
           ↓
     LSTM Network
           ↓
       Train Model
           ↓
        model.h5
           ↓
      generate.py
           ↓
   Predict New Notes
           ↓
    Convert to MIDI
           ↓
generated_music.mid
           ↓
      Play Music 🎵


✨ Features
🎼 MIDI music dataset processing
🎵 Musical note extraction
🧠 LSTM-based deep learning
🔢 Musical sequence prediction
🤖 Automatic music generation
💾 MIDI file generation
▶️ Generated music playback


⚠️ Limitations
The quality of generated music depends on the training dataset.
A small dataset may produce repetitive music.
LSTM training can take considerable time.
MIDI files require a compatible player or synthesizer for playback.
Generated music may not always have perfect musical structure.
The model learns patterns from the supplied MIDI dataset and does not create music with human-level musical understanding.

🔮 Future Improvements
The project can be improved by adding:
🎹 More MIDI training data
🎵 Multiple music genres
🎚️ Tempo control
🎸 Instrument selection
🎧 WAV/MP3 audio conversion
🖥️ Graphical User Interface (GUI)
🤖 More advanced deep learning models
🎶 GAN-based music generation
🌐 Web-based music generation
🎼 Better rhythm and duration prediction


📝 Conclusion
This project demonstrates how Artificial Intelligence and Deep Learning can be used to generate music.
MIDI files are first processed using music21 to extract musical notes. These notes are converted into sequences and used to train an LSTM neural network.
The trained model learns musical patterns and predicts new notes. The generated notes are then converted into a MIDI file using music21.
The final output is:
generated_music.mid
This project demonstrates the use of RNN/LSTM techniques for AI-based music generation.

👨‍💻 Project Information
Project Title: Music Generation with AI
Task: Task 3 - Music Generation with AI
Programming Language: Python
Deep Learning Model: LSTM
Type of Neural Network: Recurrent Neural Network (RNN)
Input: MIDI Music Dataset
Preprocessing: music21
Output: Generated MIDI Music
Output File:
generated_music.mid


📊 Task 3 Requirements
Requirement
Status
Collect MIDI music data
✅ Completed
Preprocess MIDI data
✅ Completed
Extract musical notes
✅ Completed
Create note sequences
✅ Completed
Build RNN/LSTM model
✅ Completed
Train the model
✅ Completed
Generate new music
✅ Completed
Convert generated notes to MIDI
✅ Completed
Save generated music
✅ Completed
Play generated music
✅ Supported


🎉 Project Status
TASK 3: MUSIC GENERATION WITH AI — COMPLETED ✅
The project successfully uses an LSTM neural network to learn musical patterns from MIDI data and generate new musical sequences.
The generated music is saved as:
generated_music.mid

🎵 AI Music Generation Project Completed Successfully!