"""
Day 17: AI and Machine Learning with Python
===========================================

Today we'll learn about Artificial Intelligence and Machine Learning using Python.
We'll explore popular ML libraries, build models, and understand the fundamentals
of AI/ML development.

Learning Objectives:
- Understand AI and ML concepts
- Learn about popular Python ML libraries
- Build machine learning models
- Practice data preprocessing and feature engineering
- Explore deep learning basics
- Build real-world AI applications

Let's dive into AI and Machine Learning!
"""

print("🐍 Welcome to Day 17: AI and Machine Learning with Python!")
print("=" * 60)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. WHAT IS AI AND MACHINE LEARNING?
# =============================================================================

print("\n🤖 WHAT IS AI AND MACHINE LEARNING?")
print("-" * 40)

"""
Artificial Intelligence (AI) is:
- The simulation of human intelligence in machines
- Systems that can perform tasks requiring human intelligence
- Includes learning, reasoning, and self-correction

Machine Learning (ML) is:
- A subset of AI that focuses on algorithms
- Systems that learn from data without explicit programming
- Pattern recognition and prediction from data

Types of Machine Learning:
1. Supervised Learning: Learning with labeled data
2. Unsupervised Learning: Finding patterns in unlabeled data
3. Reinforcement Learning: Learning through interaction and rewards

Popular Python ML Libraries:
- scikit-learn: General ML algorithms
- pandas: Data manipulation
- numpy: Numerical computing
- matplotlib/seaborn: Data visualization
- tensorflow/pytorch: Deep learning
- opencv: Computer vision
"""

# =============================================================================
# 2. DATA PREPROCESSING
# =============================================================================

print("\n🔧 DATA PREPROCESSING")
print("-" * 25)

def demonstrate_data_preprocessing():
    """Demonstrate data preprocessing techniques."""
    # Create sample dataset
    np.random.seed(42)
    data = {
        'age': np.random.normal(35, 10, 1000),
        'income': np.random.normal(50000, 15000, 1000),
        'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 1000),
        'experience': np.random.normal(10, 5, 1000),
        'salary': np.random.normal(60000, 20000, 1000)
    }
    
    df = pd.DataFrame(data)
    
    # Add some missing values
    df.loc[np.random.choice(df.index, 50), 'income'] = np.nan
    df.loc[np.random.choice(df.index, 30), 'education'] = np.nan
    
    print("Original Dataset:")
    print(f"Shape: {df.shape}")
    print(f"Missing values:\n{df.isnull().sum()}")
    
    # Handle missing values
    df_cleaned = df.copy()
    df_cleaned['income'].fillna(df_cleaned['income'].mean(), inplace=True)
    df_cleaned['education'].fillna(df_cleaned['education'].mode()[0], inplace=True)
    
    print(f"\nAfter cleaning missing values:\n{df_cleaned.isnull().sum()}")
    
    # Feature encoding
    le = LabelEncoder()
    df_cleaned['education_encoded'] = le.fit_transform(df_cleaned['education'])
    
    print(f"\nEducation encoding:")
    print(f"Original: {df_cleaned['education'].unique()}")
    print(f"Encoded: {df_cleaned['education_encoded'].unique()}")
    
    # Feature scaling
    scaler = StandardScaler()
    numeric_features = ['age', 'income', 'experience', 'salary']
    df_cleaned[numeric_features] = scaler.fit_transform(df_cleaned[numeric_features])
    
    print(f"\nAfter scaling (first 5 rows):")
    print(df_cleaned[numeric_features].head())
    
    return df_cleaned

df_processed = demonstrate_data_preprocessing()

# =============================================================================
# 3. SUPERVISED LEARNING
# =============================================================================

print("\n📚 SUPERVISED LEARNING")
print("-" * 25)

def demonstrate_supervised_learning():
    """Demonstrate supervised learning algorithms."""
    # Create sample dataset for classification
    from sklearn.datasets import make_classification
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, classification_report
    
    # Generate classification dataset
    X, y = make_classification(n_samples=1000, n_features=4, n_redundant=0, 
                             n_informative=4, n_clusters_per_class=1, random_state=42)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Classification Dataset:")
    print(f"Training set: {X_train.shape}")
    print(f"Test set: {X_test.shape}")
    print(f"Classes: {np.unique(y)}")
    
    # Train different models
    models = {
        'Logistic Regression': LogisticRegression(random_state=42),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'SVM': SVC(random_state=42)
    }
    
    results = {}
    for name, model in models.items():
        # Train model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy
        
        print(f"\n{name}:")
        print(f"  Accuracy: {accuracy:.4f}")
        print(f"  Classification Report:")
        print(classification_report(y_test, y_pred))
    
    # Find best model
    best_model = max(results, key=results.get)
    print(f"\nBest performing model: {best_model} ({results[best_model]:.4f})")
    
    return results

