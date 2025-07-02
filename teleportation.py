from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create the teleportation circuit
qc = QuantumCircuit(3, 3)

# Step 1: Prepare an unknown state on qubit 0 (e.g., Hadamard)
qc.h(0)
qc.barrier()

# Step 2: Entangle qubits 1 and 2
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Step 3: Bell-state measurement on qubits 0 and 1
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# Step 4: Measure qubits 0 and 1
qc.measure(0, 0)
qc.measure(1, 1)
qc.barrier()

# Step 5: Apply correction based on classical results
qc.cx(1, 2)
qc.cz(0, 2)

# Step 6: Measure the teleported qubit
qc.measure(2, 2)

# Simulate with AerSimulator
simulator = AerSimulator()
compiled_qc = transpile(qc, simulator)  # THIS is the correct way
job = simulator.run(compiled_qc, shots=1024)
result = job.result()
counts = result.get_counts()

# Output results
print("Measurement counts:", counts)
plot_histogram(counts)
plt.show()
