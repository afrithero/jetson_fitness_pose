from .evaluator_base import EvaluatorBase
from core.pose_utils import calculate_angle, is_body_straight

class PushupEvaluator(EvaluatorBase):
    def __init__(self):
        super().__init__()
        self.stage = None 
        self.shoulder = None
        self.elbow = None
        self.wrist = None
        self.hip = None
        self.ankle = None
        self.elbow_angle = None
        self.straight = None
        self.rep_scores = []

    def update(self, keypoints):
        # https://mmpose.readthedocs.io/en/latest/dataset_zoo/2d_body_keypoint.html
        self.shoulder = keypoints[5]
        self.elbow = keypoints[7]
        self.wrist = keypoints[9]
        self.hip = keypoints[11]
        self.ankle = keypoints[15]

        self.elbow_angle = calculate_angle(self.shoulder, self.elbow, self.wrist)
        self.straight = is_body_straight(self.shoulder, self.hip, self.ankle)

        if self.elbow_angle < 70:
            self.stage = "down"
        elif self.elbow_angle > 130 and self.stage == "down":
            self.stage = "up"
            self.count += 1
            rep_score = 50
            
            if self.straight:
                rep_score += 50
            
            self.rep_scores.append(rep_score)
    
    def get_score(self):
        if not self.rep_scores:
            return 0
        return sum(self.rep_scores) / len(self.rep_scores)

    def get_count(self):
        return self.count
    
    def get_info(self):
        info = {
            "texts": [
                (f"Push-up Count: {self.count}", (50, 50)),
                (f"Score: {self.get_score():.1f}", (50, 100))
            ],
            "lines": [
                # body line (left shoulder → elbow → wrist)
                ((int(self.shoulder[0]), int(self.shoulder[1])),
                (int(self.elbow[0]), int(self.elbow[1]))),
                ((int(self.elbow[0]), int(self.elbow[1])),
                (int(self.wrist[0]), int(self.wrist[1])))
            ],
            "angles": [
                ((int(self.elbow[0]), int(self.elbow[1])), self.elbow_angle)
            ]            
        }

        return info
