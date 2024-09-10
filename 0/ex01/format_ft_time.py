import time


time_s = time.time()

print(f"Seconds since January 1, 1970: {time_s:,} or {time_s:.2e} in scientific notation")
print(time.strftime("%b %d %Y") )