# Particle Swarm Optimization (PSO) Algorithm
This is the simple and classic version of the particle swarm optimization (PSO) algorithm for solving the following constrained minimization problem:

<a href="https://www.codecogs.com/eqnedit.php?latex=min&space;\big\{(x_0-6)^2&plus;(x_1-0.5)^6&plus;100x_1&plus;10x_0\big\}&space;\quad&space;s.t.&space;\quad&space;x_0\le5,&space;\quad&space;x_1\ge&space;2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?min&space;\big\{(x_0-6)^2&plus;(x_1-0.5)^6&plus;100x_1&plus;10x_0\big\}&space;\quad&space;s.t.&space;\quad&space;x_0\le5,&space;\quad&space;x_1\ge&space;2" title="min \big\{(x_0-6)^2+(x_1-0.5)^6+100x_1+10x_0\big\} \quad s.t. \quad x_0\le5, \quad x_1\ge 2" /></a>

The solution for this problem also can be obtained using an analytical approach, like KKT conditions, and hence, the correctness of the algorithm can be observed. The solution is <a href="https://www.codecogs.com/eqnedit.php?latex=x_0&space;=&space;1,&space;x_1&space;=&space;2" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_0&space;=&space;1,&space;x_1&space;=&space;2" title="x_0 = 1, x_1 = 2" /></a>

This is a very simple version of the algorithm and the purpose was to give some basic insights about how this algorithm works. 


I used the following reference for the PSO algorithm:

B. S. G. de Almeida and V. C. Leite, Particle Swarm Optimization: A Powerful Technique for Solving Engineering Problems, in Swarm Intelligence, IntechOpen, 2019.


and to handle inequality constraints, I used the barrier method. See the following references to get more details regarding this method:

S. Boyd, L. Vandenberghe, Convex Optimization, Cambridge University Press, 2004.

Mahdi Khojastehnia, Massive MIMO Channels Under the Joint Power Constraints, University of Ottawa, 2019.


