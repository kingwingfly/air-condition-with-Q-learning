from type import QTable
from config import ACTIONS, STATES
import pickle
import os

class Data:
    def __init__(self) -> None:
        self.q: QTable = {
            state: {action: 0.0 for action in ACTIONS}
            for state in STATES
        }
        self.t: list[list[float]] = [] # time cost
        self.tp: list[list[float]] = [] # initial temperature
        self.u: list[list[float]] = [] # AHU valve openings
        self.cdi: list[float] = [] # cdi = (max{t} - min{t}) / max{t}

    def save(self, path: str):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    def load(self, path: str):
        if not os.path.exists(path):
            return
        with open(path, 'rb') as f:
            data = pickle.load(f)
            self.q = data.q
            self.t = data.t
            self.tp = data.tp
            self.u = data.u
            self.cdi = data.cdi
