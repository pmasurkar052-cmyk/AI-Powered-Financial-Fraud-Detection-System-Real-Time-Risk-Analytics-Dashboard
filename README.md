# AI-Powered-Financial-Fraud-Detection-System-Real-Time-Risk-Analytics-Dashboard
  An end-to-end Machine Learning and Business Intelligence solution designed to detect fraudulent credit card transactions, mitigate financial risk, and deliver        actionable operational insights through an interactive Power BI dashboard.

1. Project Overview
   Credit card fraud is a major concern for financial institutions, typically characterized by extreme data imbalance (legitimate transactions vastly outnumber          fraudulent ones). This project bridges the gap between predictive modeling and business intelligence by combining a Python-based machine learning classification      pipeline with a fully interactive Power BI dashboard for risk tracking.

2. Business Problem & Objective
     ** The Challenge: Detecting rare fraudulent activities hidden within thousands of high-dimensional transactions without causing high false-positive rates for            customers.

     ** The Solution: Develop a risk-scoring framework that categorizes transactions into Low, Medium, and High risk tiers, empowering fraud-prevention teams to              prioritize alerts efficiently.

  3. Dataset Description 
     Sample Size: 10,000 credit card transaction records.

     Features:
 
     Time & Amount: Transaction timestamp and monetary value.

     V1 to V28: Principal Component Analysis (PCA) transformed numerical features to secure user confidentiality.

     Class: Target variable (0 for Legitimate, 1 for Fraudulent).

     Engineered Features: Fraud_Probability, Predicted_Class, and categorical Risk_Level tiers.


4. Tech Stack & Libraries
   Programming Language: Python

   Machine Learning & Data Preprocessing: scikit-learn (Random Forest Classifier, StandardScaler), pandas, numpy

   Business Intelligence: Power BI Desktop (KPI Cards, Scatter Plots, Timeline Line Charts, Matrix Visuals)

   Version Control: Git & GitHub


  5. Machine Learning Pipeline & Methodology
     Data Preprocessing & Scaling: Standardized the Amount and Time features using StandardScaler to ensure uniform feature scaling for the model.

     Model Training: Implemented a classification algorithm (Random Forest) trained to output continuous fraud probabilities.

     Risk Scoring Engine: Mapped probability thresholds into categorical operational risk tiers:

     Low Risk: Routine transactions with minimal probability.

     Medium Risk: Borderline transactions requiring secondary review.

     High Risk: High anomaly probability triggering immediate alerts.

     Data Export: Generated a clean prediction dataset (creditcard_predictions.csv) ready for BI integration.

     6. Power BI Dashboard Architecture & Visuals
        The dashboard is meticulously structured for risk analysts, featuring clean typography, consistent borders, and organized visual hierarchies:

        Executive KPI Cards: Real-time tracking of Total Transactions (10.00K), Total Fraud Detections (17), High Risk Alerts (14), and Max Risk Score (0.96).

        Fraud Probability Timeline & Risk Trends: Tracks transaction behavior across scaled time parameters.

        Feature Outlier Analysis (V10 vs V20): Scatter plot mapping PCA variables against risk tiers to isolate anomaly clusters.

        Risk Level Summary Matrix: Detailed tabular aggregation of financial metrics across risk tiers.


     7. Key Insights & Findings
        High-risk transactions are heavily concentrated around specific clusters in PCA feature spaces (V10 vs V20), validating the effectiveness of                       dimensionality reduction.

        Less than 0.2% of total volume triggered high-risk alerts, ensuring that fraud teams avoid alert fatigue while maintaining high security coverage.
