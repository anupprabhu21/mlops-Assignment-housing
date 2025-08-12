# mlopspipeline
# MLOPS Assignment1 on  Housing  dataset
python3 -m venv  
Source /Users/sampadahegde/Bits-sem3/mlopspipeline/.venv/bin/activate
# DVC
dvc init
dvc checkout
git add data/raw/housing.csv.dvc
git commit -m "Track DataSet with DVC" 
git ls-files | grep data/
git add .gitignore     
git commit -m "Add data folder to .gitignore for DVC"
python ./src/train.py
# mlflow
pip install mlflow joblib
mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root ./mlruns \
  --host 0.0.0.0 \
  --port 5000
# pip install fastapi uvicorn pydantic
uvicorn api.main:app --reload
docker build -t mlops-housing .
docker run -p 8000:8000 mlops-housing
pip install prometheus_client
chmod +x deploy.sh
flake8 src/
pytest tests/
docker build -t housing-model .
docker run --rm housing-model
# http://127.0.0.1:8000/metrics

prometheus --config.file=prometheus.yml  
grafana-v11.0.0 % ./bin/grafana-server




