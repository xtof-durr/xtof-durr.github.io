---
title: Internship on scheduling with testing
---

## Details

This internship is proposed for Master's students of MPRI, and will be supervised by Spyros Angelopoulos and Christoph Dürr, in the Sorbonne Université, LIP6.

## Subject

The traditional framework for combinatorial optimization problems has a clearly defined input which is given to an algorithm. The latter computes a solution, which has to satisfy some constraints and minimize some cost function.  However, it happens that, in some situations, obtaining the data is in fact the hard part of the problem.  Everyone who has done some intrustrial project can certify to this.

In this internship we will study a specific scheduling problem, which at first may look quite innocent. A similar problem has been studied in Dürr et al 2018. You are given n jobs, each has a processing time p or q, for some given $p < q$.  We, as an algorithm, need to schedule these jobs on a single machine, and the objectif value is the total completion times of the jobs.  The optimal schedule consists of scheduling first all p-length jobs then all q-length jobs.  However we don't know the processing of each job, unless we execute it, or we make a test. A test takes a single time unit and reveals the processing time.  It is known that the following behavior is dominant: If the test reveals length p, then the job can be scheduled right away, otherwise its execution will be delayed towards the end of the schedule.  Hence an algorithm is completely described by a word from $\\{T,E\\}^n$, where the i-th letter states whether the i-th job considered by the algorithm will be tested or executed unitested. 

We propose two measures for an algorithm. Namely the traditionnal *competitive ratio*, which divides the algorithm's cost by the optimal optimal, and the *regret*, which subtracts these two costs.  The goal of this internship is to identify the best algorithm for each of these measures, as a function of $p, q, n$.  The right approach is to start with small values of $n$, $2,3,4,$ etc, and too see a pattern emerging from these preliminary studies.  The outcome of this work would be either a clear theoretical description of the optimal algorithm, an experimental study or a combinatorion of the two. In both cases a publication in an appropriate venue is expected.

## Bibliography

The student should read during the internship at least the following documents.

- Y. Shaposhnik. Exploration vs. Exploitation: Reducing Uncertainty in Operational Problems. PhD thesis, Sloan School of Management, MIT, 2016. (to be read partially)
- R. Levi. Practice driven scheduling models. Talk at Dagstuhl Seminar 16081: Scheduling, 2016.
- S. Kahan. A model for data in motion. In 23rd Annual ACM Symposium on Theory of Computing (STOC’91), pages 267–277, 1991.
- C. Dürr, Thomas Erlebach, Nicole Megow, Julie Meißner. Scheduling with Explorable Uncertainty.  The 9th Innovations in Theoretical Computer Science Conference (ITCS), Jan 2018. 

## Appendix

Here are some experiments that we already conducted for non adaptive algorithms, for the small instance with 4 jobs.  Every point in the diagram corresponds to a specific value p (the column) and q (the row). Each letter in this grid indicates the best algorithm for the corresponding values $p,q$. It can be observed that all these algorithms are described by a word of the form $T^*E^+$.  Proving this property would be one starting point for the intern.

![](19scheduling_testing.png)