"""
Day 21: Jupyter Notebooks and Development Environment
====================================================

Today we'll learn about Jupyter Notebooks and setting up a proper Python
development environment. We'll explore virtual environments, package management,
and best practices for AI/ML development.

Learning Objectives:
- Understand Jupyter Notebooks and their advantages
- Learn to set up virtual environments (venv, conda)
- Master package management and dependencies
- Explore development tools and IDEs
- Practice collaborative development workflows
- Build reproducible AI/ML environments

Let's set up the perfect development environment!
"""

print("🐍 Welcome to Day 21: Jupyter Notebooks and Development Environment!")
print("=" * 70)

import os
import sys
import subprocess
import json
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# 1. WHAT IS JUPYTER NOTEBOOKS?
# =============================================================================

print("\n📓 WHAT IS JUPYTER NOTEBOOKS?")
print("-" * 35)

"""
Jupyter Notebooks are:
- Interactive computing environments
- Combine code, text, and visualizations
- Perfect for data science and AI/ML
- Support multiple programming languages
- Enable reproducible research

Key Features:
- Interactive code execution
- Rich text with Markdown
- Data visualization integration
- Export to various formats
- Collaborative development
- Version control integration

Advantages for AI/ML:
- Exploratory data analysis
- Prototyping and experimentation
- Documentation and storytelling
- Educational content
- Research reproducibility
"""

# =============================================================================
# 2. VIRTUAL ENVIRONMENTS
# =============================================================================

print("\n🔧 VIRTUAL ENVIRONMENTS")
print("-" * 25)

def demonstrate_virtual_environments():
    """Demonstrate virtual environment setup and management."""
    print("Virtual Environment Setup:")
    
    # 1. Python venv (built-in)
    print("\n1. Python venv (Built-in):")
    print("Creating virtual environment:")
    print("python -m venv myenv")
    print("myenv\\Scripts\\activate  # Windows")
    print("source myenv/bin/activate  # Linux/Mac")
    print("deactivate  # Deactivate")
    
    # 2. Conda environments
    print("\n2. Conda Environments:")
    print("Creating conda environment:")
    print("conda create -n myenv python=3.11")
    print("conda activate myenv")
    print("conda deactivate")
    
    # 3. Environment management
    print("\n3. Environment Management:")
    print("List environments:")
    print("conda env list")
    print("pip list")
    
    # 4. Requirements management
    print("\n4. Requirements Management:")
    requirements_content = """# Core dependencies
numpy>=1.21.0
pandas>=1.3.0
matplotlib>=3.4.0
seaborn>=0.11.0

# AI/ML libraries
scikit-learn>=1.0.0
tensorflow>=2.8.0
torch>=1.11.0
transformers>=4.15.0

# Jupyter and development
jupyter>=1.0.0
jupyterlab>=3.0.0
ipykernel>=6.0.0

# Data processing
openpyxl>=3.0.0
requests>=2.25.0
beautifulsoup4>=4.9.0

# Visualization
plotly>=5.0.0
bokeh>=2.4.0

# Development tools
pytest>=6.0.0
black>=21.0.0
flake8>=4.0.0
"""
    
    print("requirements.txt content:")
    print(requirements_content)
    
    # 5. Environment activation
    print("\n5. Environment Activation:")
    print("Windows:")
    print("  myenv\\Scripts\\activate")
    print("Linux/Mac:")
    print("  source myenv/bin/activate")
    print("Conda:")
    print("  conda activate myenv")
    
    # 6. Package installation
    print("\n6. Package Installation:")
    print("Install from requirements:")
    print("pip install -r requirements.txt")
    print("Install specific packages:")
    print("pip install numpy pandas matplotlib")
    print("Install development packages:")
    print("pip install -r requirements-dev.txt")

demonstrate_virtual_environments()

# =============================================================================
# 3. JUPYTER NOTEBOOK BASICS
# =============================================================================

print("\n📓 JUPYTER NOTEBOOK BASICS")
print("-" * 30)

