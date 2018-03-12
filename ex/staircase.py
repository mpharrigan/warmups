import numpy as np


def move(loc, i):
    next = loc.copy()
    next[i] += 1
    return next


def staircase_sum(M: np.ndarray):
    stack = []
    location = np.ones(M.ndim)
    running_mult = 1.0
    running_sum = 0.0
    end = np.asarray(M.shape)
    direction = 0

    while True:
        if np.any(location > end):
            # This path has failed. Go back and try the next direction
            try:
                location, running_mult, direction = stack.pop()
                direction += 1
            except IndexError:
                break

        if direction == 0:
            # If this is the first time we've visited this node on this path
            # multiply it in.
            running_mult *= M[tuple(int(k - 1) for k in location)]

        if np.array_equal(location, end):
            # If we've reached the end, add this path to our total and go back
            # to explore other paths
            running_sum += running_mult
            try:
                location, running_mult, direction = stack.pop()
                direction += 1
            except IndexError:
                break

        # If there are more directions to explore, explore them
        # first make a note of where we are
        if direction < M.ndim:
            stack.append((location, running_mult, direction))
            location = move(location, direction)
            direction = 0
        else:
            # Otherwise work through our backlog
            try:
                location, running_mult, direction = stack.pop()
                direction += 1
            except IndexError:
                break

    return running_sum


def test_paths():
    test_m = np.array([
        [1, 2],
        [3, 4],
    ])
    res = staircase_sum(test_m)
    assert res == (1 * 3 * 4 + 1 * 2 * 4)


if __name__ == '__main__':
    test_paths()
