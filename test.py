from ping_game_theory_25 import Strategy, StrategyTester, Move, History


class ILoveRocks(Strategy):
    def __init__(self) -> None:
        pass

    def begin(self) -> Move:
        return Move.ROCK

    def turn(self, history: History) -> Move:
        return self.begin()


if __name__ == "__main__":
    tester = StrategyTester(ILoveRocks)
    tester.run()
