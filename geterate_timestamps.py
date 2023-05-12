import datetime
import os
from ssl import OP_NO_COMPRESSION
import numpy as np

def write_timestamps(timestamps_file, interval):
    counter = 0
    current_timestamp = interval
    timestamps=[]
    while counter < 25:
        timestamps.append(current_timestamp)
        current_timestamp += interval
        counter += 1
    np.savetxt('timestamps.txt', np.array(timestamps), '%i') 

if __name__ == "__main__":
    interval = (1/30)*1e6
    write_timestamps("timestamps.txt", interval)
    timestamps = np.loadtxt(str("timestamps.txt"), dtype=np.int64)
    print(timestamps)
