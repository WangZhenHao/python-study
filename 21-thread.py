# multi threading  = used to perform multiple task at the same time

import threading
import time

def walk_doy(fistname, lastname):
    time.sleep(5)
    print(f"Walking with doy name={fistname} {lastname}")

def take_out_trash():
    time.sleep(3)
    print("Take out trash")

def get_mail():
    time.sleep(2)
    print("Get mail")


# walk_doy()
# take_out_trash()
# get_mail()
chore1 = threading.Thread(target=walk_doy, args=("Doy", "Kim"))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

chore1.start()
chore2.start()
chore3.start()


chore1.join()
chore2.join()
chore3.join()
print("All done")