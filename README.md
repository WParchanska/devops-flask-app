*DevOps Flask App*

Simple Flask application demonstrating a complete DevOps workflow using Docker, CI/CD, and cloud deployment.

*Tech Stack*
Python (Flask)
Docker
GitHub Actions (CI/CD)
Docker Hub
AWS EC2

*Features*
REST API built with Flask
Health check endpoint /health
Dockerized application
Automated CI/CD pipeline
Docker image pushed to Docker Hub
Ready for cloud deployment

*Example Response*
/health

{
  "status": "OK"
}

*Run with Docker*
docker run -d -p 5001:5001 wupe7/desvops-flask-app:latest

Test: 
curl http://127.0.0.1:5001/health

*Run with Docker Compose*
docker-compose up -d

*CI/CD Pipeline*
The project uses GitHub Actions to automate:
Installing dependencies
Running tests (pytest)
Testing /health endpoint
Building Docker image
Pushing image to Docker Hub
Pipeline runs on every push to main.

*Deployment (AWS EC2)*
Application was deployed on AWS EC2 instance:
Docker installed on EC2
Image pulled from Docker Hub
Container started and tested locally on server

*What I Learned*
Building and testing Flask applications
Writing CI/CD pipelines with GitHub Actions
Working with Docker images and containers
Managing secrets (GitHub + Docker Hub tokens)
Basic cloud deployment on AWS EC2

*Docker Hub*
docker pull wupe7/desvops-flask-app:latest

*Project Purpose*
This project was created as a hands-on DevOps practice project to demonstrate real-world workflow skills for junior DevOps roles.
