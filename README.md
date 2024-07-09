# End to end Text-Summarizer-Project

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Text-Summarization
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```
# AWS CI/CD Deployment with GitHub Actions

## Steps to Setup

### 1. Login to AWS Console
   - Access your AWS console using your credentials.

### 2. Create IAM User for Deployment
   - Create a new IAM user with the following specific access:
     1. EC2 access: Provides access to virtual machines.
     2. ECR access: Allows usage of Elastic Container Registry to save your Docker images in AWS.

## Description: About the Deployment

1. Build the Docker image of the source code.
2. Push the Docker image to ECR.
3. Launch an EC2 instance.
4. Pull the Docker image from ECR in the EC2 instance.
5. Launch the Docker image in the EC2 instance.

## Policies

1. Attach the following policies to your IAM user:
   - `AmazonEC2ContainerRegistryFullAccess`
   - `AmazonEC2FullAccess`

### Steps to Follow

1. **Create an ECR Repository**:
   - Create an ECR repository to store/save your Docker image.
   - Save the URI, e.g., `566373416292.dkr.ecr.us-east-1.amazonaws.com/text-s`.

2. **Create an EC2 Machine (Ubuntu)**:
   - Launch a new EC2 instance running Ubuntu.

3. **Open EC2 and Install Docker**:
   - **Optional**:
     ```sh
     sudo apt-get update -y
     sudo apt-get upgrade
     ```
   - **Required**:
     ```sh
     curl -fsSL https://get.docker.com -o get-docker.sh
     sudo sh get-docker.sh
     sudo usermod -aG docker ubuntu
     newgrp docker
     ```

4. **Configure EC2 as Self-Hosted Runner**:
   - Navigate to GitHub repository settings.
   - Go to `Actions` > `Runners` > `New self-hosted runner`.
   - Choose the operating system and follow the instructions to run the provided commands on your EC2 instance.

5. **Setup GitHub Secrets**:
   - Go to your GitHub repository.
   - Navigate to `Settings` > `Secrets` > `Actions` > `New repository secret`.
   - Add the following secrets:
     - `AWS_ACCESS_KEY_ID`
     - `AWS_SECRET_ACCESS_KEY`
     - `AWS_REGION` 
     - `AWS_ECR_LOGIN_URI`
     - `ECR_REPOSITORY_NAME`


