from qiskit import QuantumCircuit, Aer, execute

def quantum_fork_decision():
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1).result()
    counts = result.get_counts()
    return "branch1" if "0" in counts else "branch2"
