"""
    current_time to unix_time converter
"""
import time

current_time = time.time()
unix_time = int(current_time)
print("Текущее время в формате Unix: ", unix_time)
