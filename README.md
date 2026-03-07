# open-canvas

A hobby project exploring **gesture-based interaction** using computer vision. It uses a webcam feed and hand tracking to let you draw freehand lines on screen by pinching your fingers — no mouse or touchscreen needed.

A second module (`mouse.py`) is in progress and will eventually replace canvas drawing with full mouse cursor control via hand gestures.

---

## What It Does

- Detects your hand in real time via webcam (or an IP camera stream)
- Tracks 21 hand landmarks using **MediaPipe**
- Measures the distance between your **index fingertip and thumb tip**
- When the pinch distance is ≤ 30px → starts drawing a freehand line on the canvas
- When you open your hand → stops drawing
- The canvas is overlaid live on the camera feed in a resizable window

---

## Project Structure

```
open-canvas/
├── main.py           # Main app — hand tracking + freehand drawing
├── mouse.py          # WIP — future mouse cursor control via gestures
└── requirements.txt  # Python dependencies
```

---

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your camera source

In `main.py`, the video source is set to an IP camera by default:

```python
cap = cv2.VideoCapture("http://192.168.29.71:4747/video")
```

To use your laptop's built-in webcam instead, change this to:

```python
cap = cv2.VideoCapture(0)
```

If using an IP camera, you can use an app like **DroidCam** and replace the URL with your device's stream address.

### 3. Run the app

```bash
python main.py
```

A window titled **"Image"** will open showing the live camera feed with hand landmarks drawn. Pinch your index finger and thumb together to draw on screen. Press **`q`** to quit.

---

## How the Drawing Works

| Gesture | Action |
|---|---|
| Thumb + index finger pinched (distance ≤ 30px) | Draw line at index fingertip position |
| Fingers separated | Stop drawing |

---

## Planned Features (`mouse.py`)

The `mouse.py` file is a scratchpad for the next phase: controlling the **mouse cursor** with hand movements using `pyautogui`. Once integrated into `main.py`, you'll be able to:

- Move the cursor by pointing your index finger
- Click by pinching

---

## Dependencies

Key libraries used:

- **MediaPipe** — hand landmark detection
- **OpenCV** — video capture and rendering
- **NumPy** — canvas manipulation
- **PyAutoGUI** *(mouse.py, upcoming)* — OS-level mouse control

Install everything with:

```bash
pip install -r requirements.txt
```
