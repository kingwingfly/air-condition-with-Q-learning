from agent import Agent
from config import ALPHA, GAMMA, EPSILON

def main():
    Agent(alpha=ALPHA, gamma=GAMMA, epsilon=EPSILON).run()

if __name__ == "__main__":
    main()
