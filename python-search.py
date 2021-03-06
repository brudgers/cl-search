"""This file was autogenerated using org-babel-tangle
on the literate programming document located in the
root directory of the git repository."""

def tree_search(states, goal_p, successors, combiner):
    """Find a state that satisfies goal_p. Start with states and search according to successors and combiner."""
    if not states:
        return fail
    elif goal_p(states[0]):
        return states[0]
    else:
        tree_search(combiner(successors(first states), rest(states)), goal_p, successors, combiner)
