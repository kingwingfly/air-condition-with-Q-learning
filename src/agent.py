from threading import Thread
from data import Data
from config import ACTIONS, STATES, TESTING, PATH
from utils import get_inputs, print_if_testing
import numpy as np
from type import Action


class Agent(Thread):
    def __init__(self, alpha: float, gamma: float, epsilon: float):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.data = Data()
        self.data.load(PATH)

    def run(self):
        self.main_loop()

    def main_loop(self):
        print("Agent is running...")
        print_if_testing(self.data.q)
        while True:
            action = self.recommend_action()
            print(f"Recommended action: {action}")
            self.execute_action(action)
            self.collect_data()
            self.update_q_table(action)
            print_if_testing(self.data.q)
            if not TESTING:
                self.data.save(PATH)

    def recommend_action(self) -> Action:
        m = len(ACTIONS)
        if len(self.data.cdi) == 0:
            print("No data available. Randomly selecting an action.")
            idx: int = np.random.choice(m)
            return ACTIONS[idx]
        for state in STATES:
            if not (
                state[0] <= self.data.cdi[-1] < state[1]
                or self.data.cdi[-1] == state[1] == 1.0
            ):
                continue
            distribution = [self.epsilon / m] * m
            idx = max(range(m), key=lambda i: self.data.q[state][ACTIONS[i]])
            distribution[idx] += 1 - self.epsilon
            idx = np.random.choice(m, p=distribution)
            return ACTIONS[idx]
        raise RuntimeError(
            "No action recommended. cdi out of range. make sure data and STATES are correct."
        )

    def execute_action(self, action: Action): ...

    def collect_data(self):
        if TESTING:
            t = [float(i) for i in range(0, 5)]
            tp = [float(i) for i in range(0, 5)]
            u = [float(i) for i in range(0, 5)]
            input("Using testing data, Press any key to continue...")
        else:
            t = get_inputs("Enter the time cost: ", float)
            tp = get_inputs("Enter the initial temperature: ", float)
            u = get_inputs("Enter the AHU valve openings: ", float)
            assert (
                len(t) == len(tp) == len(u)
            ), "Lengths of time cost, initial temperature, and AHU valve openings must be the same."
        cdi = 1 - min(t) / max(t)
        self.data.t.append(t)
        self.data.tp.append(tp)
        self.data.u.append(u)
        self.data.cdi.append(cdi)

    def update_q_table(self, action: Action):
        if len(self.data.cdi) < 2:
            print("Not enough data to update Q table.")
            return
        for old_s in STATES:
            if not (
                old_s[0] <= self.data.cdi[-2] < old_s[1]
                or self.data.cdi[-2] == old_s[1] == 1.0
            ):
                continue
            for new_s in STATES:
                if not (
                    new_s[0] <= self.data.cdi[-1] < new_s[1]
                    or self.data.cdi[-1] == new_s[1] == 1.0
                ):
                    continue
                r = -max(self.data.t[-1])  # reward
                self.data.q[old_s][action] *= 1 - self.alpha
                self.data.q[old_s][action] += self.alpha * (
                    r + self.gamma * max(self.data.q[new_s].values())
                )
                return
        raise RuntimeError(
            "Failed to update Q table. cdi out of range. make sure data and STATES are correct."
        )
