import time 

start = time.perf_counter()

def do_something():
  time.sleep(1)

do_something()

finish = time.perf_counter()

print(f'The program runs {finish-start} s.')
