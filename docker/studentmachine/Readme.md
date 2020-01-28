# Student Working Environment Container

**Container name**: studentmachine

This docker image provides the working environment for students.
It contains Ansible, so they can execute all Ansible lessons from this container.

It is based on Ubuntu 18.04 with the following additional software packages installed:
  * OpenSSH client
  * Ansible
  * locales
  * vim, nano, cat, less, ping

## HowTo start the container
Simply use the compose file: docker-compose up -d

### Container Networking
This will launch a network called studentnet01 and 3 containers which are connected to it called "studentmachine01, sshmachine01, sshmachine01a"

## HowTo stop the container
Simply use the compose file: docker-compose down

## Generate larger environments
You can use the script **generate-docker-compose-file.py** to generate yourself a docker-compose file with more studentmachines and sshmachines.
Simply execute it and answer the questions. It will create a docker-compose.yml file with n networks & n studentmachines, and m sshmachines per network / studenmtachine.
