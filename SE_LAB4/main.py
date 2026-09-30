from game import Mastermind, DIFFICULTIES

if __name__ == "__main__":
    choice = ""
    while choice not in DIFFICULTIES:
        choice = input(f"Difficulty ({'/'.join(DIFFICULTIES)}) > ").strip().lower()
    Mastermind(choice).run()