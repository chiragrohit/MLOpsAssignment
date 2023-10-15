# MLOpsAssignment
Predict miles per gallon.
Dataset: [Auto-mpg dataset](https://www.kaggle.com/datasets/uciml/autompg-dataset/data)

# Docker Containerization
This project can be containerized using Docker to make it easily deployable.

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
