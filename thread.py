import threading
import time

def function1():
  for i in range(5):
    print("Function 1:", i)
    time.sleep(1)  # Simulate some work

def function2():
  for i in range(5):
    print("Function 2:", i)
    time.sleep(2)  # Simulate some work

def function3():
  for i in range(5):
    print("Function 3:", i)
    time.sleep(3)  # Simulate some work

# Create and start threads
thread1 = threading.Thread(target=function1)
thread2 = threading.Thread(target=function2)
thread3 = threading.Thread(target=function3)

thread1.start()
thread2.start()
thread3.start()

# Wait for threads to finish (optional)
thread1.join()
thread2.join()
thread3.join()

print("All functions completed!")
