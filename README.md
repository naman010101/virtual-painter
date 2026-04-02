# Virtual Painter with Hand Tracking 🎨

A cutting-edge real-time virtual painting application that transforms your hand into a digital brush. Using advanced computer vision and MediaPipe's hand tracking technology, users can paint and create artwork directly from their webcam feed with intuitive hand gestures—no physical tools required!

## 📋 Project Overview

**Virtual Painter** is a gesture-based drawing application that leverages real-time hand detection and finger tracking to enable users to paint on a digital canvas using only their hands. This project demonstrates the power of modern computer vision techniques combined with intuitive gesture recognition to create an interactive and engaging user experience.

Whether you're an artist looking to experiment with digital painting, a developer interested in computer vision projects, or someone curious about hand tracking technology, Virtual Painter provides a fun and educational platform to explore gesture-based interfaces.

## ✨ Key Features

- **🎯 Real-Time Hand Detection**: Leverages MediaPipe's state-of-the-art hand landmark detection for accurate and responsive tracking
- **✏️ Intuitive Gesture-Based Drawing**: Paint on the canvas using natural hand movements without any device attachments
- **🌈 Multi-Color Support**: Switch between different brush colors using simple hand gestures
- **🧹 Smart Eraser Function**: Clear mistakes with dedicated eraser gesture recognition
- **⚡ High Performance**: Optimized for real-time performance with minimal latency
- **🎬 Live Webcam Feed**: Direct visual feedback as you paint on your webcam stream
- **📊 Finger Tracking**: Precise detection of all five fingers with 21 hand landmarks per hand
- **🖥️ User-Friendly Interface**: Clean UI with on-screen controls and visual feedback
- **👐 Dual Hand Support**: Track and interact with both hands simultaneously

## 🛠️ Technical Stack

| Component | Technology |
|-----------|-----------|
| **Computer Vision Framework** | OpenCV (cv2) |
| **Hand Detection & Tracking** | MediaPipe Hand Landmarker |
| **Language** | Python 3.7+ |
| **Core Libraries** | NumPy for numerical operations |
| **Video Capture** | OpenCV Webcam Interface |

## 📦 Requirements

```
Python 3.7 or higher
OpenCV (cv2) - 4.5+
MediaPipe - Latest version
NumPy - 1.19+
```

## 🚀 Installation & Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/naman010101/virtual-painter.git
cd virtual-painter
```

### Step 2: Install Dependencies
```bash
pip install opencv-python mediapipe numpy
```

Or install all at once:
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python VirtualPainter.py
```

## 🎮 How to Use

1. **Start the Application**: Run `python VirtualPainter.py`
2. **Position Your Hand**: Face your webcam with your hand visible
3. **Draw**: Use your index and middle fingers to draw on the canvas
4. **Change Colors**: Use specific hand gestures to switch between colors
5. **Erase**: Make an erasing gesture to clear parts of your drawing
6. **Exit**: Press 'q' or close the window to exit

## 📁 File Structure

### Main Application
- **`VirtualPainter.py`** - Core application that handles rendering, drawing, and user interactions
  - Initializes webcam feed
  - Processes hand tracking data
  - Renders paint strokes on canvas
  - Manages color selection and eraser functionality
  - Displays UI overlays and controls

### Hand Tracking Module
- **`handtrackingmodule.py`** - Comprehensive hand detection and tracking module (Detailed below)
  - Wraps MediaPipe's hand landmark detection
  - Provides easy-to-use methods for hand detection
  - Calculates hand positions and finger coordinates
  - Enables gesture recognition through landmark analysis

### User Interface
- **`Header - virtual painter/`** - Contains UI overlay images and icons
  - Visual elements for the painting interface
  - Color palette graphics
  - Button overlays for interaction

## 🔍 Hand Tracking Module - Detailed Description

### Overview
The `handtrackingmodule.py` is a custom wrapper around MediaPipe's Hand Landmarker solution. It simplifies the process of hand detection and provides a high-level API for hand tracking operations in computer vision applications.

### Features & Capabilities

**Hand Landmark Detection**
- Detects up to 21 hand landmarks per hand
- Tracks both left and right hands simultaneously
- Provides 3D coordinates (x, y, z) for each landmark
- Calculates confidence scores for each detection

**Landmark Indices** (MediaPipe Standard):
```
0:  Wrist
1-4:    Thumb (base → tip)
5-8:    Index finger
9-12:   Middle finger
13-16:  Ring finger
17-20:  Pinky finger
```

