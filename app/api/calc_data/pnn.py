
import numpy as np
from scipy.signal import find_peaks

#*******************************************************
#               Find RRI          
#*******************************************************
def find_RRI(time, data):       
    peaks, _ = find_peaks(data, distance=50, prominence=0.2)#, threshold=0.2)
    print ("In pnn.py peaks = ", peaks)
    peak_time = np.array(time)[peaks] * 0.001
    print ("In pnn.py peak_time = ", peak_time)
    RRI = np.diff(peak_time, n = 1)
    return peak_time, RRI, peaks
    
#*******************************************************
#               Calculation of PNN
#*******************************************************
def cal_pnn(peak_time, RRI):
    peak_time, RRI = peak_time, RRI        
    diffRRI = np.abs(np.diff(RRI, n=1))
    print ("In pnn.py diffRRI = ", diffRRI)
    number = len(diffRRI)
    print ("In pnn.py number = ", number)
    pnn50 = []
    pnn_time = []
    
    pnn50 = len(np.where(diffRRI > 0.05)[0])/number
    pnn_time = peak_time[-1]

    print ("In pnn.py pnn50 =", pnn50)
    return pnn_time, pnn50

