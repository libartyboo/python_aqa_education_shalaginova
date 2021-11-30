import datetime
import time

dt = datetime.datetime(1991, 6, 12, 6, 9)
print(dt)
print(datetime.datetime.now())
print(datetime.datetime.today())
print(dt.time())
print(dt.date())


current_time = time.gmtime()
action = "to feed the cat"
print(f"It's {current_time}. Time {action}.")
current_time = time.asctime(time.gmtime())
print(f"It's {current_time}. Time {action}.")


action2 = "to feed the dog"
time.sleep(3)
current_time = time.strftime("%H:%M", time.localtime())
print(f"It's {current_time}. Time {action2}.")


print(time.asctime())
print(time.ctime(time.time()))
print(time.gmtime(0))

last_time = time.time()
action = 'to feed the cat'
current_time = time.strftime("%H:%M", time.localtime())
print(f"It's {current_time}. Time {action}.")
time.sleep(1)


new_cur_time = time.time()
print(new_cur_time)
time_passed = int((new_cur_time - last_time) / 60)
print(f"You have fed the cat {time_passed} minutes ago.")

start = time.perf_counter()
print("Oh no! The cat's breaking his diet!")
end = time.perf_counter()
total_time = end - start
print(f"Your program has executed for {total_time} seconds.")

print(time.timezone / 3600)
print(time.tzname)
print(time.daylight)
