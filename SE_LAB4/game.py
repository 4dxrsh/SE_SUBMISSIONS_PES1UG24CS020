import random
from logic import feedback

DIFFICULTIES = {
    "easy": (3, 4, 8),
    "medium": (4, 6, 10),
    "hard": (5, 8, 12),
}  # (code length, symbol range, allowed guesses)


class Mastermind:
    def __init__(self, difficulty="medium"):
        self.length, self.symbols, self.turns = DIFFICULTIES[difficulty]
        self.alphabet = "".join(str(i) for i in range(1, self.symbols + 1))
        self.code = [random.choice(self.alphabet) for _ in range(self.length)]
        self.history = []
        self.won = False
        self.over = False

    def valid(self, raw):
        return len(raw) == self.length and all(ch in self.alphabet for ch in raw)

    def guess(self, raw):
        if self.over or not self.valid(raw):
            return None
        exact, partial = feedback(self.code, list(raw))
        self.history.append((raw, exact, partial))
        self.turns -= 1
        if exact == self.length:
            self.won = self.over = True
        elif self.turns == 0:
            self.over = True
        return exact, partial

    def run(self):
        print(f"Mastermind: enter {self.length} digits from 1 to {self.symbols}. 'q' quits.")
        while not self.over:
            raw = input(f"{self.turns} turns left > ").strip()
            if raw.lower() == "q":
                print("You quit. The code was", "".join(self.code))
                return
            result = self.guess(raw)
            if result is None:
                print(f"Enter exactly {self.length} digits from 1 to {self.symbols}.")
                continue
            print("Exact:", result[0], " Partial:", result[1])
        if self.won:
            print("Cracked the code!")
        else:
            print("Out of turns. The code was", "".join(self.code))