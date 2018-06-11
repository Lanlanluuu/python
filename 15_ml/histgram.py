import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 8))

# Fixing random state for reproducibility
#np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

#print(x[:100])
x.sort()
xlen = len(x)
low = x[int(xlen/3)]
high = x[int(xlen*2/3)]
#print(low,high)

def level(iq,low,high):
    if iq < low:
        return "low"
    elif iq < high:
        return "medium"
    else:
        return "high"
print(level(85,low,high))

plt.subplot(121)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
#plt.axis([40, 160, 0, 0.03])
plt.grid(True)
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.show()
