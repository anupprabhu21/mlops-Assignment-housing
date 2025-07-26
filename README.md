 California Housing Price Prediction - End-to-End ML Pipeline

This repository contains an end-to-end machine learning workflow for predicting housing prices using the California Housing Dataset. The pipeline includes data preprocessing, model training, evaluation, version control with DVC, experiment tracking with MLflow, and deployment.

---

## 📂 Project Structure

.
├── data/ # Raw and processed datasets
│ └── raw/
├── notebooks/ # Jupyter notebooks for EDA & development
├── src/ # Source code (data loading, training, utils)
├── models/ # Trained models
├── dvc.yaml # DVC pipeline stages
├── dvc.lock # DVC lock file (auto generated)
├── .dvc/ # DVC config directory
├── mlruns/ # MLflow tracking directory
├── requirements.txt # Python dependencies
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2️⃣ Create & Activate a Virtual Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Install DVC & MLflow (if not already installed)
bash
Copy
Edit
pip install dvc mlflow
🚀 Running the Pipeline
➤ Pull the data from DVC (if not present)
bash
Copy
Edit
dvc pull
➤ Run the DVC pipeline
bash
Copy
Edit
dvc repro
🔬 Track Experiments with MLflow
Start MLflow UI:

bash
Copy
Edit
mlflow ui --port 5001
Then open http://127.0.0.1:5001 in your browser.

🧪 Sample Commands
Train and log experiment:

bash
Copy
Edit
python src/train.py
📦 Reproducibility & Versioning
DVC: For tracking data, models, and pipeline stages.

MLflow: For logging parameters, metrics, models.

Git: For version control of code and pipelines.

🧰 Tools & Libraries Used
Python 3.8+

scikit-learn

pandas, numpy, matplotlib

DVC

MLflow

Git

📜 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Name: Anup Prabhu
      SAMPADA BALGI
      MEGHA TIWARI

Email: anupprabhu1998@gmail.com
