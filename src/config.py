from type import Action, State

# set to True to use testing data
# set to False to use user inputs
TESTING = True

ALPHA, GAMMA, EPSILON = 0.9, 0.1, 0.3

# path to save/load data
PATH = 'data.pkl'

# list of actions and states
ACTIONS: list[Action] = [(0.5, 0.0125), (1.0, 0.025), (2.0, 0.05)]
STATES: list[State] = [(0.2 * i, 0.2 * (i + 1)) for i in range(5)]
