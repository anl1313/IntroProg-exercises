import numpy as np

def myfun(n):
    for i in range(n):
        print('hello world!')

vec = np.array([-2.5,-2.0,-1.5,-1.0,-0.5,0,0.5,1.0,1.5,2])

# b. Define probabilities
prob = np.exp(np.linspace(-2,2,vec.size))**5.6789 # all positive numbers
prob /= np.sum(prob) # make probabilities sum to one

# c. Get draws from distribution
x = np.random.choice(vec,size=10**6,p=prob)
def Rune(x):
    print(np.mean(x))
    
    