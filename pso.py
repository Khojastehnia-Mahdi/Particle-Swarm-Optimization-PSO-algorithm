import numpy as np
import random
import matplotlib.pyplot as plt


# The following Particle Swarm Optimization (PSO) algorithm will 
# find the solution for the following problem:
# min f2(x0 ,x1) s.t. x0<5 & x1>2, where f2(x0, x1) = (x0-6)**2 + (x1-0.5)**6 + 100*x1 + 10*x0


# We use the barrier method to handle the inequality constraints.
def func(x0,x1):
    f0 = 1e100 if x0>5 else 0
    f1 = 1e100 if x1<2 else 0
    f2= (x0-6)**2 + (x1-0.5)**6 + 100*x1 + 10*x0
    return f0+f1+f2


numberPar = 40  # number of particles
NumItr = 100    # number of iterations
wMax = 0.2      # max of inertia weight
wMin = 0.05     # min of inertia weight

# The chance of reaching the global optimum (here global minimum) increases for smaller values of w.

# initialization
X = np.zeros((numberPar, 2))
V = np.zeros((numberPar, 2))
Objective = np.zeros((numberPar,))
Pbest = np.zeros((numberPar, 2))

for i in range(numberPar):
    # we need to make sure that the initial values are in the feasible set.
    x0New = 4.5*np.random.rand()
    x1New = 2+np.random.rand()
    X[i,:] = np.array([x0New, x1New])
    V[i,:] = np.random.rand(2)
    Objective[i] = func(X[i,0], X[i,1])
    Pbest[i,:] = X[i,:]
Gbest = X[np.argmin(Objective),:] 



# the main loop for the pso algorithm
t = 0 
c1 = 1     # individual-cognition parameter
c2 = 1     # social learning parameter
obj = []
while t<NumItr:
    w = wMax - ((wMax-wMin)*t/NumItr)
    for i in range(numberPar):
        # updating the velocity and the position
        r1 = random.random()
        r2 = random.random()
        oldV = X[i,:]
        oldX = V[i,:]
        newV0 = w*oldV[0] + c1*r1*(Pbest[i,0] - oldX[0]) + c2*r2*(Gbest[0] - oldX[0])
        newV1 = w*oldV[1] + c1*r1*(Pbest[i,1] - oldX[1]) + c2*r2*(Gbest[1] - oldX[1])

        newX0 = oldX[0] + newV0
        newX1 = oldX[1] + newV1

        X[i,:] = np.array([newX0, newX1])
        V[i,:] = np.array([newV0,newV1])

        # updating the best position for i'th particle
        if func(Pbest[i,0], Pbest[i,1])>func(newX0,newX1):
            Pbest[i,:] = np.array([newX0,newX1])

        # updating the best position for all particles
        if func(Gbest[0], Gbest[1])>func(newX0,newX1):
            Gbest = np.array([newX0,newX1])
        
    obj.append(func(Gbest[0], Gbest[1]))

    t = t+1

# x0 = 1 and x1 = 2 are the optimla points. 
# Let's compare the result obtained from PSO with that by the analytical approach.
print('Gbest = ',Gbest)
print('min f2(x0,x1) st. x0<5, x1>2 = ', func(Gbest[0],Gbest[1]))
print('Accuracy of the algorithm [%] = ', ((func(Gbest[0],Gbest[1])-func(1,2))/func(1,2))*100)

# plot the result for each iteration
plt.plot(range(NumItr), obj, 'k-')
plt.plot(range(NumItr), func(1,2)*np.ones((NumItr,)), 'r--')
plt.ylim(200, 300)
plt.xscale("log")
plt.xlabel('Step')
plt.ylabel('Objective function')
plt.title('PSO - constrained minimization problem')
plt.show()
