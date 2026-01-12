import numpy as np
from ml.model import train_model, inference, compute_model_metrics


def test_train_model_returns_model():
    X = np.random.rand(20, 5)
    y = np.random.randint(0, 2, 20)
    model = train_model(X, y)
    assert model is not None


def test_inference_output_shape():
    X = np.random.rand(20, 5)
    y = np.random.randint(0, 2, 20)
    model = train_model(X, y)
    preds = inference(model, X)
    assert len(preds) == len(X)


def test_compute_model_metrics_range():
    y_true = np.array([0, 1, 1, 0])
    y_pred = np.array([0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    assert 0.0 <= precision <= 1.0
    assert 0.0 <= recall <= 1.0
    assert 0.0 <= fbeta <= 1.0

