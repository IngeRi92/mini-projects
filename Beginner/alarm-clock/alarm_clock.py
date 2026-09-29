"""A simple command-line alarm clock using the computer's local time."""

from datetime import datetime, timedelta
import time


def get_alarm_time():
    """Ask for an alarm time, retrying until the input is valid.

    Times that have already passed today are scheduled for tomorrow.

    Returns:
        datetime: The next occurrence of the entered time.
    """
    while True:
        user_input = input("Set alarm (HH:MM, 24-hour time): ").strip()
        try:
            alarm_time = datetime.strptime(user_input, "%H:%M")
        except ValueError:
            print("Please enter a valid time, such as 07:30 or 18:45.")
            continue

        now = datetime.now()
        alarm_time = now.replace(
            hour=alarm_time.hour, minute=alarm_time.minute,
            second=0, microsecond=0
        )
        if alarm_time <= now:
            alarm_time += timedelta(days=1)
        return alarm_time


def wait_for_alarm(alarm_time):
    """Wait until the alarm is due, then display an alert and terminal bell.

    Args:
        alarm_time (datetime): The local date and time for the alarm.

    Returns:
        None.
    """
    while datetime.now() < alarm_time:
        # Pause between checks so the loop does not keep the CPU busy.
        time.sleep(1)
    print("\aTime's up! Your alarm is ringing!", flush=True)


def main():
    """Set and run one alarm, allowing Ctrl+C to cancel.

    Returns:
        None.
    """
    print("Welcome to Alarm Clock!")
    print("Keep this program running and your computer awake.")
    print("Press Ctrl+C to cancel.")
    try:
        alarm_time = get_alarm_time()
        print(f"Alarm set for {alarm_time:%Y-%m-%d %H:%M}.")
        wait_for_alarm(alarm_time)
    except (KeyboardInterrupt, EOFError):
        print("\nAlarm cancelled.")


if __name__ == "__main__":
    main()
