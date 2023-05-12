import numpy as np
import h5py
filename = ""
print(np.loadtxt("h5test.txt", h5py.File('/home/wojciech/Dokumenty/studia/dvs/e2calib/python/test1.h5')['t'])[0])