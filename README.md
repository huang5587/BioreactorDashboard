# Bioreactor Dashboard
This project pulls bioreactor metrics from a postgresql database and displays them as a cluster of graphs. There is also a feature to download the data as a CSV files. Both the front-end and back-end are coded with Python, and dependencies and deployment are handled with docker. The streamlit and matplot libraries are used for the front-end display and graphs. 

## Installation  
This project is deployed and maintained with docker. The official instructions explaining how to install Docker are below. The instructions vary depeneding on your operating system.
```
https://docs.docker.com/desktop/install/mac-install/)https://docs.docker.com/desktop/install/mac-install/
```

## Usage
To run the program run the following commands into your command line interface. You may need to run this command as an administrator using the sudo keyword. 

```
docker compose up
```


At this point the project should be accessible by navigating to http://localhost:8888/ on your web browser. It should look something like this.

![image](https://github.com/huang5587/BioreactorDashboard/assets/65338691/694c537f-e409-4292-88b9-989e20b62839)
## Motivations

This project was undertaken to gain experience with deploying and maintaining a project with Docker, and also exploring the python Streamlit library for full-stack web applicatons.
