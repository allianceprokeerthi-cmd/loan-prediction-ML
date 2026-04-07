# 🏦 Loan Prediction ML Project

## 📌 Overview

This project focuses on building a Machine Learning model to predict whether a loan application will be **approved or rejected** based on applicant details.

The dataset is sourced from Kaggle and includes features such as income, loan amount, credit history, and more.

---

## 🎯 Problem Statement

Predict the **Loan Status**:

* `1` → Approved
* `0` → Rejected

This is a **binary classification problem**.

---

## 📂 Dataset Features

Some important features used:

* ApplicantIncome
* CoapplicantIncome
* LoanAmount
* Credit_History
* Gender, Education, Property_Area

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* XGBoost

---

## 🔍 Approach

### 1️⃣ Data Preprocessing

* Handled missing values
* Encoded categorical variables
* Removed unnecessary columns (e.g., Loan_ID)

---

### 2️⃣ Exploratory Data Analysis (EDA)

* Analyzed feature distributions
* Checked class imbalance
* Studied relationship with target variable

---

### 3️⃣ Handling Imbalance

* Used class balancing techniques
* Evaluated models using macro F1-score

---

### 4️⃣ Model Building

Models experimented with:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost ✅ (Final Model)

---

### 5️⃣ Model Tuning

* Hyperparameter tuning using GridSearchCV
* Cross-validation using Stratified K-Fold
* Optimized parameters like:

  * learning_rate
  * max_depth
  * n_estimators

---

## 🏆 Final Model

**XGBoost Classifier**

```python id="u7yqzp"
XGBClassifier(
    n_estimators=150,
    max_depth=3,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric='logloss',
    random_state=42
)
```

---

## 📊 Final Results

| Metric         | Score    |
| -------------- | -------- |
| Accuracy       | **0.85** |
| Macro F1 Score | **0.81** |

### Classification Report:

```id="3q0hvt"
Class 0 (Rejected): Precision = 0.88, Recall = 0.61, F1 = 0.72  
Class 1 (Approved): Precision = 0.85, Recall = 0.96, F1 = 0.90  
```
## 📊 Confusion Matrix

![Confusion Matrix](confusion_matrix.png)
---

## 📈 Key Insights

* Multiple models were tested including Logistic Regression, Random Forest, Gradient Boosting, and XGBoost
* XGBoost achieved the best overall performance with highest macro F1-score
* It minimized false negatives, which is critical in loan approval systems
* Tree-based models performed better after tuning
* Cross-validation ensured model stability and reliability

---

## ⚠️ Challenges

* Imbalanced dataset
* Small dataset size
* Initial model bias toward majority class

---

## 🚀 Future Improvements

* Apply SMOTE for further imbalance handling
* Feature engineering (income ratios, etc.)
* Model deployment using Flask/Streamlit
* Add explainability (SHAP values for XGBoost)

---

## 💡 Conclusion

After evaluating multiple models, XGBoost provided the best balance between accuracy and recall, making it the most suitable model for loan approval prediction.

---

## 🙌 Author

**Keerthi**
GitHub: https://github.com/allianceprokeerthi-cmd
