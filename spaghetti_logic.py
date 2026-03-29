from pathlib import Path
from typing import Iterable, List


def calculate_total(value: float, rate: float = 0.15) -> float:
    """Apply a mark-up rate to a numeric value."""
    if value < 0:
        raise ValueError("Value must be non-negative")
    return value * (1 + rate)


def format_total(value: float) -> str:
    """Create a user-friendly formatted output string."""
    return f"Total: {value:.2f}"


def append_list_to_log(values: Iterable[float], log_path: Path | str = "log.txt") -> None:
    """Append a list of values to a log file as a line of text."""
    path = Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(repr(list(values)) + "\n")


def process_data(data: Iterable[float], rate: float = 0.15, log_path: Path | str = "log.txt") -> List[float]:
    """Compute totals for input values, print formatted results, and persist to log.

    This function is intentionally a coordinator that uses small single-purpose helpers.
    """
    if not hasattr(data, "__iter__"):
        raise TypeError("data must be an iterable of numbers")

    results: List[float] = []

    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("All items in data must be int or float")

        total = calculate_total(float(item), rate=rate)
        results.append(total)
        print(format_total(total))

    append_list_to_log(results, log_path=log_path)

    return results


if __name__ == "__main__":
    sample = [100, 23.5, 0]
    process_data(sample)

