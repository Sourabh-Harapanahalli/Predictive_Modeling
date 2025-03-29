# Predictive Modeling - Student Financial Behavior Analysis

## 📌 Project Overview
This project aims to predict whether a student will overdraw a checking account based on their age, gender, and alcohol consumption habits. A **Decision Tree Classifier** is used to model and analyze the relationships between these factors and financial behaviors.

## 📂 Repository Structure
```
📁 Predictive_Modeling
│── 📝 studentbehaviors.py          # Python script implementing the decision tree model
│── 📝 StudentBehaviors.ipynb       # Jupyter Notebook for model development and evaluation
│── 📝 overdrawn.csv                # Dataset containing student information
│── 📝 README.md                    # Project documentation (this file)
```

## 🔍 Problem Statement
Students often face financial challenges, and this study investigates how **age, gender, and alcohol consumption habits** affect the likelihood of overdrawing their checking accounts. The **main objectives** are:

1. **Predictive Modeling**: Build a decision tree classifier to predict checking account overdrawing behavior.
2. **Risk Assessment**: Evaluate risk factors influencing student financial behaviors.
3. **Insights Generation**: Identify key factors contributing to financial mismanagement.

## 📊 Dataset
The dataset contains the following features:
- **Age**: The age of the student.
- **Gender**: Encoded as `0` for male and `1` for female.
- **DaysDrink**: Number of days the student consumed alcohol in the past 30 days.
- **Overdrawn**: Target variable indicating if the student overdrew their checking account (`1` for Yes, `0` for No).

## 👩‍💻 Model Development
The predictive model is built using the **Decision Tree Classifier** from `scikit-learn`. The steps involved:
1. **Data Preprocessing**
   - Convert `DaysDrink` into categorical values (Low, Medium, High consumption levels).
   - Handle missing values and ensure data compatibility for machine learning algorithms.
2. **Training the Model**
   - Split data into training and testing sets (70%-30% split).
   - Train a **Decision Tree Classifier** on the dataset.
3. **Evaluation Metrics**
   - Compute **Accuracy Score** to assess model performance.
   - Generate a **Confusion Matrix** to analyze prediction quality.

## 📊 Model Evaluation
The model performance is measured using:
- **Accuracy Score**: Measures the proportion of correctly classified instances.
- **Confusion Matrix**: Analyzes true positives, true negatives, false positives, and false negatives.

## 🤖 Predictions and Queries
The model is tested using different queries to check its robustness:
- **Query 1**: A 20-year-old male who drank alcohol for 10 days.
- **Query 2**: A 25-year-old female who drank alcohol for 5 days.
- **Query 3**: A 19-year-old male who drank alcohol for 20 days.
- **Query 4**: A 22-year-old female who drank alcohol for 15 days.
- **Query 5**: A 21-year-old male who drank alcohol for 20 days.

## 🔧 Installation & Usage
1. **Clone the Repository**
   ```sh
   git clone https://github.com/sourabh-harapanahalli/Predictive_Modeling.git
   cd Predictive_Modeling
   ```
2. **Install Dependencies**
   ```sh
   pip install pandas numpy scikit-learn graphviz
   ```
3. **Run the Script**
   ```sh
   python studentbehaviors.py
   ```
4. **Run the Jupyter Notebook** (for interactive analysis)
   ```sh
   jupyter notebook StudentBehaviors.ipynb
   ```

## 🔍 Key Findings
- The **decision tree classifier** performed well with an acceptable accuracy score.
- Alcohol consumption is a significant predictor of financial mismanagement.
- The model provides insights into financial behaviors and can assist in designing better financial awareness programs.

## 💡 Limitations
- The dataset is limited in scope and may not generalize well to a broader student population.
- The model does not consider other external financial factors that may influence overdrawn behaviors.
- The decision tree may overfit on a small dataset.

## 📈 Future Improvements
- Use additional features like **income level, spending habits, and credit score**.
- Implement **ensemble methods** (Random Forest, Gradient Boosting) to improve accuracy.
- Optimize hyperparameters using **GridSearchCV**.


## 📤 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
