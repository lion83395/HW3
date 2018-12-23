

from math import fabs
from time import time
 
data = open('graph_6.txt')
N =  2000
tax_rate = 0.15
eps = 1e-6
r = [1./N for i in range(N)]
r2 = [1./N for i in range(N)]
out_degree = [0 for i in range(N)]
m = [[] for i in range(N*2)]
hash_table = [-1 for i in range(N*2)]
idx = 0
 
def hash(x):
	global idx
	if hash_table[x] == -1:
		hash_table[x] = idx
		idx += 1
	return hash_table[x]
 

data.readline()
for line in data:
	x, y = map(hash, map(int, line.split(",")))
	out_degree[x] += 1
	m[y].append(x)
 

 
t = 0
begin = time()
 
while True:
	for i in range(N):
		r[i] = 0
		for in_id in m[i]: 
			r[i] += tax_rate * r2[in_id] / out_degree[in_id]
	der = 1 - sum(r)
	for i in range(N):
		r[i] += der / N
 
	tag = 0
	for i in range(N):
		if fabs(r[i]-r2[i]) > eps:
			tag = 1
			break
	for i in range(N):
		r2[i] = r[i]
	t += 1
	if tag == 0:
		break
 
end = time()
print (r[hash(99)])
print ('total iteration is %d' % t)
print ('total time is %f' % (end - begin))

