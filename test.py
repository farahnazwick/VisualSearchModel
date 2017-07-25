import numpy as np
# import math
# import cPickle
# import json
from scipy import stats

x= np.arange(10)
y= np.asarray([.4,.23,.7,.3,0,-.9,-.4,.3,.6,0])

tmp = x[1]
x[1] = x[2]
x[2] = tmp

ans = np.argsort(y)
print 'sorted array: ',ans