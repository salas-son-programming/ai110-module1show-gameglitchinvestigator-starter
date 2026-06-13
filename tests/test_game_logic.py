import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from logic_utils import check_guess


def test_high_guess():
    outcome, message = check_guess(60, 50)

    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"


def test_low_guess():
    outcome, message = check_guess(40, 50)

    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_correct_guess():
    outcome, message = check_guess(50, 50)

    assert outcome == "Win"