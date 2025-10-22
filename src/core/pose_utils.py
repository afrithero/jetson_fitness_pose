import numpy as np
from typing import Tuple

Point = Tuple[float, float] # (x, y)

def calculate_angle(a: Point, b: Point, c: Point) -> float:
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
    
    return angle

def is_body_straight(shoulder: Point, hip: Point, ankle: Point, tol: float = 15) -> bool:
    angle = calculate_angle(shoulder, hip, ankle)
    return abs(angle - 180) < tol
