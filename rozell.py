#rozell equation preformed on a 2d element 

#first iteration, setting up the equation
import numpy as np


s_t =np.array( [1, 2])
u_t =np.array( [0, 0])
a_t =np.array( [0, 0])
d_t = 0.1
phi = np.matrix(((0.5, 2),
	        (1, 3)))

b_t = s_t*phi

u_hat=np.array([0, 0])
identity=np.identity(2)


#transposing

b_t=b_t.T
u_t=u_t.T
a_t=a_t.T
u_hat=u_hat.T

i=0

def rozell_function(b_t, u_t, phi, identity, a_t, d_t):
    u_hat=(b_t-u_t-((phi.T*phi)-identity)*a_t)*d_t

    return u_hat


while i<100:
    
    u_hat=rozell_function(b_t,u_t,phi,identity,a_t,a_t)

    u_t=u_hat+u_T
    a_t=u_t
    i=i+1 
