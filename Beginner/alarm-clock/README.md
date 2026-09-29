# Alarm Clock

A simple command-line alarm clock in Python.

## Features

- Set one alarm using 24-hour local time
- Checks invalid input and lets you try again
- Schedules times that have already passed for tomorrow
- Displays an alert and sends a terminal bell when the alarm is due
- Press Ctrl+C to cancel

## How to Run

1. Make sure you have Python 3 installed. No extra packages are needed.
2. From the project root, run:

   ```bash
   python Beginner/alarm-clock/alarm_clock.py
   ```

   Or, from this folder, run `python alarm_clock.py`.

## Example

```text
Welcome to Alarm Clock!
Keep this program running and your computer awake.
Press Ctrl+C to cancel.
Set alarm (HH:MM, 24-hour time): 18:45
Alarm set for 2026-09-29 18:45.
Time's up! Your alarm is ringing!
```

The date depends on when you run the program. An alarm starts at zero
seconds of the chosen minute, so entering the current minute schedules
it for tomorrow. To try it quickly, choose the next minute.

Keep the terminal open and the computer awake while waiting. The bell
may be silent depending on your terminal settings; the text alert still
appears. The program exits after the alert.

## What You Can Learn

- Use `input()` and `try`/`except` to validate user input
- Parse times with `datetime.strptime()`
- Use `timedelta` to move a date forward by one day
- Combine a `while` loop with `time.sleep()` to wait between checks
- Organize a program into small functions with docstrings

---

Project for learning purposes.
