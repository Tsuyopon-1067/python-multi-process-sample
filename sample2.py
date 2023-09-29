import time
from multiprocessing import Pool
import os
from typing import List

def nijou(ary: List[int]):
	res: List[int] = []
	for x in ary:
		res.append(x*x)
	time.sleep(1)
	return(res)

def ary_split(ary: List[int], n: int):
	res: [List[List[int]]] = []
	ary_len: int = len(ary)

	split_len = int(ary_len/n)
	count: int = ary_len - split_len*n
	idx_lst: List[int] = []
	idx_lst.append(0)
	idx_pointer: int = 0

	for i in range(n):
		idx_pointer += split_len
		if count > 0:
			idx_pointer += 1
			count -= 1
		idx_lst.append(idx_pointer)

	for i in range(n):
		tmp: List[int] = ary[idx_lst[i]:idx_lst[i+1]]
		res.append(tmp)
	return res

def main():
	ary = list(range(100))
	n:int = os.cpu_count()
	print(n)

	p = Pool(n)
	ary2 = ary_split(ary, n)
	print(ary2)

	result = p.map(nijou, ary2)
	print(result)

if __name__ == "__main__":
	main()

