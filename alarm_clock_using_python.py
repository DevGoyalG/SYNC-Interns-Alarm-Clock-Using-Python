import time
import winsound

def set_alarm():
    print("Enter the time for the alarm (format: HH:MM):")
    while True:
        alarm_time = input("> ")
        try:
            alarm_hours, alarm_minutes = map(int, alarm_time.split(":"))
            if 0 <= alarm_hours < 24 and 0 <= alarm_minutes < 60:
                return alarm_hours, alarm_minutes
            else:
                print("Invalid time. Please enter a valid time in the format HH:MM.")
        except ValueError:
            print("Invalid time format. Please enter the time in the format HH:MM.")

def play_alarm_sound():
    frequency = 2500    #hz
    duration = 1000     #ms
    for _ in range(5):  
        winsound.Beep(frequency, duration)

def main():
    print("Welcome to the Alarm Clock!")
    alarm_hours, alarm_minutes = set_alarm()

    while True:
        current_time = time.localtime()
        current_hours, current_minutes = current_time.tm_hour, current_time.tm_min

        if current_hours == alarm_hours and current_minutes == alarm_minutes:
            print("Time's up! Alarm is going off.")
            play_alarm_sound()
            break

        time.sleep(60)

if __name__ == "__main__":
    main()

