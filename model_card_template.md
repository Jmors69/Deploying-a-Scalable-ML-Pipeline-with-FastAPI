\# Model Card

---



\## Model Details

This model is a \*\*RandomForestClassifier\*\* trained to predict whether an individual earns \*\*more than $50K per year\*\* based on U.S. Census demographic data.



\- Model type: Random Forest (scikit-learn)

\- Task: Binary classification

\- Output labels: `<=50K`, `>50K`



---



\## Intended Use

This model is intended \*\*for educational purposes only\*\* as part of the Udacity \*Deploying a Scalable ML Pipeline with FastAPI\* project.



It should \*\*not\*\* be used for real-world income prediction or decision-making.



---



\## Training Data

The model was trained using the \*\*UCI Census Income dataset\*\* provided by Udacity.  

The dataset contains demographic and employment-related features such as:



\- Age

\- Education

\- Occupation

\- Marital status

\- Hours worked per week

\- Native country



The target variable indicates whether annual income exceeds $50K.



---



\## Evaluation Data

The dataset was split into training and test sets using an \*\*80/20 split\*\* prior to training.  

Model evaluation was performed on the held-out test set.



---



\## Metrics

The following metrics were used to evaluate model performance:



\- Precision

\- Recall

\- F1-score



Overall performance was reasonable for the task, with metrics varying across different categorical data slices.  

Detailed slice-level performance results are documented in \*\*`slice\_output.txt`\*\*.



---



\## Ethical Considerations

The dataset includes sensitive demographic attributes such as \*\*sex, race, and nationality\*\*.  

Predictions may reflect historical biases present in the data.



This model should not be used in high-stakes or decision-making contexts without additional fairness analysis and bias mitigation.



---



\## Caveats and Recommendations

\- This model is not production-ready.

\- Additional bias and fairness evaluation is recommended.

\- Model performance may vary significantly across demographic subgroups.

\- Monitoring and retraining would be required for real-world deployment.

