from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# Step 1: Prepare qubit 0 in an arbitrary state |ψ>
qc.h(0)
qc.barrier()

# Step 2: Entangle qubit 1 and 2
qc.h(1)
qc.cx(1, 2)
qc.barrier()

# Step 3: Bell measurement on qubit 0 and 1
qc.cx(0, 1)
qc.h(0)
qc.barrier()

# Step 4: Measure qubit 0 and 1
qc.measure([0, 1], [0, 1])
qc.barrier()

# Step 5: Conditional operations
qc.cx(1, 2)
qc.cz(0, 2)

# Step 6: Final measurement of qubit 2 (teleported state)
qc.measure(2, 2)

# Run the circuit
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, simulator, shots=1024).result()
counts = result.get_counts()

# Plot results
print("Measurement counts:", counts)
plot_histogram(counts)
plt.show()
