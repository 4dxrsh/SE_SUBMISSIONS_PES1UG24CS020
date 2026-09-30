from collections import Counter


def feedback(code, guess):
    exact = sum(a == b for a, b in zip(code, guess))
    common = sum((Counter(code) & Counter(guess)).values())
    return exact, common - exact