def demonstrate_jupyter_basics():
    """Demonstrate Jupyter Notebook basics."""
    print("Jupyter Notebook Basics:")
    
    # 1. Starting Jupyter
    print("\n1. Starting Jupyter:")
    print("Start Jupyter Notebook:")
    print("jupyter notebook")
    print("Start JupyterLab:")
    print("jupyter lab")
    print("Start with specific port:")
    print("jupyter notebook --port=8888")
    
    # 2. Notebook structure
    print("\n2. Notebook Structure:")
    print("Cells can contain:")
    print("- Code (Python, R, Julia, etc.)")
    print("- Markdown text")
    print("- Raw text")
    print("- HTML")
    
    # 3. Cell execution
    print("\n3. Cell Execution:")
    print("Execute cell: Shift + Enter")
    print("Execute and add new cell: Alt + Enter")
    print("Execute all cells: Cell -> Run All")
    print("Restart kernel: Kernel -> Restart")
    
    # 4. Magic commands
    print("\n4. Magic Commands:")
    print("Line magics (start with %):")
    print("%timeit - Time execution")
    print("%matplotlib inline - Inline plots")
    print("%load - Load from file")
    print("%run - Run Python file")
    
    print("Cell magics (start with %%):")
    print("%%time - Time cell execution")
    print("%%bash - Run bash commands")
    print("%%html - HTML output")
    print("%%latex - LaTeX output")
    
    # 5. Keyboard shortcuts
    print("\n5. Keyboard Shortcuts:")
    print("Edit mode (Enter):")
    print("- Tab: Code completion")
    print("- Shift + Tab: Help")
    print("- Ctrl + /: Comment/uncomment")
    
    print("Command mode (Esc):")
    print("- A: Insert cell above")
    print("- B: Insert cell below")
    print("- DD: Delete cell")
    print("- M: Convert to Markdown")
    print("- Y: Convert to Code")
    print("- Z: Undo cell deletion")

demonstrate_jupyter_basics()

# =============================================================================
# 4. JUPYTER FOR AI/ML DEVELOPMENT
# =============================================================================

print("\n🤖 JUPYTER FOR AI/ML DEVELOPMENT")
print("-" * 35)

def demonstrate_jupyter_ai_ml():
    """Demonstrate Jupyter for AI/ML development."""
    print("Jupyter for AI/ML Development:")
    
    # 1. Data exploration workflow
    print("\n1. Data Exploration Workflow:")
    print("Step 1: Load and inspect data")
    print("import pandas as pd")
    print("df = pd.read_csv('data.csv')")
    print("df.head()")
    print("df.info()")
    print("df.describe()")
    
    print("\nStep 2: Visualize data")
    print("import matplotlib.pyplot as plt")
    print("import seaborn as sns")
    print("plt.figure(figsize=(10, 6))")
    print("sns.histplot(df['target'])")
    print("plt.show()")
    
    print("\nStep 3: Feature engineering")
    print("df['new_feature'] = df['col1'] * df['col2']")
    print("df['categorical'] = pd.Categorical(df['category'])")
    
    # 2. Model development workflow
    print("\n2. Model Development Workflow:")
    print("Step 1: Prepare data")
    print("from sklearn.model_selection import train_test_split")
    print("X_train, X_test, y_train, y_test = train_test_split(X, y)")
    
    print("\nStep 2: Train model")
    print("from sklearn.ensemble import RandomForestClassifier")
    print("model = RandomForestClassifier()")
    print("model.fit(X_train, y_train)")
    
    print("\nStep 3: Evaluate model")
    print("from sklearn.metrics import accuracy_score")
    print("predictions = model.predict(X_test)")
    print("accuracy = accuracy_score(y_test, predictions)")
    print("print(f'Accuracy: {accuracy:.4f}')")
    
    # 3. Visualization and analysis
    print("\n3. Visualization and Analysis:")
    print("Confusion matrix:")
    print("from sklearn.metrics import confusion_matrix")
    print("import seaborn as sns")
    print("cm = confusion_matrix(y_test, predictions)")
    print("sns.heatmap(cm, annot=True)")
    print("plt.show()")
    
    print("\nFeature importance:")
    print("feature_importance = pd.DataFrame({")
    print("    'feature': X.columns,")
    print("    'importance': model.feature_importances_")
    print("}).sort_values('importance', ascending=False)")
    print("sns.barplot(data=feature_importance, x='importance', y='feature')")
    
    # 4. Interactive widgets
    print("\n4. Interactive Widgets:")
    print("from ipywidgets import interact, widgets")
    print("@interact")
    print("def plot_data(column=widgets.Dropdown(options=df.columns)):")
    print("    plt.figure(figsize=(10, 6))")
    print("    plt.hist(df[column])")
    print("    plt.title(f'Distribution of {column}')")
    print("    plt.show()")
    
    # 5. Progress tracking
    print("\n5. Progress Tracking:")
    print("from tqdm import tqdm")
    print("import time")
    print("for i in tqdm(range(100)):")
    print("    time.sleep(0.01)  # Simulate work")
    
    # 6. Memory management
    print("\n6. Memory Management:")
    print("import psutil")
    print("import gc")
    print("print(f'Memory usage: {psutil.virtual_memory().percent}%')")
    print("del large_dataframe")
    print("gc.collect()")

