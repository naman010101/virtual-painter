# Virtual Painter with Hand Tracking

A real-time virtual painting application that uses hand tracking powered by MediaPipe. Paint on your canvas using hand gestures!

## Features
- 🎨 Real-time hand tracking with MediaPipe
- ✏️ Virtual drawing/painting on webcam feed
- 👆 Finger-based brush control
- 🎯 Adaptive hand detection and tracking
- 🖼️ Header overlays for UI

## Requirements
- Python 3.7+
- OpenCV (cv2)
- MediaPipe
- NumPy

## Installation
```bash
pip install opencv-python mediapipe numpy
```

## Usage
```bash
python VirtualPainter.py
```

## Files
- **VirtualPainter.py** - Main application
- **handtrackingmodule.py** - Hand detection and tracking module using MediaPipe
- **Header - virtual painter/** - UI overlay images

## How It Works
The application uses MediaPipe's Hand Landmarker to detect hand landmarks in real-time:
1. Captures video from webcam
2. Detects hand positions and landmarks
3. Tracks finger movements for drawing
4. Renders virtual brush strokes on canvas

## Controls
- Use your hand to draw on the canvas
- Point your index and middle fingers to draw
- Use specific gestures to select colors and eraser

## License
MIT

## Author
[Your Name]
