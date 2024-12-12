# k and b
Action = tuple[float, float]
# the cdi range
State = tuple[float, float]

QTable = dict[State, dict[Action, float]]