demonstrate_jupyter_ai_ml()

# =============================================================================
# 5. DEVELOPMENT TOOLS AND IDES
# =============================================================================

print("\n🛠️ DEVELOPMENT TOOLS AND IDES")
print("-" * 35)

def demonstrate_development_tools():
    """Demonstrate development tools and IDEs."""
    print("Development Tools and IDEs:")
    
    # 1. VS Code with Python
    print("\n1. VS Code with Python:")
    print("Extensions to install:")
    print("- Python")
    print("- Jupyter")
    print("- Python Docstring Generator")
    print("- autoDocstring")
    print("- Python Indent")
    print("- Python Type Hint")
    
    print("\nVS Code settings for Python:")
    vs_code_settings = {
        "python.defaultInterpreterPath": "./venv/Scripts/python.exe",
        "python.linting.enabled": True,
        "python.linting.pylintEnabled": True,
        "python.formatting.provider": "black",
        "python.testing.pytestEnabled": True,
        "jupyter.askForKernelRestart": False
    }
    print(json.dumps(vs_code_settings, indent=2))
    
    # 2. PyCharm
    print("\n2. PyCharm:")
    print("Features:")
    print("- Intelligent code completion")
    print("- Debugging and profiling")
    print("- Version control integration")
    print("- Database tools")
    print("- Scientific tools")
    print("- Web development")
    
    # 3. JupyterLab
    print("\n3. JupyterLab:")
    print("Features:")
    print("- File browser")
    print("- Text editor")
    print("- Terminal")
    print("- Launcher")
    print("- Extensions")
    print("- Multi-tab interface")
    
    # 4. Google Colab
    print("\n4. Google Colab:")
    print("Features:")
    print("- Free GPU/TPU access")
    print("- Pre-installed libraries")
    print("- Google Drive integration")
    print("- Collaborative editing")
    print("- Version control")
    print("- Export to GitHub")
    
    # 5. Development workflow
    print("\n5. Development Workflow:")
    print("1. Set up virtual environment")
    print("2. Install dependencies")
    print("3. Create project structure")
    print("4. Initialize Git repository")
    print("5. Configure IDE/editor")
    print("6. Start development")
    print("7. Test and debug")
    print("8. Deploy")

demonstrate_development_tools()

# =============================================================================
# 6. PROJECT STRUCTURE AND ORGANIZATION
# =============================================================================

print("\n📁 PROJECT STRUCTURE AND ORGANIZATION")
print("-" * 45)

def demonstrate_project_structure():
    """Demonstrate project structure and organization."""
    print("Project Structure and Organization:")
    
    # 1. AI/ML project structure
    print("\n1. AI/ML Project Structure:")
    project_structure = """
my_ai_project/
├── data/                   # Data files
│   ├── raw/               # Raw data
│   ├── processed/         # Processed data
│   └── external/          # External data
├── notebooks/             # Jupyter notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_model_evaluation.ipynb
├── src/                   # Source code
│   ├── __init__.py
│   ├── data/              # Data processing
│   ├── features/          # Feature engineering
│   ├── models/            # Model definitions
│   └── visualization/     # Plotting functions
├── tests/                 # Test files
├── models/                # Trained models
├── reports/               # Generated reports
├── requirements.txt       # Dependencies
├── environment.yml        # Conda environment
├── README.md             # Project documentation
├── .gitignore            # Git ignore file
└── setup.py              # Package setup
"""
    print(project_structure)
    
    # 2. Configuration files
    print("\n2. Configuration Files:")
    
    # .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Environment
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Data
data/raw/
data/processed/
*.csv
*.json
*.parquet

