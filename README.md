# Drowsiness Detection System

This Python script detects drowsiness in real-time using facial landmarks and eye aspect ratio (EAR). It utilizes the `dlib` library for face detection and facial landmark prediction.

## Requirements

- Python 3.x
- OpenCV
- imutils
- dlib
- playsound

## Usage

1. Clone the repository:
    git clone https://github.com/your_username/drowsiness-detection.git

2. Install the required dependencies:
    pip install opencv-python imutils dlib playsound

3. Run the script:
  python final.py -p shape_predictor_68_face_landmarks.dat -a alarm.wav
  
The script takes two optional arguments:
- `-p` or `--shape-predictor`: Path to the facial landmark predictor file.
- `-a` or `--alarm`: Path to the alarm sound file (in WAV format).

You can also specify the webcam index using the `-w` or `--webcam` argument. By default, it uses the default webcam.

## Implementation Details

The script performs the following steps:

1. Loads the facial landmark predictor and initializes constants for eye aspect ratio (EAR) threshold and consecutive frames.
2. Starts the video stream from the webcam.
3. Detects faces in each frame using dlib's face detector.
4. Computes the eye aspect ratio (EAR) for each eye based on the detected facial landmarks.
5. Checks if the EAR is below the blink threshold for a specified number of consecutive frames.
6. If the eyes are closed for a sufficient number of frames, an alarm is triggered.
7. The alarm sound is played and an alert message is displayed on the frame.
8. The process continues until the user presses the 'q' key to quit the program.

Feel free to customize the script by modifying the threshold values or using a different alarm sound.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


