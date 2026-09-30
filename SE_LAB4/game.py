import random
from logic import feedback


class Mastermind:
    def __init__(self):
        self.code = [str(random.randint(1, 6)) for _ in range(4)]
        self.history = []
        self.turns = 10
        self.won = False
        self.over = False

    def guess(self, raw):
        if self.over:
            return None
        exact, partial = feedback(self.code, list(raw))
        self.history.append((raw, exact, partial))
        self.turns -= 1
        if exact == 4:
            self.won = self.over = True
        elif self.turns == 0:
            self.over = True
        return exact, partial

    def run(self):
        print("Mastermind — enter four digits from 1 to 6.")
        while not self.over:
            raw = input(f"{self.turns} turns left > ").strip()
            if raw.lower() == "q":
                print("You quit. The code was", "".join(self.code))
                return
            if len(raw) != 4 or any(ch not in "123456" for ch in raw):
                print("Enter exactly four digits from 1 to 6.")
                continue
            exact, partial = self.guess(raw)
            print("Exact:", exact, " Partial:", partial)
        if self.won:
            print("Cracked the code!")
        else:
            print("Out of turns. The code was", "".join(self.code))