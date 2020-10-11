#!/usr/bin/env python3

import svgwrite
from svgwrite import cm


def normalize(s):
	((a, b, c),
	 (d, e, f),
	 (g, h, i)) = s
	return min(((c, f, i),
				(b, e, h),
				(a, d, g)),
			   ((i, h, g),
				(f, e, d),
				(c, b, a)),
			   ((c, b, a),
				(f, e, d),
				(i, h, g)),
			   ((a, d, g),
				(b, e, h),
				(c, f, i)),
			   ((g, h, i),
				(d, e, f),
				(a, b, c)),
			   ((i, f, c),
				(h, e, b),
				(g, d, a)),
			   ((g, d, a),
				(h, e, b),
				(i, f, c)), s)


def set(s, i, j, v):
	M = list(list(row) for row in s)
	M[i][j] = v
	return normalize(tuple(tuple(row) for row in M))


def eval(s):
	((a, b, c),
	 (d, e, f),
	 (g, h, i)) = s
	lines =  [(a,b,c), (d,e,f), (g,h,i), (a,d,g), (b,e,h), (c,f,i), (a,e,i), (c,e,g)]
	for (x,y,z) in lines:
		if x and x == y == z:
			return x
	return 0


def opponent(turn):
	if turn == 1:
		return 2
	else:
		return 1


def name(ts):
	return ''.join(''.join(map(str,row)) for row in ts[1])


corr = ".ox"
def label(ts):
	return "\n".join(''.join(corr[x] for x in row) for row in ts[1])


# build graph

root  = (1,((0,0,0),(0,0,0),(0,0,0)))
graph = {root:[]}
win = {}

order = []
Q = [root]
while Q:
	ts = Q.pop()
	order.append(ts)
	turn, s = ts
	w = eval(s)
	if w:
		win[ts] = w
	else:
		for i in range(3):
			for j in range(3):
				if s[i][j] == 0:
					s1 = set(s, i, j, turn)
					turn1 = opponent(turn)
					ts1 = (turn1, s1)
					if ts1 not in graph[ts]:
						graph[ts].append(ts1)
						if ts1 not in graph:
							graph[ts1] = []
							Q.append(ts1)


color = {1: 'white', 2: 'black'}


for ts in graph:
	dwg = svgwrite.Drawing('n/' + name(ts) + '.svg')
	for i in range(4):
		dwg.add(dwg.line((0 * cm, i * cm), (3 * cm, i * cm), stroke='gray'))
		dwg.add(dwg.line((i * cm, 0 * cm), (i * cm, 3 * cm), stroke='gray'))
	for i in range(3):
		for j in range(3):
			x = ts[1][i][j]
			if x:
				dwg.add(dwg.circle(center=((j + 0.5)*cm, (i + 0.5)*cm), r='0.45cm', stroke='black', fill=color[x]))
	dwg.save()

f = open("n/tree.dot", "w")
print("digraph {", file=f)
for s in graph:
	# print(name(s), '[shape=none, scale=true, image="%s.svg", label="%"]' % name(s), file=f)
	print(name(s), '[shape=box,label="%s"]' % label(s), file=f)
	for s1 in graph[s]:
		print(name(s), '->', name(s1), file=f)
print("}", file=f)

print(len(graph))
print(len([s for s in graph if not graph[s]]))

# for s in graph:
# 	if not graph[s]:
# 		print(label(s))
# 		print('\t', eval(s[1]))


