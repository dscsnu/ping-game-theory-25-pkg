# Types

## `Move` (Enum)

```python
class Move(StrEnum):
    COOPERATE = "COOPERATE"
    DEFECT = "DEFECT"
```

Represents a single move in the Iterated Prisoner's Dilemma game.

## `HistoryEntry` (Dataclass)

```py
@dataclass
class HistoryEntry:
    self: Move
    other: Move
```

Represents the result of one round of play between two strategies.

| Field   | Type   | Meaning                            |
| ------- | ------ | ---------------------------------- |
| `self`  | `Move` | The move played by _this_ strategy |
| `other` | `Move` | The move played by the opponent    |

## `History` (Type Alias)

```py
History = Tuple[HistoryEntry, ...]
```

A read-only sequence of all previous rounds. Each element is a `HistoryEntry`. The most recent round is at the **end** of the tuple.

## `Strategy` (Abstract Base Class)

```py
class Strategy(ABC):
    @abstractmethod
    def begin(self) -> Move:
        ...
    @abstractmethod
    def turn(self, history: History) -> Move:
        ...
```

Base class for all strategies (bots).

Every strategy must implement two methods:

| Method          | Called When                 | Purpose                                         |
| --------------- | --------------------------- | ----------------------------------------------- |
| `begin()`       | Before the first round      | Returns the first move                          |
| `turn(history)` | Every round after the first | Returns the next move based on previous history |

Any class that does **not** implement both methods cannot be instantiated.

# Game Rules: Prisoner's Dilemma

The Iterated Prisoner's Dilemma is played over multiple rounds. Each round, both players simultaneously choose to either **cooperate** or **defect**. Points are awarded based on the payoff matrix:

| Your Move | Opponent's Move | Your Score | Opponent's Score |
| --------- | --------------- | ---------- | ---------------- |
| COOPERATE | COOPERATE       | 3          | 3                |
| COOPERATE | DEFECT          | 0          | 5                |
| DEFECT    | COOPERATE       | 5          | 0                |
| DEFECT    | DEFECT          | 1          | 1                |

**Key insight:** Defecting always gives you more points than cooperating in any single round, but mutual cooperation gives both players better scores than mutual defection over time.

# Example Strategies

## Always Cooperate

```py
class AlwaysCooperate(Strategy):
    def __init__(self) -> None:
        self.author_netid = ""
        self.strategy_name = ""
        self.strategy_desc = ""

    def begin(self) -> Move:
        return Move.COOPERATE

    def turn(self, history: History) -> Move:
        return Move.COOPERATE
```

## Tit for Tat

```py
class TitForTat(Strategy):
    def __init__(self) -> None:
        self.author_netid = ""
        self.strategy_name = ""
        self.strategy_desc = ""

    def begin(self) -> Move:
        return Move.COOPERATE

    def turn(self, history: History) -> Move:
        # Copy what the opponent did last round
        return history[-1].other
```

# Strategy Tester

To ensure every strategy follows the required interface and runs efficiently, the project includes a built-in tester: `StrategyTester`

The tester automatically checks:

| Check              | What it verifies                                         |
| ------------------ | -------------------------------------------------------- |
| **Initialization** | Your strategy's `__init__` runs without errors           |
| **Return types**   | `begin()` and `turn()` must always return a valid `Move` |
| **No exceptions**  | Your strategy must never crash during play               |
| **Performance**    | Must complete `10,000` rounds within `60 seconds`        |

If your strategy passes all checks, you will see:

```
✅ PASS: 10000 rounds in X.XX seconds
Strategy Total Score: XXXX (avg: X.XX)
Opponent Total Score: XXXX (avg: X.XX)
```

## How to Test Your Strategy

You must pass in your strategy class **without** instantiating it:

```py
if __name__ == "__main__":
    tester = StrategyTester(TitForTat)
    tester.run()
```