**Key Functions**
- `detect_hands()` - Detects all hands in the current frame
- `get_hand_positions()` - Returns x, y coordinates of all landmarks
- `get_finger_positions()` - Returns specific finger tip positions
- `calculate_distance()` - Measures distance between two landmarks
- `is_finger_extended()` - Checks if a specific finger is extended

**Distance Calculation**
- Euclidean distance computation between landmarks
- Useful for gesture recognition
- Enables pinch detection, finger distance analysis, and more

**Gesture Recognition Support**
- Foundation for identifying hand gestures
- Pinch detection (thumb and index finger proximity)
- Finger up/down status detection
- Hand orientation analysis

### Integration with Virtual Painter
The hand tracking module provides raw hand data that Virtual Painter transforms into:
1. **Drawing Input**: Index and middle finger positions control brush location
2. **Color Selection**: Specific hand gestures trigger color changes
3. **Eraser Activation**: Dedicated gesture activates eraser mode
4. **Canvas Control**: Hand movements translate to brush strokes

## 🎯 How It Works - Technical Flow

```
Video Frame
    ↓
MediaPipe Hand Detection (handtrackingmodule.py)
    ↓
Extract Hand Landmarks (21 points per hand)
    ↓
Gesture Recognition & Finger Analysis
    ↓
Virtual Painter Application (VirtualPainter.py)
    ↓
Update Canvas & Render Paint Strokes
    ↓
Display Output with UI Overlays
```

### Step-by-Step Process

1. **Frame Capture**: Captures video frames from the webcam in real-time
2. **Hand Detection**: MediaPipe analyzes frames to identify hands and their landmarks
3. **Landmark Extraction**: Retrieves 21 hand landmarks for each detected hand
4. **Gesture Processing**: Analyzes landmark positions to determine current gestures
5. **Canvas Update**: Based on gestures, updates the virtual canvas with paint strokes
6. **Rendering**: Combines original video with painted canvas and UI elements
7. **Display**: Shows the final output to the user

## 🎨 Color Palette & Gestures

The application uses intuitive hand gestures to control various functions:

| Gesture | Action |
|---------|--------|
| Index + Middle fingers extended | Draw mode |
| Ring finger point | Eraser mode |
| Thumb + Index pinch | Color selection |
| All fingers extended | Reset/Clear canvas |
| Closed fist | Pause drawing |

## 🔧 Customization Options

You can easily customize the Virtual Painter:

- **Brush Size**: Modify brush thickness in VirtualPainter.py
- **Colors**: Add more colors to the palette
- **Detection Confidence**: Adjust MediaPipe confidence thresholds for stricter/looser detection
- **Canvas Size**: Change the drawing canvas dimensions
- **Gesture Sensitivity**: Fine-tune gesture recognition parameters

## 📊 Performance Considerations

- **Real-Time Processing**: Runs at ~30 FPS on most modern systems
- **Latency**: Minimal delay between hand movement and brush stroke
- **Memory Usage**: Optimized for regular laptops (200-500 MB typical)
- **CPU/GPU**: Works on CPU; can be accelerated with GPU support

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Hand not detected | Ensure good lighting and hand is clearly visible |
| Laggy performance | Close other applications; consider reducing resolution |
| Shaky brush strokes | Increase smoothing factor or distance threshold |
| Gestures not working | Adjust gesture sensitivity parameters |

## 🎓 Learning Outcomes

This project demonstrates:
- Real-time computer vision processing with OpenCV
- Machine learning inference using MediaPipe
- Hand pose estimation and gesture recognition
- Event-driven programming with video streams
- Real-time canvas rendering and graphics manipulation
- Integration of multiple computer vision libraries

## 🚀 Future Enhancements

- 3D hand gesture recognition
- ML model for advanced gesture commands
- Save/Export drawn artwork as images
- Undo/Redo functionality
- Touch-free zoom and pan controls
- Machine learning-based stroke prediction
- Hand pose classification for artistic effects
- Multi-user collaboration support

## 📝 License

MIT License - Feel free to use, modify, and distribute this project

## 👨‍💻 Author

**Naman Saluja**  
GitHub: [@naman010101](https://github.com/naman010101)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Suggest new features
- Submit pull requests with improvements
- Share your artwork created with Virtual Painter

## 📧 Contact & Support

If you have questions or need support, feel free to open an issue on GitHub.

---

**Give this project a ⭐ if you found it useful!**
