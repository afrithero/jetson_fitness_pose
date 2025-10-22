from abc import ABC, abstractmethod
import numpy as np

class EvaluatorBase(ABC):

    def __init__(self):
        self.count = 0
        self.stage = 0

    @abstractmethod
    def update(self, keypoints):
        # keypoints shape: [17, 2]
        pass

    @abstractmethod
    def get_score(self):
        pass
    
    @abstractmethod
    def get_count(self):
        pass
    
    @abstractmethod
    def get_info(self):
        pass
