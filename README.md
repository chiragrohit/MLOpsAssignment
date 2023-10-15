# MLOpsAssignment
MLOpsAssignment: Predicting Miles per Gallon with the Auto-mpg Dataset
Dataset: [Auto-mpg dataset](https://www.kaggle.com/datasets/uciml/autompg-dataset/data)

# Docker Containerization
To facilitate easy deployment, this project can be containerized using Docker.

1. Create a `Dockerfile` in project root.
2. Build the Docker image:
```bash
docker build -t project-name .
```
# Cloud Deployment
- Using Cloud Run by Google Cloud
- Create a new project in Cloud Run
- Initialize using gcloud cmd line interface
 - ```gcloud init```
 - ```gcloud run deploy [service name] --source .```
- Endpoint: https://mlopsassingmentsvc-chfxmr7jba-el.a.run.app/
# Automated Testing
- To ensure that the model functions as expected, automated testing has been set up. 
- The testing is defined in the .github/workflows/test.yml file.
