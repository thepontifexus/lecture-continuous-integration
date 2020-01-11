# Student SSH Ansible Target Container

**Container name**: sshmachine

This docker image provides the target machine where students can try out their Ansible excercices.
It contains an OpenSSH Server, Ansible can connect from the "studentmachine" container to it.

It is based on Ubuntu 18.04 with the following additional software packages installed:
  * OpenSSH Server

## HowTo build this container
    docker build -t sshmachine .

## HowTo start the container
For the lecture environment, it is automatically started from the docker-compose file by the other conteiner "studentmachine". 
Have a look into the folder docker/studentmachine.

If you want to launch this container manually, you can do it via:
    docker run -d -P --network ubuntu1804_studentnet1 --network-alias sshmachine sshmachine
    docker port sshmachine 22
