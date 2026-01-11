import os

import pandas as pd
from sklearn.model_selection import train_test_split

from ml.data import process_data
from ml.model import (
    compute_model_metrics,
    inference,
    performance_on_categorical_slice,
    save_model,
    train_model,
)

CAT_FEATURES = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]


def main():
    project_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(project_path, "data", "census.csv")
    print(f"Loading data from: {data_path}")

    data = pd.read_csv(data_path)

    train, test = train_test_split(
        data,
        test_size=0.20,
        random_state=42,
        stratify=data["salary"] if "salary" in data.columns else None,
    )

    X_train, y_train, encoder, lb = process_data(
        train,
        categorical_features=CAT_FEATURES,
        label="salary",
        training=True,
        encoder=None,
        lb=None,
    )

    X_test, y_test, _, _ = process_data(
        test,
        categorical_features=CAT_FEATURES,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    model = train_model(X_train, y_train)
    preds = inference(model, X_test)

    precision, recall, fbeta = compute_model_metrics(y_test, preds)
    print(f"Precision: {precision:.4f} | Recall: {recall:.4f} | F1: {fbeta:.4f}")

    # Save model + encoder
    model_path = os.path.join(project_path, "model", "model.pkl")
    encoder_path = os.path.join(project_path, "model", "encoder.pkl")

    save_model(model, model_path)
    save_model(encoder, encoder_path)

    print(f"Saved model to: {model_path}")
    print(f"Saved encoder to: {encoder_path}")

    # Optional: slice metrics output
    slice_out = os.path.join(project_path, "slice_output.txt")
    with open(slice_out, "w", encoding="utf-8") as f:
        for col in CAT_FEATURES:
            for slice_value in sorted(test[col].dropna().unique()):
                count = (test[col] == slice_value).sum()
                p, r, fb = performance_on_categorical_slice(
                    test,
                    column_name=col,
                    slice_value=slice_value,
                    categorical_features=CAT_FEATURES,
                    label="salary",
                    encoder=encoder,
                    lb=lb,
                    model=model,
                )
                f.write(f"{col}: {slice_value}, Count: {count}\n")
                f.write(f"Precision: {p:.4f} | Recall: {r:.4f} | F1: {fb:.4f}\n\n")

    print(f"Wrote slice metrics to: {slice_out}")


if __name__ == "__main__":
    main()
