import pandas as pd
import numpy as np

class InvalidScoreError(Exception):
    def __init__(self, name, scores):
        message = f"Invalid score, Score must be Above 0 and Below 100 only. Score is {scores}"
        super().__init__(message)
        self.name = name
        self.scores = scores

def CheckScore(scores):
    if scores <0 and >=101:
        raise InvalidScoreError(scores)
    

class StudentRecordLockedError(Exception):
    pass

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
    
    def __str__(self):
        return f"{self.name} Has a score of: {self.scores}."

    def __repr__(self):
        return f"Student({self.name} Has a score of: {self.scores}.)"

raw_rows = [
    {"name": " Amara ", "scores": "92,85,78"},
    {"name": "Leo", "scores": "88,91,73"},
    {"name": "Priya", "scores": "65,72,150"},         
    {"name": "Sam", "scores": "70,not_a_number,60"},  
    {"name": "Amara", "scores": "95,90,88"},          
    {"name": "Jade", "scores": "81,77,84,90"},
]

