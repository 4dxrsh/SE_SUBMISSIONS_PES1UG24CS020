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

    def show_history(self):
        for i, (g, e, p) in enumerate(self.history, 1):
            print(f"  {i:>2}. {g}  exact={e} partial={p}")

    def run(self):
        print(f"Mastermind: enter {self.length} digits from 1 to {self.symbols}. 'q' quits.")
        while not self.over:
            raw = input(f"{self.turns} turns left > ").strip()
            if raw.lower() == "q":
                print("You quit. The code was", "".join(self.code))
                return
            if self.guess(raw) is None:
                print(f"Enter exactly {self.length} digits from 1 to {self.symbols}.")
                continue
            self.show_history()
        if self.won:
            print("Cracked the code!")
        else:
            print("Out of turns. The code was", "".join(self.code))