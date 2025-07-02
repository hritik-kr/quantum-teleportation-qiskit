import unittest
from teleportation import create_teleportation_circuit, simulate_circuit

class TestQuantumTeleportation(unittest.TestCase):

    def test_circuit_structure(self):
        qc = create_teleportation_circuit()
        self.assertEqual(qc.num_qubits, 3)
        self.assertEqual(qc.num_clbits, 3)
        self.assertGreater(len(qc.data), 0)

    def test_simulation_output(self):
        qc = create_teleportation_circuit()
        counts = simulate_circuit(qc, shots=512)
        self.assertIsInstance(counts, dict)
        self.assertGreater(len(counts), 0)
        for key, val in counts.items():
            self.assertTrue(all(bit in "01" for bit in key))
            self.assertIsInstance(val, int)

if __name__ == '__main__':
    unittest.main()