classification_results = demonstrate_supervised_learning()

# =============================================================================
# 4. REGRESSION ANALYSIS
# =============================================================================

print("\n📈 REGRESSION ANALYSIS")
print("-" * 25)

def demonstrate_regression():
    """Demonstrate regression analysis."""
    # Create sample regression dataset
    from sklearn.datasets import make_regression
    from sklearn.linear_model import LinearRegression, Ridge, Lasso
    from sklearn.metrics import mean_squared_error, r2_score
    
    # Generate regression dataset
    X, y = make_regression(n_samples=1000, n_features=4, noise=0.1, random_state=42)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Regression Dataset:")
    print(f"Training set: {X_train.shape}")
    print(f"Test set: {X_test.shape}")
    
    # Train different regression models
    regression_models = {
        'Linear Regression': LinearRegression(),
        'Ridge Regression': Ridge(alpha=1.0),
        'Lasso Regression': Lasso(alpha=1.0)
    }
    
    regression_results = {}
    for name, model in regression_models.items():
        # Train model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate metrics
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        regression_results[name] = {'MSE': mse, 'R2': r2}
        
        print(f"\n{name}:")
        print(f"  MSE: {mse:.4f}")
        print(f"  R²: {r2:.4f}")
    
    # Find best model
    best_regression = min(regression_results, key=lambda x: regression_results[x]['MSE'])
    print(f"\nBest performing model: {best_regression}")
    
    return regression_results

regression_results = demonstrate_regression()

# =============================================================================
# 5. UNSUPERVISED LEARNING
# =============================================================================

print("\n🔍 UNSUPERVISED LEARNING")
print("-" * 30)

def demonstrate_unsupervised_learning():
    """Demonstrate unsupervised learning algorithms."""
    from sklearn.cluster import KMeans, DBSCAN
    from sklearn.decomposition import PCA
    from sklearn.datasets import make_blobs
    
    # Generate clustering dataset
    X, y_true = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)
    
    print("Clustering Dataset:")
    print(f"Shape: {X.shape}")
    print(f"True clusters: {len(np.unique(y_true))}")
    
    # K-Means Clustering
    kmeans = KMeans(n_clusters=4, random_state=42)
    kmeans_labels = kmeans.fit_predict(X)
    
    print(f"\nK-Means Clustering:")
    print(f"Cluster centers: {kmeans.cluster_centers_.shape}")
    print(f"Labels: {np.unique(kmeans_labels)}")
    
    # DBSCAN Clustering
    dbscan = DBSCAN(eps=0.5, min_samples=5)
    dbscan_labels = dbscan.fit_predict(X)
    
    print(f"\nDBSCAN Clustering:")
    print(f"Number of clusters: {len(set(dbscan_labels)) - (1 if -1 in dbscan_labels else 0)}")
    print(f"Number of noise points: {list(dbscan_labels).count(-1)}")
    
    # PCA for dimensionality reduction
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    
    print(f"\nPCA Dimensionality Reduction:")
    print(f"Original shape: {X.shape}")
    print(f"Reduced shape: {X_pca.shape}")
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    
    return kmeans_labels, dbscan_labels, X_pca

clustering_results = demonstrate_unsupervised_learning()

# =============================================================================
# 6. FEATURE ENGINEERING
# =============================================================================

print("\n⚙️ FEATURE ENGINEERING")
print("-" * 25)

