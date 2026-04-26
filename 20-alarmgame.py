
import pygame
import datetime
import time

print(pygame.mixer.init)
def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    is_running = True

    while is_running:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(now)

        if now == alarm_time:
            print("wake up")

            pygame.mixer.init();
            pygame.mixer.music.load('./status/music.mp3')
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            print("music stop")
            is_running = False


        time.sleep(1)
    


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time: ")
    set_alarm(alarm_time)