# Real-Time Fitness Pose Estimation on Jetson
This repository showcases real-time fitness pose estimation running entirely on the NVIDIA Jetson Orin Nano, leveraging YOLO pose models accelerated with TensorRT. Designed as an edge AI application, the system can analyze human body keypoints directly on-device, evaluate exercise quality, and provide immediate feedback. The combination of YOLO’s efficient pose detection and TensorRT’s optimized inference enables smooth, low-latency performance suitable for real-world fitness monitoring and interactive training scenarios.

![Demo](demo.gif)

## Feature
- **Exercise Support**:
  Currently supports push-up pose evaluation (counting reps and scoring form).
  Future updates will expand to include pull-ups, squats, sit-ups, and more common fitness movements.

- **Input Sources:**
  - Video file (.mp4 and other formats)
  - Webcam (USB camera connected to Jetson Orin Nano)
  - RTSP streams for remote or network-based camera feeds

## Environment Setup

### Build Image
```bash
docker build -t my-fitness-pose .
```

### Run Container
```bash
docker run -it \
  --runtime=nvidia \
  --network host \
  --device [your webcam device path] \
  my-fitness-pose
```

## How to use?
### Video Inference
```bash
cd ./src
python main.py \
  --model [your checkpoint path] \ # .pt or .engine
  --source [your video path] \
  --output [the video output path]
```

### Webcam
```bash
cd ./src
python main.py \
  --model [your checkpoint path] \ # .pt or .engine
  --source [your webcam device ID] # e.g., 0
```

### RTSP
```bash
cd ./src
python main.py \
  --model [your checkpoint path] \ # .pt or .engine
  --source rtsp://{IP}:{Port}/{stream}
```