def demonstrate_feature_engineering():
    """Demonstrate feature engineering techniques."""
    # Create sample dataset
    np.random.seed(42)
    data = {
        'age': np.random.normal(35, 10, 1000),
        'income': np.random.normal(50000, 15000, 1000),
        'education_years': np.random.normal(16, 4, 1000),
        'experience': np.random.normal(10, 5, 1000)
    }
    
    df = pd.DataFrame(data)
    
    print("Original Features:")
    print(df.head())
    
    # Feature creation
    df['age_group'] = pd.cut(df['age'], bins=[0, 25, 35, 50, 100], labels=['Young', 'Adult', 'Middle', 'Senior'])
    df['income_category'] = pd.cut(df['income'], bins=[0, 30000, 60000, 100000, float('inf')], 
                                  labels=['Low', 'Medium', 'High', 'Very High'])
    
    # Polynomial features
    df['age_squared'] = df['age'] ** 2
    df['income_log'] = np.log(df['income'] + 1)
    
    # Interaction features
    df['age_income_interaction'] = df['age'] * df['income']
    df['education_experience_ratio'] = df['education_years'] / (df['experience'] + 1)
    
    # Statistical features
    df['income_zscore'] = (df['income'] - df['income'].mean()) / df['income'].std()
    df['age_percentile'] = df['age'].rank(pct=True)
    
    print(f"\nAfter Feature Engineering:")
    print(f"New features: {df.columns.tolist()}")
    print(f"Dataset shape: {df.shape}")
    
    # Feature selection (correlation analysis)
    numeric_features = df.select_dtypes(include=[np.number]).columns
    correlation_matrix = df[numeric_features].corr()
    
    print(f"\nFeature Correlation Matrix:")
    print(correlation_matrix)
    
    return df

engineered_df = demonstrate_feature_engineering()

# =============================================================================
# 7. MODEL EVALUATION AND VALIDATION
# =============================================================================

print("\n📊 MODEL EVALUATION AND VALIDATION")
print("-" * 40)

def demonstrate_model_evaluation():
    """Demonstrate model evaluation techniques."""
    from sklearn.model_selection import cross_val_score, validation_curve
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification
    
    # Generate dataset
    X, y = make_classification(n_samples=1000, n_features=4, n_classes=2, random_state=42)
    
    # Create model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    
    print("Cross-Validation Results:")
    print(f"CV Scores: {cv_scores}")
    print(f"Mean CV Score: {cv_scores.mean():.4f}")
    print(f"Standard Deviation: {cv_scores.std():.4f}")
    
    # Validation curve
    param_range = [10, 50, 100, 200, 500]
    train_scores, test_scores = validation_curve(
        RandomForestClassifier(random_state=42), X, y, 
        param_name='n_estimators', param_range=param_range, cv=3
    )
    
    print(f"\nValidation Curve Results:")
    print(f"Parameter range: {param_range}")
    print(f"Train scores mean: {train_scores.mean(axis=1)}")
    print(f"Test scores mean: {test_scores.mean(axis=1)}")
    
    # Learning curve
    from sklearn.model_selection import learning_curve
    
    train_sizes, train_scores_lc, test_scores_lc = learning_curve(
        model, X, y, train_sizes=[0.1, 0.3, 0.5, 0.7, 0.9], cv=3
    )
    
    print(f"\nLearning Curve Results:")
    print(f"Train sizes: {train_sizes}")
    print(f"Train scores mean: {train_scores_lc.mean(axis=1)}")
    print(f"Test scores mean: {test_scores_lc.mean(axis=1)}")
    
    return cv_scores

evaluation_results = demonstrate_model_evaluation()

# =============================================================================
# 8. DEEP LEARNING BASICS
# =============================================================================

print("\n🧠 DEEP LEARNING BASICS")
print("-" * 25)

