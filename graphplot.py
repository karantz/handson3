import numpy as np
import matplotlib.pyplot as plt
import timeit

def f(n):
    x = 1
    for i in range(n):
        for j in range(n):
            x += 1
    return x

#n_values = np.arange(1,1001,50) 
n_values=list(range(1,100)) # You can adjust the range for larger values
time_values = []

for n in n_values:
    time_taken=timeit.timeit(lambda: f(n),number=10)
    time_values.append(time_taken)
    #start_time = time.time()
    #f(n)
    #end_time = time.time()
    #time_values.append(end_time - start_time)

# Fit a polynomial curve
coefficients = np.polyfit(n_values, time_values, 2)  # Quadratic fit
polynomial = np.poly1d(coefficients)
fitted_curve = polynomial(n_values)

plt.figure(figsize=(10, 6))
plt.plot(n_values, time_values, '.-', label='Measured time')
plt.plot(n_values, fitted_curve, 'r--', label='Fitted polynomial')

# Approximate n_0 (choose an appropriate value based on your plot)
n_0 = 30 # Example value
plt.axvline(x=n_0, color='g', linestyle='--', label=f'n_0 ≈ {n_0}')
plt.scatter(n_0, time_values[n_0-1], color='g', zorder=5)  # Mark n_0 on the plot
plt.text(n_0, time_values[n_0-1], f'  n_0 = {n_0}', verticalalignment='bottom', horizontalalignment='right')

plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Time vs n')
plt.legend()
plt.grid(True)
plt.show()



