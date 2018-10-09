---
title: OPAL 2019
---

Spring school on Optimization and Algorithms in Dynamic Environments. 

This school is organized by the Institute of Mathematics (VAST), Hanoi, Vietnam, and supported by the South East Asian Mathematical Society.

Objective: Introduction to the current optimization and algorithmic techniques in online algorithms, stochastic programming and online learning. The school is two week long from 18 Feb to 1 March 2019. There are three mini-courses, each consists of 6 x 120 minute lectures in addition with the introduction and conclusion. There will be exercise section everyday from 16h30-17h30. The courses require only basic knowledge on linear algebra, calculus and probability. 
The school is followed by a closely related workshop “Algorithms, Optimization and Learning in Dynamic Environments” organized at the Vietnam Institute of Mathematics (VAST) and the Vietnam Institute for Advanced Study in Mathematics (VIASM) in Hanoi  from 4 March to 8 March 2019. 

# Feb 18th, 2019 to March 1st

### Lecture 1: Competitive analysis of online algorithms.

Lecturer: Christoph Dürr

Abstract: The online computation paradigm applies to situations where the input of a computational problem is provided in form of a request sequence to the algorithm. The algorithm has to serve each request with some action that will generate a cost depending on the current configuration. Classical examples include the ski-rental problem, the caching problem, the k-server problem and the TCP acknowledgement problem, as well as online versions of the classical combinatorial optimization problems. Interesting variants are the secretary problem and the cow path problem. The performance of an online algorithm is typically measured with the so-called competitive ratio. It compares the performance of the algorithm to the optimal offline solution, and measures the price of not knowing the future requests in advance. In this course, we will cover the algorithmic ideas that are useful for these problem, as well as adversarial constructions to show impossibility results. The ultimate goal of the course is to understand the primal dual framework for online problems.

##### References:

* The Design of Competitive Online Algorithms Via a Primal-Dual Approach by Naor and Buchbinder.

##### Detailed plan:

1.	Ski rental. Basic concepts.
2.	Scheduling. Charging schemes.
3.	Buffer management. Collecting items from a dynamic queue. Open problems.
4.	Caching. Bijective analysis.
5.	The k-server problem. The work function algorithm.
6.	The primal dual framework for online algorithms.

### Lecture 2: Introduction to Stochastic Programming
Lecturer: Nguyễn Việt Hưng. Abstract: The aim of the course is to introduce the main notions of stochastic programming:  multistage stochastic programming, chance constrained programming, stochastic integer programming, decomposition, primal method, dual method.##### Detailed plan:
1.	Introduction to Stochastic Programming2.	Duality and Optimality3.	Decomposition methods4.	Probabilistic Constraint Programming5.	Integer Stochastic Programming 6.	Applications of Stochastic Programming##### References:* John Birge and François Louveaux, Introduction to Stochastic Programming. Springer Series in Operations Research and Financial Engineering, 2011.* Alexander Shapiro, Darinka Dentcheva and Andrzej Ruszczynski. Lectures on Stochastic Programming: Model and Theory. MOS-SIAM Series on Optimization, 2009.

### Lecture 3: Online Learning/Online Convex Optimization.
Lecturer: Nguyễn Kim Thắng and Lê Hải Yến
Abstract: The aim of the course is to introduce modern tools to design optimization algorithms in online learning that are robust in dynamically evolving settings. We will cover fundamental concepts and present challenges in order to understand the mathematics of machine learning, in particular deep learning.  ##### Detailed plan:
1.	Introduction. Gentle start: Learning from Experts.2.	Gradient Descent/Stochastic Gradient Descent. Upper and lower bounds. Applications: support vector machine (SVM) training.3.	Mirror Descent. Regularization. Applications.4.	Bandit Convex Optimization. 5.	Projection-free Algorithms. Second order methods.6.	Learning Theory and Applications.##### References:
* Elad Hazan, Introduction to Online Convex Optimization. Foundations and Trends in Optimization, 2016.* Sébastien Bubeck, Convex Optimization: Algorithms and Complexity. Foundations and Trends in Machine Learning, 2015.
### Tentative Schedule


| date   | 9-11                                                         | 14-16                                                               |
|--------|--------------------------------------------------------------|---------------------------------------------------------------------|
|   18/2 |      Introduction                                            | Christoph: Ski rental. Basic concepts.                              |
|   19/2 |      Hưng: Introduction to Stochastic Programming.           | Thắng/Yến: Standard notions. Learning from Experts.                 |
|   20/2 |     Christoph: Scheduling. Charging schemes.                 | Hưng: Duality and Optimality.                                |
|   21/2 |     Thắng/Yến: Gradient Descent                              | Christoph: Buffer management. Collecting items from a dynamic queue |
|   22/2 |     Hưng: Decomposition methods.                             | Thắng/Yến: Mirror Descent and Regularization                        |
|        |                                                              |                                                                     |
|   25/2 |     Christoph: Caching. Bijective analysis                   | Hưng: Probabilistic Constraint Programming.                  |
|   26/2 |     Thắng/Yến: Bandit Convex Optimization                    | Christoph: The k-server problem. The work function algorithm        |
|   27/2 |     Hưng: Integer Stochastic Programming.                    | Thắng/Yến: Projection-Free Algorithms and Second Order Methods      |
|   28/2 |     Christoph: Primal-dual framework.                        | Hưng: Applications of Stochastic Programming.                |
|   1/3  |     Thắng/Yến: Connection with Learning Theory and Appl.     | Conclusion.                                                         |

