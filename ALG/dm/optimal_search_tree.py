#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# minimum search tree
# christoph durr - 2014-2018

from random import randint, seed
from sys import exit

seed(1)

from A import main as student  # cette ligne doit être adapté à chaque devoir rendu

def search(tree, key):
	""" searches a key in a binary search tree

	:param tree: of the form [left, center, right], 
			where left, right are subtrees and center is the label of the root, 
			which is an integer between 0 and n - 1, 
			for n being the number of nodes in the tree.
			Empty tress are represented as None.
	:returns: the node of the tree labeled key.
	"""
	curr = tree
	while curr:
		left, center, right = tree
		if center == key:
			return tree
		elif center < key:
			curr = right
		else:
			curr = left
	return None


def ancestor_tree(tree, n):
	""" produces an ancestor list of a given tree.

	:param tree: of the form [left, center, right], 
			where left, right are subtrees and center is the label of the root, 
			which is an integer between 0 and n - 1, 
			for n being the number of nodes in the tree.
			Empty tress are represented as None.
	:param n: number of nodes in the tree 
	:complexity: linear in the size the tree
	:returns: a list anc, such that anc[u] == v iff
		the node with label u has an ancestor with label v.
	"""
	anc = [0] * n
	Q = [(tree, tree[1])]
	while Q:
		[[left, center, right], father] = Q.pop()
		anc[center] = father
		for subtree in [left, right]:
			if subtree is not None:
				Q.append([subtree, center])
	return anc

def optimal_search_tree(freq):
	"""Optimal binary search tree 
		by 
		Optimum Binary Search Trees, D. E. KNUTH , Acta Informatica 1, 14-25 (1971) 

	:param freq: list of frequencies for each element 
	             of rank 0 to n-1, for n = len(freq)
	:returns: a binary search tree in form of a list.
			every node of the tree is a list [left, center, right]
			where left, right are subtrees and center is the index of its root. 
	:complexity: `O(n^2)`
	"""
	n = len(freq)
	N = range(n + 1)
	# [i,j] define subproblem for items from i to j (included)
	# [i+1,i] is the empty subproblem
	# weight[i][j] = total weight (frequencies) of subproblem
	# tree[i][j] = optimal tree for subproblem
	# root[i][j] = label at its root
	# cost[i][j] = cost of this tree
	root = [[i for j in N] for i in N]
	cost = [[float('inf') for j in N] for i in N]
	tree = [[None for j in N] for i in N]
	weight = [[0 for j in N] for i in N]
	# base cases
	for i in range(n):
		weight[i][i] = cost[i][i] = freq[i]
		tree[i][i] = [None, i, None]
	for i in range(n + 1):
		weight[i][i - 1] = cost[i][i - 1] = 0
	# recursion
	for i in range(n-1, -1, -1):
		for j in range(i + 1, n):
			weight[i][j] = weight[i][j - 1] + freq[j]
			for r in range(root[i][j - 1], root[i + 1][j] + 1):
				alt = cost[i][r - 1] + weight[i][j] + cost[r + 1][j]
				if alt < cost[i][j]:
					cost[i][j] = alt
					root[i][j] = r
					tree[i][j] = [tree[i][r - 1], r, tree[r + 1][j]]
	# return the optimal tree (not unique)
	# print("root=", root)
	# print("cost=", cost)
	# print("tree=", tree)
	# print("weight=", weight)
	return tree[0][n - 1]

def cost_tree(anc, freq):
	n = len(anc)
	desc = [[] for _ in range(n)]
	root = None
	for i in range(n):
		if not( 0 <= anc[i] < n):
			return -1
		if anc[i] == i:
			if root is None:
				root = i
			else:
				return -2
		else:
			desc[anc[i]].append(i)
	if root is None:
		return -3
	if max(map(len, desc)) > 2:
		return -4
	# explore bottom up
	level = [0] * n
	level[root] = 0
	Q = [root]
	while Q:
		v = Q.pop()
		for u in desc[v]:
			level[u] = level[v] + 1
			Q.append(u)
	return sum(freq[v] * level[v] for v in range(n))


if __name__ == "__main__":

	# print(ancestor_tree(optimal_search_tree([10, 1]), 2))

	print("test correctness")
	for n in [4, 2, 3, 4, 5, 10, 100]:
		for _ in range(4):
			freq = [randint(0, 1000) for _2 in range(n)]
			t = optimal_search_tree(freq)
			sol = ancestor_tree(t, len(freq))
			stu = student(freq)
			print(freq, stu)
			c_sol = cost_tree(sol, freq)
			# print("(", end='')
			c_stu = cost_tree(stu, freq)
			# print(")", end='')
			if c_stu != c_sol:
				print(freq, sol, c_sol, stu, c_stu)
				# exit(0)

	print("test complexity")
	freq = [randint(0, 1000) for _ in range(1000)]
	student(freq)
