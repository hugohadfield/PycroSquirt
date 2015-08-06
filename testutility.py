
from MicroSquirt import MicroSquirt
import time


ms = MicroSquirt('COM7')
for i in range(0,100):
	ms.get_data()
	time.sleep(0.5)
