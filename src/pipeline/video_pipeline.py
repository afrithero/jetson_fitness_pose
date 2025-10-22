import cv2
from ultralytics import YOLO
from core.visualizer import draw_info

class VideoPipeline:
    def __init__(self, model_path, evaluator, source=0, output_path=None):
        self.model = YOLO(model_path)
        self.evaluator = evaluator
        self.source = source
        self.output_path = output_path
    
    def run(self):
        cap = cv2.VideoCapture(self.source)
        
        if not cap.isOpened():
            print(f"Cannot open source: {self.source}")
            return 

        # create video writer
        writer = None
        
        if self.output_path:
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            fps = cap.get(cv2.CAP_PROP_FPS) or 20
            w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            writer = cv2.VideoWriter(self.output_path, fourcc, fps, (w, h))
        
        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                break
            
            results = self.model(frame)

            if results and results[0].keypoints is not None:
                keypoints = results[0].keypoints.xy[0].cpu().numpy()
                self.evaluator.update(keypoints)
                info = self.evaluator.get_info()
                frame = draw_info(frame, info)
            
            if writer:
                writer.write(frame)

        cap.release()
        
        if writer:
            writer.release()
        
        print(f"Video has been saved to {self.output_path}")
