import time

# for x in range(3):
# for x in range(3, 0, -1):
my_timer = int(input("Enter a number: "));

for x in range(my_timer, 0, -1):
    secent = x % 60;
    minutes = int(x / 60) % 60;
    hours = int(x / 3600);
    print(f"{hours:02}:{minutes:02}:{secent:02d}")
    time.sleep(1)

print('Done!')