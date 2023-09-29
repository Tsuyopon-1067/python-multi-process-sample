import time
from multiprocessing import Pool
import os

def nijou(x):
	print('input: %d' % x)
	time.sleep(1)
	retValue = x * x
	print('double: %d' % (retValue))
	return(retValue)


def main():
	n:int = os.cpu_count()
	p = Pool(n)
	result = p.map(nijou, range(10))
	print(result)

if __name__ == "__main__":
    main()
