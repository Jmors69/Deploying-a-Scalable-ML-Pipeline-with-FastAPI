# Census Income Prediction Model Card

## Model Details
- **Model type:** Random Forest Classifier
- **Framework:** scikit-learn
- **Input data:** U.S. Census Income Dataset
- **Prediction target:** Income category (`<=50K` or `>50K`)

---

## Intended Use
This model is intended to predict whether an individual earns more than $50K per year based on demographic and employment-related features.  
It is designed for educational purposes and should **not** be used for real-world decision-making.

---

## Training Data
The model was trained on the U.S. Census Income dataset, which includes features such as:
- Age
- Work class
- Education
- Marital status
- Occupation
- Relationship
- Race
- Sex
- Capital gain/loss
- Hours per week
- Native country

---

## Evaluation Data
The evaluation dataset is a held-out test split from the same Census dataset to ensure consistency between training and testing distributions.

---

## Metrics
The model was evaluated using **precision**, **recall**, and **F1 score**.

### Overall Model Performance
- **Precision:** 0.74  
- **Recall:** 0.64  
- **F1 Score:** 0.68  

Additionally, slice-based performance metrics were computed across different demographic groups to assess potential bias.

---

## Ethical Considerations
This model uses sensitive demographic features (e.g., race, sex, native country).  
Predictions may reflect historical biases present in the training data.  
Care should be taken to avoid discriminatory or harmful downstream use.

---

## Caveats and Recommendations
- The model performance varies across demographic slices.
- The dataset may not represent all populations equally.
- Further bias analysis and fairness evaluation are recommended before any production use.


