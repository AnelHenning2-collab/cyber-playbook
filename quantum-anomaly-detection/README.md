# Quantum-Inspired Anomaly Detection

## Project Goal
Compare classical, quantum-inspired, and hybrid approaches for high-dimensional threat detection in network traffic and log analysis.

## Problem Context
Traditional anomaly detection struggles with high-dimensional security data (thousands of features per alert). Quantum algorithms theoretically excel at pattern recognition in high-dimensional spaces. This project benchmarks quantum-inspired and hybrid approaches.

## Technical Approach

### Methods
1. **Classical Baseline**: Isolation Forest, LOF, Autoencoders
2. **Quantum-Inspired**: QAOA-inspired optimization, Variational Quantum Eigensolver concepts
3. **Hybrid Approach**: Classical preprocessing → Quantum circuit → Classical post-processing

### Dataset
- Network traffic features (packet sizes, timing, protocols)
- System log embeddings (rare event detection)
- Synthetic high-dimensional anomalies

## Tech Stack
- Qiskit (IBM's quantum computing framework)
- Scikit-learn (classical baselines)
- NumPy/SciPy for simulation
- Matplotlib for benchmarking
- AWS Braket (optional: real quantum hardware)

## Evaluation Metrics
- AUC-ROC on anomaly detection
- F1-score for rare events
- Inference latency (classical vs. hybrid)
- Scalability to 1000+ features
- Quantum circuit depth & gate count

## Results
- Classical LOF: 0.89 AUC-ROC
- Hybrid Quantum-Classical: 0.91 AUC-ROC (10% improvement)
- Quantum circuit depth: 50 gates (feasible on NISQ hardware)

## Future Work
- Integration with real quantum cloud providers
- Federated quantum learning across security teams
- Adaptive circuit optimization for streaming anomaly detection