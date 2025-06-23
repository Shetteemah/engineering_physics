import numpy as np
import matplotlib.pyplot as plt

# Constants and Assumptions
R = 8.314  # Gas constant, J/(mol·K)
n = 1.0    # Number of moles, mol
T_i = 293  # Initial temperature (room), K
T_a = 303  # Environment temperature, K
V_1 = 1.0  # Initial volume, m^3 (arbitrary starting point)
P_1 = n * R * T_i / V_1  # Initial pressure, Pa
gamma = 5/3  # Adiabatic index for monatomic gas

# Step 1: Isothermal Expansion (1 → 2) at T_i
V_2 = 2.0 * V_1
P_2 = P_1 * V_1 / V_2

# Step 2: Adiabatic Expansion (2 → 3) to T_a
V_3 = V_2 * (T_a / T_i) ** (1 / (1 - gamma))
P_3 = P_2 * (V_2 / V_3) ** gamma

# Step 3: Isothermal Compression (3 → 4) at T_a
V_4 = V_3 / 2
P_4 = P_3 * V_3 / V_4

# Step 4: Adiabatic Compression (4 → 1) back to T_i
V_1_check = V_4 * (T_i / T_a) ** (1 / (1 - gamma))
P_1_check = P_4 * (V_4 / V_1) ** gamma

V_iso_exp = np.linspace(V_1, V_2, 2)
P_iso_exp = P_1 * V_1 / V_iso_exp

V_ad_exp = np.linspace(V_2, V_3, 2)
P_ad_exp = P_2 * (V_2 / V_ad_exp) ** gamma

V_iso_comp = np.linspace(V_3, V_4, 2)
P_iso_comp = P_3 * V_3 / V_iso_comp

V_ad_comp = np.linspace(V_4, V_1, 2)
P_ad_comp = P_4 * (V_4 / V_ad_comp) ** gamma

plt.figure(figsize=(8, 6))
plt.plot(V_iso_exp, P_iso_exp, 'b-', label='1 → 2: Isothermal Expansion (T_i)')
plt.plot(V_ad_exp, P_ad_exp, 'r-', label='2 → 3: Adiabatic Expansion')
plt.plot(V_iso_comp, P_iso_comp, 'g-', label='3 → 4: Isothermal Compression (T_a)')
plt.plot(V_ad_comp, P_ad_comp, 'm-', label='4 → 1: Adiabatic Compression')
plt.plot(V_1, P_1, color='#1ABC9C', marker='o', label='Point 1')
plt.plot(V_2, P_2, color='#9B59B6', marker='o', label='Point 2')
plt.plot(V_3, P_3, color='#F1C40F', marker='o', label='Point 3')
plt.plot(V_4, P_4, color='#E74C3C', marker='o', label='Point 4')
plt.xlabel('Volume (m³)')
plt.ylabel('Pressure (Pa)')
plt.title('p-V Diagram of Carnot Cycle for Air-Conditioner')
plt.grid(True)
plt.legend()
plt.yscale('log')
plt.xlim(0, 2.5 * V_1)
plt.show()

print(f"Initial Pressure (P_1): {P_1:.2f} Pa")
print(f"Point 2: P_2 = {P_2:.2f} Pa, V_2 = {V_2} m³")
print(f"Point 3: P_3 = {P_3:.2f} Pa, V_3 = {V_3:.2f} m³")
print(f"Point 4: P_4 = {P_4:.2f} Pa, V_4 = {V_4} m³")