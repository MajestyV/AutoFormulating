from AutoFormulating import Ink
import numpy as np

#a = np.array([[0.95,-0.05,-0.05],[-0.1,0.9,-0.1],[-0.73,-0.73,0.27]])
#b = np.array([4.75,9.45,68.895])
#x = np.linalg.solve(a,b)

#print(x)

ink = Ink.formula([[20,0.945]])
print('5 wt% for 20 mL: '+str(ink.GetSoluteMass([5],'mg')[0])+' mg')
print('8 wt% for 20 mL: '+str(ink.GetSoluteMass([8],'mg')[0])+' mg')