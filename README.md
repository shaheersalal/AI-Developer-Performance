# AI-Developer-Performance
AI Developer Performance counter Machine Learning Model
AI Developer Performance Analysis - README
📊 Project Overview
This Jupyter notebook analyzes a dataset containing performance metrics for 1000 AI developers. The dataset includes various behavioral and productivity metrics such as coding hours, lines of code, bugs found/fixed, AI usage, sleep patterns, stress levels, and other development-related factors.

📁 Dataset Information
File: AI_Developer_Performance_Extended_1000.csv
Records: 1000 entries
Features: 13 columns

Features Description:
Hours_Coding - Hours spent coding (int64)

Lines_of_Code - Number of lines written (int64)

Bugs_Found - Number of bugs identified (int64)

Bugs_Fixed - Number of bugs resolved (int64)

AI_Usage_Hours - Hours using AI tools (int64)

Sleep_Hours - Hours slept (float64)

Cognitive_Load - Cognitive load measurement (int64)

Task_Success_Rate - Success rate percentage (int64)

Coffee_Intake - Cups of coffee consumed (int64)

Stress_Level - Stress level measurement (int64)

Task_Duration_Hours - Duration of tasks (float64)

Commits - Number of code commits (int64)

Errors - Number of errors encountered (int64)

🛠️ Technical Stack
Python Libraries Used:
EDA & Data Manipulation:
pandas - Data manipulation and analysis

numpy - Numerical computations

seaborn & matplotlib - Data visualization

Preprocessing & Feature Engineering:
sklearn.model_selection.train_test_split - Data splitting

sklearn.preprocessing - Various scalers and transformers:

StandardScaler, MinMaxScaler, RobustScaler, MaxAbsScaler

KBinsDiscretizer

PowerTransformer, FunctionTransformer

OneHotEncoder, LabelEncoder, OrdinalEncoder

sklearn.impute - Missing value imputation:

SimpleImputer, IterativeImputer, KNNImputer

sklearn.compose.ColumnTransformer - Column transformations

sklearn.pipeline.Pipeline - ML pipeline creation

Modeling & Evaluation:
sklearn.linear_model - Linear and Logistic Regression

sklearn.metrics - Model evaluation metrics

joblib.dump - Model serialization

🔍 Key Analysis Steps
1. Data Loading & Initial Exploration
Loaded the CSV dataset with 1000 rows and 13 features

Displayed basic information and first few rows

Checked for null values (none found)

Checked for duplicates (none found)

2. Statistical Summary
Generated descriptive statistics (count, mean, std, min, quartiles, max)

Examined data distributions and ranges for all features

3. Data Quality Checks
No missing values detected

No duplicate records found

📈 Key Insights from Data Summary
Average Developer Profile:
Hours Coding: 5.84 hours/day

Lines of Code: 356 lines/day

Bugs Found/Fixed: ~10 found, ~7 fixed daily

AI Usage: ~3 hours/day

Sleep: 6.47 hours/night

Task Success Rate: ~57%

Coffee Intake: ~3 cups/day

Stress Level: ~66/100

Task Duration: ~8.7 hours

Commits: ~17 commits

Errors: ~5 errors

Data Ranges:
Coding hours: 1-11 hours

Lines of code: 26-993 lines

Stress levels: 30-100

Task duration: 0.5-27.5 hours

🚀 Next Steps (Implied from Imports)
Planned Analysis:
Data Preprocessing:

Feature scaling/normalization

Encoding categorical variables

Handling potential outliers

Feature selection/engineering

Model Development:

Train-test split

Linear/Logistic regression modeling

Performance evaluation (accuracy, ROC-AUC)

Learning curve analysis

Model Deployment:

Pipeline creation for reproducible workflows

Model serialization with joblib

💡 Potential Use Cases
Developer Productivity Analysis

Stress Management Optimization

AI Tool Usage Impact Assessment

Code Quality Prediction

Team Performance Optimization

📋 Requirements
To run this notebook, install the required packages:

bash
pip install pandas numpy seaborn matplotlib scikit-learn joblib
🔄 Project Structure
text
AI_Developer_Performance_Extended_1000.ipynb  # Main analysis notebook
AI_Developer_Performance_Extended_1000.csv   # Dataset
README.md                                    # This file
📊 Dataset Statistics Summary
Total Records: 1000

Features: 13 (11 integer, 2 float)

Memory Usage: ~101.7 KB

No missing values

No duplicates

🎯 Target Variables
The notebook imports regression and classification models, suggesting potential prediction tasks such as:

Task success rate prediction

Error rate prediction

Stress level modeling

Productivity optimization
