import numpy as np

def predict_anomaly(values):
    x = np.array(values)

    # Fake "quantum kernel" distance
    score = float(np.exp(-np.linalg.norm(x)))

    label = "anomaly" if score < 0.5 else "normal"

    return label, score
