# 💧 Water Potability Prediction Project

![Water Potability Banner](https://user-images.githubusercontent.com/81433342/153164943-20551731-8664-4432-8438-23212b7f0f62.png)

This end-to-end data science project focuses on predicting whether water is potable (safe for human consumption) based on its physicochemical properties. The project handles a common challenge in real-world datasets: class imbalance, which is addressed using the SMOTE technique.

---

## 🚀 Live Demo

You can interact with the final trained model through the live Streamlit web application:

**[➡️ Click here to view the Streamlit App](https://water-purity-test-tajhaicajwq6dhcwrfjqou.streamlit.app/)**

---

## ## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset](#-dataset)
- [Project Workflow](#-project-workflow)
- [Model Performance](#-model-performance)
- [Installation](#-installation)
- [How to Run](#-how-to-run)
- [Technologies Used](#-technologies-used)

---

## ## 📝 Project Overview

The primary goal of this project is to build an efficient and reliable machine learning model to classify water quality. The dataset contains various chemical and physical metrics for different water samples. A key challenge was the imbalanced nature of the dataset, where one class significantly outnumbered the other. This was resolved by implementing the **Synthetic Minority Over-sampling Technique (SMOTE)** to create a balanced training set, leading to a more robust and unbiased model.

---

## ## 📊 Dataset

The dataset used is the **Water Potability Dataset**, which contains 9 features (e.g., pH, Hardness, Solids, Chloramines) and a target variable, `Potability`.

- **Source:** [Kaggle Water Potability Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)
- **Features:** 9 continuous variables.
- **Target:** `Potability` (1 for potable, 0 for not potable).
- **Challenge:** The dataset is imbalanced and contains missing values which were handled during preprocessing.

---

## ## ⚙️ Project Workflow

The project followed a standard end-to-end machine learning pipeline:

1.  **Data Ingestion & EDA:** Loaded the data and performed Exploratory Data Analysis to understand feature distributions and correlations.
2.  **Data Preprocessing:**
    - Handled missing values using an appropriate imputation strategy (e.g., median).
    - Split the data into training and testing sets.
3.  **Data Balancing (SMOTE):** Applied SMOTE **only on the training data** to create synthetic samples for the minority class.
4.  **Feature Scaling:** Scaled the numerical features using `StandardScaler` to bring them to a uniform scale.
5.  **Model Training:** Trained and evaluated several classification models to find the best performer.
6.  **Hyperparameter Tuning:** Optimized the best-performing model using `GridSearchCV` to enhance its predictive power.
7.  **Deployment:** Created a user-friendly web interface using **Streamlit** to allow for real-time predictions.

---
## ## 🛠️ Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ## 🏃 How to Run

Once the installation is complete, you can launch the Streamlit application:

```bash
streamlit run app.py