def demonstrate_deep_learning():
    """Demonstrate deep learning concepts."""
    print("Deep Learning Concepts:")
    
    # Neural Network Architecture
    print("\n1. Neural Network Architecture:")
    print("   - Input Layer: Receives data")
    print("   - Hidden Layers: Process information")
    print("   - Output Layer: Produces predictions")
    print("   - Weights and Biases: Learnable parameters")
    print("   - Activation Functions: Non-linear transformations")
    
    # Popular Deep Learning Libraries
    print("\n2. Popular Deep Learning Libraries:")
    print("   - TensorFlow: Google's open-source platform")
    print("   - PyTorch: Facebook's research platform")
    print("   - Keras: High-level neural network API")
    print("   - Scikit-learn: Traditional ML algorithms")
    
    # Deep Learning Applications
    print("\n3. Deep Learning Applications:")
    print("   - Computer Vision: Image classification, object detection")
    print("   - Natural Language Processing: Text analysis, translation")
    print("   - Speech Recognition: Voice commands, transcription")
    print("   - Recommendation Systems: Personalized content")
    print("   - Autonomous Vehicles: Self-driving cars")
    
    # Simple Neural Network Example (using scikit-learn)
    from sklearn.neural_network import MLPClassifier
    from sklearn.datasets import make_classification
    
    # Generate dataset
    X, y = make_classification(n_samples=1000, n_features=4, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create neural network
    mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    mlp.fit(X_train, y_train)
    
    # Evaluate
    accuracy = mlp.score(X_test, y_test)
    print(f"\n4. Simple Neural Network Results:")
    print(f"   Accuracy: {accuracy:.4f}")
    print(f"   Hidden layers: {mlp.hidden_layer_sizes}")
    print(f"   Iterations: {mlp.n_iter_}")
    
    return mlp

deep_learning_model = demonstrate_deep_learning()

# =============================================================================
# 9. PRACTICAL AI APPLICATIONS
# =============================================================================

print("\n💼 PRACTICAL AI APPLICATIONS")
print("-" * 35)

def demonstrate_ai_applications():
    """Demonstrate practical AI applications."""
    print("Practical AI Applications:")
    
    # 1. Sentiment Analysis
    print("\n1. Sentiment Analysis:")
    print("   - Analyze customer reviews")
    print("   - Social media monitoring")
    print("   - Brand reputation management")
    print("   - Market research insights")
    
    # 2. Recommendation Systems
    print("\n2. Recommendation Systems:")
    print("   - E-commerce product recommendations")
    print("   - Content recommendations (Netflix, YouTube)")
    print("   - Music and book recommendations")
    print("   - Friend suggestions on social media")
    
    # 3. Computer Vision
    print("\n3. Computer Vision:")
    print("   - Medical image analysis")
    print("   - Autonomous vehicle navigation")
    print("   - Security and surveillance")
    print("   - Quality control in manufacturing")
    
    # 4. Natural Language Processing
    print("\n4. Natural Language Processing:")
    print("   - Chatbots and virtual assistants")
    print("   - Language translation")
    print("   - Text summarization")
    print("   - Voice recognition and synthesis")
    
    # 5. Predictive Analytics
    print("\n5. Predictive Analytics:")
    print("   - Stock market prediction")
    print("   - Weather forecasting")
    print("   - Demand forecasting")
    print("   - Risk assessment")
    
    # 6. Fraud Detection
    print("\n6. Fraud Detection:")
    print("   - Credit card fraud detection")
    print("   - Insurance fraud prevention")
    print("   - Cybersecurity threat detection")
    print("   - Identity verification")

demonstrate_ai_applications()

# =============================================================================
# 10. AI ETHICS AND RESPONSIBLE AI
# =============================================================================

print("\n🤝 AI ETHICS AND RESPONSIBLE AI")
print("-" * 35)

def demonstrate_ai_ethics():
    """Demonstrate AI ethics and responsible AI practices."""
    print("AI Ethics and Responsible AI:")
    
    # 1. Bias and Fairness
    print("\n1. Bias and Fairness:")
    print("   - Algorithmic bias detection")
    print("   - Fairness in decision making")
    print("   - Diverse training data")
    print("   - Regular bias audits")
    
    # 2. Privacy and Security
    print("\n2. Privacy and Security:")
    print("   - Data privacy protection")
    print("   - Secure model deployment")
    print("   - Differential privacy")
    print("   - Secure multi-party computation")
    
    # 3. Transparency and Explainability
    print("\n3. Transparency and Explainability:")
    print("   - Model interpretability")
    print("   - Decision explanations")
    print("   - Open source algorithms")
    print("   - Clear documentation")
    
    # 4. Accountability
    print("\n4. Accountability:")
    print("   - Clear responsibility chains")
    print("   - Model monitoring")
    print("   - Error tracking")
    print("   - Regular model updates")
    
    # 5. Human-AI Collaboration
    print("\n5. Human-AI Collaboration:")
    print("   - Human-in-the-loop systems")
    print("   - AI-assisted decision making")
    print("   - Human oversight")
    print("   - Collaborative intelligence")

demonstrate_ai_ethics()

# =============================================================================
# 11. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice AI and ML concepts:

Exercise 1: Build a Customer Churn Prediction Model
- Load customer data
- Preprocess and engineer features
- Train classification models
- Evaluate model performance
- Deploy the model

Exercise 2: Create a Movie Recommendation System
- Use collaborative filtering
- Implement content-based filtering
- Build hybrid recommendation system
- Evaluate recommendation quality
- Create user interface

Exercise 3: Develop a Sentiment Analysis Tool
- Collect social media data
- Preprocess text data
- Train sentiment classification model
- Analyze sentiment trends
- Create visualization dashboard

Exercise 4: Build an Image Classification System
- Use computer vision libraries
- Implement image preprocessing
- Train CNN model
- Evaluate classification accuracy
- Deploy image recognition API

Exercise 5: Create a Stock Price Prediction Model
- Collect financial data
- Engineer technical indicators
- Train time series models
- Predict future prices
- Implement trading strategy
""")

# =============================================================================
# 12. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
AI/ML best practices:

1. Data Quality
   ✅ Clean and validate data
   ❌ Use dirty or incomplete data

2. Feature Engineering
   ✅ Create meaningful features
   ❌ Use raw data without processing

3. Model Selection
   ✅ Try multiple algorithms
   ❌ Stick to one algorithm

4. Cross-Validation
   ✅ Use proper validation techniques
   ❌ Test on training data

5. Hyperparameter Tuning
   ✅ Optimize model parameters
   ❌ Use default parameters only

6. Model Interpretability
   ✅ Understand model decisions
   ❌ Use black-box models blindly

7. Monitoring and Maintenance
   ✅ Monitor model performance
   ❌ Deploy and forget

8. Ethical Considerations
   ✅ Consider bias and fairness
   ❌ Ignore ethical implications
""")

