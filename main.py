import random

SECONDS_PER_SECOND = 1
SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

SECONDS_PER_HOUR = SECONDS_PER_MINUTE * MINUTES_PER_HOUR
SECONDS_PER_DAY = SECONDS_PER_HOUR * HOURS_PER_DAY


def clock(seconds_since_midnight: int) -> tuple[int, int, int]:
    """Func returns clock indication"""

    days = seconds_since_midnight // SECONDS_PER_DAY
    seconds_since_midnight %= SECONDS_PER_DAY

    hours = seconds_since_midnight // SECONDS_PER_HOUR
    seconds_since_midnight %= SECONDS_PER_HOUR

    minutes = seconds_since_midnight // SECONDS_PER_MINUTE
    seconds_since_midnight %= SECONDS_PER_MINUTE

    seconds = seconds_since_midnight // SECONDS_PER_SECOND
    seconds_since_midnight %= SECONDS_PER_SECOND

    return hours, minutes, seconds


def main():

    n = int(input())

    hours, minutes, seconds = clock(n)

    print(f"{hours}:{minutes:02}:{seconds:02}")


main()
