from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def create_teleportation_circuit():
    qc = QuantumCircuit(3, 3)

    # Prepare unknown state
    qc.h(0)
    qc.barrier()

    # Entangle qubit 1 and 2
    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    # Bell measurement
    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    # Measure qubit 0 and 1
    qc.measure(0, 0)
    qc.measure(1, 1)
    qc.barrier()

    # Conditional correction
    qc.cx(1, 2)
    qc.cz(0, 2)

    # Final measurement
    qc.measure(2, 2)
    return qc

def simulate_circuit(qc, shots=1024):
    simulator = AerSimulator()
    compiled = transpile(qc, simulator)
    job = simulator.run(compiled, shots=shots)
    result = job.result()
    return result.get_counts()

def main():
    qc = create_teleportation_circuit()
    counts = simulate_circuit(qc)
    print("Counts:", counts)
    plot_histogram(counts)
        # Save circuit image
    qc.draw('mpl', filename='circuit_diagram.png')

    plt.show()

if __name__ == "__main__":
    main()