# =============================================================================
# 13. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common AI/ML mistakes:

1. Data Leakage
   ❌ Using future data to predict past
   ✅ Proper temporal validation

2. Overfitting
   ❌ Model memorizes training data
   ✅ Use regularization and validation

3. Underfitting
   ❌ Model too simple for data
   ✅ Increase model complexity

4. Ignoring Data Distribution
   ❌ Assume training = test distribution
   ✅ Validate data distribution

5. Not Handling Imbalanced Data
   ❌ Ignore class imbalance
   ✅ Use appropriate sampling techniques

6. Poor Feature Selection
   ❌ Use all features without selection
   ✅ Select relevant features

7. Not Validating Assumptions
   ❌ Assume linear relationships
   ✅ Test model assumptions

8. Ignoring Business Context
   ❌ Focus only on technical metrics
   ✅ Consider business impact
""")

# =============================================================================
# 14. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ AI and ML fundamentals
✅ Data preprocessing and feature engineering
✅ Supervised and unsupervised learning
✅ Model evaluation and validation
✅ Deep learning basics
✅ Practical AI applications
✅ AI ethics and responsible AI
✅ Best practices for ML development

Next Steps:
- Explore specific ML domains (NLP, Computer Vision)
- Learn advanced deep learning techniques
- Practice with real-world datasets
- Build end-to-end ML pipelines
""")

# =============================================================================
# 15. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 17 of your Python journey!

You now understand:
- AI and Machine Learning fundamentals
- Popular Python ML libraries
- Data preprocessing and feature engineering
- Model training and evaluation
- Deep learning concepts
- Practical AI applications
- AI ethics and responsible development

AI and ML are powerful tools for solving complex problems!
Practice with the exercises to master these cutting-edge skills.

Happy coding! 🐍✨
""")

# =============================================================================
# 16. COMPLETE LEARNING JOURNEY SUMMARY
# =============================================================================

print("\n🎓 COMPLETE LEARNING JOURNEY SUMMARY")
print("-" * 40)

print("""
Congratulations! You've completed a comprehensive 17-day Python learning journey:

Days 1-5: Foundation
- Day 1: Python Basics
- Day 2: Operators & Conditionals
- Day 3: Loops & Iteration
- Day 4: Functions & Scope
- Day 5: Data Structures

Days 6-10: Intermediate
- Day 6: File Handling
- Day 7: Exception Handling
- Day 8: Object-Oriented Programming
- Day 9: Modules & Packages
- Day 10: Advanced Data Structures

Days 11-16: Advanced
- Day 11: Regular Expressions
- Day 12: Web Scraping & APIs
- Day 13: Data Analysis with Pandas
- Day 14: Web Development with Flask
- Day 15: Testing & Debugging
- Day 16: Deployment & Production

Day 17: AI/ML
- Day 17: AI and Machine Learning

You now have a complete foundation in Python programming and AI/ML!
Continue practicing and building projects to master these skills.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 17: AI and Machine Learning with Python Tutorial")
    print("Run this file to see all examples in action!")
