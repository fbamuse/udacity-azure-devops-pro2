# Overview

This project is demonstration the Continuous Integration and Continuous Delivery with Github Action and Azure devops.
Continuous Integration. this repository three branch step1,step2 and step3.

- branch: step1  
  Github Action with C/I

- branch: step2  
  Azure build app and push AppService

- branch: step3  
  Build image and push DockerHub, then AppService pull image from DockerHub
   



## Project Plan

* Trello board for the project
  ![](2021-02-14-23-01-24.png)
* A link to a spreadsheet that includes the original and final project plan>
  https://docs.google.com/spreadsheets/d/1xIKzw1vmUmW_91NAxOSHVHGcylxuuXhUJ8YQ1ca1Rls/edit#gid=1348135932




## Instructions
### Architectural Diagram
  
1. Github Action with continuous Integration 
- branch: step1  
![](2021-02-14-17-58-31.png)

2. Github integrate with Azure devops pipeline  
- branch: step2  
  Azure build application and push AppService 
![](2021-02-14-17-58-01.png)

- branch: step3  
  Build image and push DockerHub, then AppService pull  image from DockerHub
![](2021-02-14-17-57-30.png)

 

### step
1. Github Action with continuus Integragion 

	Cloned project files into Azure Cloud Shell  
	we can get starter file from repo (https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code.git)
	![](2021-02-14-21-32-10.png)

	Check Makefile works fine at Azure Cloud Shell.
	![](2021-02-14-21-22-36.png)

	Build Continuas integration pipeline using Github Action.
	and work fine.
	![](2021-02-14-21-27-26.png)

   ![Python application test with Github Actions](https://github.com/fbamuse/udacity-azure-devops-pro2/workflows/Python%20application%20test%20with%20Github%20Actions/badge.svg?branch=step1)

2. Github integrate with Azure devops pipeline  

- branch: step2   
  Azure build application and push AppService  


   start Appservice plan and AppService 
   run commnad.sh which incloud following az command
  
   >> az group create -l japaneast -n  udagroup  
   >>az appservice plan create -g udagroup -n my-service-plan --is-linux --sku B1    
   >>az webapp create -g udagroup -p my-service-plan -n my-appservice --runtime "Python|3.7"  

	You can find following page (https://my-appservice.azurewebsites.ne)
	![](2021-02-14-19-07-35.png)


	After git repository registered devpos pipeline start  
	AzureDevops(https://dev.azure.com/)

	![](2021-02-14-19-10-58.png)

	after while pipeline finished
	![](2021-02-14-19-14-57.png)

	ML AppService is started 
	![](2021-02-14-19-16-14.png)



	Scoreing predict  
	run "make_predict_azure_app.sh"

	![](2021-02-14-19-17-58.png)


	Load test  
	define test senario in locustfile.py
![](2021-02-14-22-08-15.png)


	start locust
	```bash
	python3 -m venv ~/venv
	source ~/venv/bin/activate
	pip install locust==1.4.3
	locust -H https://my-appservice.azurewebsites.net
	```

	acsess to  http://localhost:8089   
	define Number of users to simulate and Hatch rate
	![](2021-02-14-12-57-46.png)


- branch: step3  
  Build image and push DockerHub, then AppService pull  image from DockerHub

	Set up to pull the latest image from DouckerHub in the Deployment Center settings of AppService.
	![](2021-02-14-22-47-27.png)

	Triggered by registering on GitHub, the Azure Devops pipeline builds a Docker image and pushes it to Docker Hub.
	![](2021-02-14-22-50-41.png)
	Appservice pulls the image from Docker Hub.
	![](2021-02-14-22-45-50.png)
	Application is ready  
	![](2021-02-14-22-48-34.png)
	Predict  
	![](2021-02-14-22-52-04.png)















   


## Enhancements


- Upgrade to autoscale and Kubernetes linked to access load

- Creating a UI that looks good and is easy to use
- Working with the MLOps pipeline of machine learning models


## Demo 

<TODO: Add link Screencast on YouTube>


