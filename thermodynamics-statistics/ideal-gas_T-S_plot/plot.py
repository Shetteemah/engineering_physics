import numpy as np
import matplotlib.pyplot as plt

# Constants
R = 8.314  # J/(mol·K)
C_v = 1.5 * R  # J/(mol·K)
C_p = 2.5 * R  # J/(mol·K)
T_1 = 300  # K
Q = 1000  # J
n = 1  # mol
S_0 = 0  # Reference entropy

# Isothermal
Delta_S_iso = Q / T_1
S_iso = np.array([S_0, S_0 + Delta_S_iso])
T_iso = np.array([T_1, T_1])

# Isochoric
T_2_v = T_1 + Q / (n * C_v)
T_v = np.linspace(T_1, T_2_v, 100)
S_v = S_0 + C_v * np.log(T_v / T_1)

# Isobaric
T_2_p = T_1 + Q / (n * C_p)
T_p = np.linspace(T_1, T_2_p, 100)
S_p = S_0 + C_p * np.log(T_p / T_1)

# Plot
plt.figure(figsize=(8, 6))
plt.plot(S_iso, T_iso, 'b-', label='Isothermal (ΔS = 3.333 J/K)')
plt.plot(S_v, T_v, 'r-', label='Isochoric (ΔS = 2.933 J/K)')
plt.plot(S_p, T_p, 'g-', label='Isobaric (ΔS = 3.076 J/K)')
plt.xlabel('Entropy (J/K)')
plt.ylabel('Temperature (K)')
plt.title('T-S Diagram for Ideal Gas Processes (Q = 1000 J)')
plt.grid(True)
plt.legend()
plt.show()