# Models
models/*.pkl
models/*.joblib
models/*.h5
models/*.pth

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
"""
    print(".gitignore content:")
    print(gitignore_content)
    
    # 3. Environment files
    print("\n3. Environment Files:")
    
    # environment.yml
    environment_yml = """name: ai_project
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn
  - jupyter
  - jupyterlab
  - ipykernel
  - pip
  - pip:
    - tensorflow
    - torch
    - transformers
"""
    print("environment.yml:")
    print(environment_yml)
    
    # 4. Setup.py
    setup_py_content = """from setuptools import setup, find_packages

setup(
    name="ai_project",
    version="0.1.0",
    description="AI/ML project",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
        "jupyter>=1.0.0",
    ],
    python_requires=">=3.8",
)
"""
    print("setup.py:")
    print(setup_py_content)

demonstrate_project_structure()

# =============================================================================
# 7. COLLABORATIVE DEVELOPMENT
# =============================================================================

print("\n👥 COLLABORATIVE DEVELOPMENT")
print("-" * 30)

def demonstrate_collaborative_development():
    """Demonstrate collaborative development workflows."""
    print("Collaborative Development:")
    
    # 1. Version control with Git
    print("\n1. Version Control with Git:")
    print("Initialize repository:")
    print("git init")
    print("git add .")
    print("git commit -m 'Initial commit'")
    print("git remote add origin <repository-url>")
    print("git push -u origin main")
    
    print("\nBranching strategy:")
    print("git checkout -b feature/new-model")
    print("git add .")
    print("git commit -m 'Add new model'")
    print("git push origin feature/new-model")
    print("git checkout main")
    print("git merge feature/new-model")
    
    # 2. Code review process
    print("\n2. Code Review Process:")
    print("1. Create feature branch")
    print("2. Make changes")
    print("3. Test changes")
    print("4. Commit changes")
    print("5. Push to remote")
    print("6. Create pull request")
    print("7. Review and discuss")
    print("8. Merge to main")
    
    # 3. Documentation
    print("\n3. Documentation:")
    print("README.md should include:")
    print("- Project description")
    print("- Installation instructions")
    print("- Usage examples")
    print("- API documentation")
    print("- Contributing guidelines")
    print("- License information")
    
    # 4. Testing
    print("\n4. Testing:")
    print("Unit tests:")
    print("def test_model_prediction():")
    print("    model = load_model()")
    print("    prediction = model.predict(test_data)")
    print("    assert prediction.shape == expected_shape")
    
    print("\nIntegration tests:")
    print("def test_training_pipeline():")
    print("    data = load_data()")
    print("    model = train_model(data)")
    print("    assert model.score > 0.8")
    
    # 5. Continuous Integration
    print("\n5. Continuous Integration:")
    print("GitHub Actions workflow:")
    ci_workflow = """name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.11
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest
    - name: Run linting
      run: flake8 src/
"""
    print(ci_workflow)

demonstrate_collaborative_development()

# =============================================================================
# 8. DEPLOYMENT AND PRODUCTION
# =============================================================================

print("\n🚀 DEPLOYMENT AND PRODUCTION")
print("-" * 30)

def demonstrate_deployment():
    """Demonstrate deployment and production considerations."""
    print("Deployment and Production:")
    
    # 1. Model serialization
    print("\n1. Model Serialization:")
    print("Save model:")
    print("import joblib")
    print("joblib.dump(model, 'model.pkl')")
    print("Load model:")
    print("model = joblib.load('model.pkl')")
    
    print("\nTensorFlow/Keras:")
    print("model.save('model.h5')")
    print("model = tf.keras.models.load_model('model.h5')")
    
    # 2. API development
    print("\n2. API Development:")
    print("Flask API example:")
    flask_api = """from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
"""
    print(flask_api)
    
    # 3. Containerization
    print("\n3. Containerization:")
    print("Dockerfile for AI/ML:")
    dockerfile_content = """FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
"""
    print(dockerfile_content)
    
    # 4. Cloud deployment
    print("\n4. Cloud Deployment:")
    print("AWS SageMaker:")
    print("- Managed Jupyter notebooks")
    print("- Built-in algorithms")
    print("- Model hosting")
    print("- Auto-scaling")
    
    print("\nGoogle Colab:")
    print("- Free GPU access")
    print("- Pre-installed libraries")
    print("- Easy sharing")
    print("- Version control")
    
    print("\nAzure ML:")
    print("- MLOps capabilities")
    print("- Model registry")
    print("- Automated ML")
    print("- Pipeline orchestration")

demonstrate_deployment()

# =============================================================================
# 9. EXERCISES
# =============================================================================

print("\n🏋️ EXERCISES")
print("-" * 15)

print("""
Try these exercises to practice Jupyter and development environment:

Exercise 1: Set Up AI/ML Development Environment
- Create virtual environment
- Install required packages
- Set up Jupyter Notebook
- Configure VS Code
- Create project structure

Exercise 2: Build Data Science Pipeline
- Load and explore dataset
- Perform data cleaning
- Create visualizations
- Build machine learning model
- Document findings

Exercise 3: Create Interactive Dashboard
- Use Jupyter widgets
- Create interactive plots
- Build data exploration tools
- Add real-time updates
- Deploy as web app

Exercise 4: Collaborative AI Project
- Set up Git repository
- Create development workflow
- Implement code review process
- Add automated testing
- Deploy to production

Exercise 5: MLOps Pipeline
- Version control models
- Implement CI/CD
- Monitor model performance
- Automate retraining
- Scale deployment
""")

# =============================================================================
# 10. BEST PRACTICES
# =============================================================================

print("\n💡 BEST PRACTICES")
print("-" * 18)

print("""
Jupyter and Development Environment Best Practices:

1. Environment Management
   ✅ Use virtual environments
   ❌ Install packages globally

2. Notebook Organization
   ✅ One notebook per analysis
   ❌ Everything in one notebook

3. Code Quality
   ✅ Write clean, documented code
   ❌ Ignore code quality

4. Version Control
   ✅ Use Git for all projects
   ❌ Skip version control

5. Testing
   ✅ Test your code
   ❌ Deploy without testing

6. Documentation
   ✅ Document your work
   ❌ Write code without comments

7. Collaboration
   ✅ Use collaborative tools
   ❌ Work in isolation

8. Security
   ✅ Secure sensitive data
   ❌ Expose credentials
""")

# =============================================================================
# 11. COMMON MISTAKES TO AVOID
# =============================================================================

print("\n⚠️ COMMON MISTAKES TO AVOID")
print("-" * 30)

print("""
Common Jupyter and development mistakes:

1. Not using virtual environments
   ❌ Installing packages globally
   ✅ Use venv or conda

2. Poor notebook organization
   ❌ One giant notebook
   ✅ Separate notebooks by purpose

3. Not cleaning up outputs
   ❌ Committing notebooks with outputs
   ✅ Clear outputs before committing

4. Ignoring code quality
   ❌ No linting or formatting
   ✅ Use black, flake8, pylint

5. Not using version control
   ❌ No Git repository
   ✅ Initialize Git from start

6. Hardcoding paths
   ❌ Absolute paths in code
   ✅ Use relative paths or config

7. Not testing code
   ❌ Deploy without testing
   ✅ Write and run tests

8. Poor documentation
   ❌ No README or comments
   ✅ Document everything
""")

# =============================================================================
# 12. KEY TAKEAWAYS
# =============================================================================

print("\n🎯 KEY TAKEAWAYS")
print("-" * 16)

print("""
What you've learned today:

✅ Jupyter Notebooks fundamentals
✅ Virtual environment setup
✅ Development tools and IDEs
✅ Project structure and organization
✅ Collaborative development workflows
✅ Deployment and production considerations
✅ Best practices for AI/ML development
✅ Common mistakes to avoid

Next Steps:
- Set up your development environment
- Practice with Jupyter Notebooks
- Build AI/ML projects
- Learn advanced development tools
""")

# =============================================================================
# 13. CONCLUSION
# =============================================================================

print("\n🎉 CONGRATULATIONS!")
print("-" * 20)

print("""
You've completed Day 21 of your Python journey!

You now understand:
- How to set up Jupyter Notebooks
- Virtual environment management
- Development tools and workflows
- Project organization and structure
- Collaborative development practices
- Deployment and production considerations

A proper development environment is essential for AI/ML success!
Practice with the exercises to master these crucial skills.

Happy coding! 🐍✨
""")

# =============================================================================
# 14. COMPLETE LEARNING JOURNEY SUMMARY
# =============================================================================

print("\n🎓 COMPLETE LEARNING JOURNEY SUMMARY")
print("-" * 40)

print("""
Congratulations! You've completed a comprehensive 21-day Python learning journey:

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

Days 17-21: AI/ML & Development
- Day 17: AI and Machine Learning
- Day 18: AI Integration with Python
- Day 19: SQL Database Operations
- Day 20: NumPy Fundamentals
- Day 21: Jupyter Notebooks and Development Environment

You now have a complete foundation in Python programming, AI/ML, and development!
Continue practicing and building projects to master these skills.

Happy coding! 🐍✨
""")

# Run the tutorial
if __name__ == "__main__":
    print("Day 21: Jupyter Notebooks and Development Environment Tutorial")
    print("Run this file to see all examples in action!")
