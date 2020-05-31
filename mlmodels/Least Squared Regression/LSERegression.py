import matplotlib.pyplot as plt
import numpy as np

# Class function
def class1(numsamp, mu, theta,scalex,scaley):
    # Define the covariance
    R = np.matrix([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
    S = np.matrix([[scalex, 0.0],[0.0,scaley]])
    cov = R*S*S*np.transpose(R)
    x, y = np.random.multivariate_normal(mu, cov, numsamp).T

    return x,y

def gen_line(w,minr,maxr,nsamp):
    # Generate samples for x
    x = np.array(np.linspace(minr,maxr,nsamp))

    # Generate the samples for y
    y = -w[0,0]/w[2,0]-(w[1,0]/w[2,0])*x

    return x,y

# Sample number for Gaussians
nsamples = 100

# For the lines
nsamp = 10

# Building the samples
x1,y1 = class1(nsamples, [4.0,1.0], np.pi/8.0 ,2.0,0.5)
x2,y2 = class1(nsamples, [1.0,4.0], np.pi/8.0 ,2.0,0.5)


#x=np.reshape(x1,:,1)

# Generate the X matrix
C1 = np.stack((np.ones(nsamples),x1,y1),axis = 1)
C2 = np.stack((np.ones(nsamples),x2,y2),axis = 1)
X = np.matrix(np.vstack((C1,C2)))

# Get the label array
y = np.matrix(np.vstack((np.ones((nsamples,1)),-np.ones((nsamples,1)))))

# Finally get the w for the decision surface
w = np.linalg.inv((np.transpose(X)*X))*np.transpose(X)*y

# Find the min and max of x coordinate
minr = np.amin(np.concatenate((x1,x2)))
maxr = np.amax(np.concatenate((x1,x2)))

# Generate the line
x3,y3 = gen_line(w,minr,maxr,nsamp)

# Plot Everything
plt.plot(x1, y1, 'bx')
plt.plot(x2, y2, 'ro')
plt.plot(x3, y3, 'g')
plt.axis('equal')
plt.savefig('LMSRegression.svg', transparent=True)
#plt.show()
