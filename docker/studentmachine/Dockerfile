#From localhost:5000/studentmachine
From  ros:melodic-ros-core
MAINTAINER Frank Gut <info@fdoelitzscher.de>

User root

Run apt-get update  -q 

# Install latest verison of Ansible from ppa:ansible Ubuntu repo
Run DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends \
  bash openssh-client openssh-server locales locales-all software-properties-common iputils-ping net-tools iproute2 vim nano less netcat figlet sudo &&\ 
  apt-add-repository ppa:ansible/ansible && \
  apt-get update -q && \
  apt-get install -y ansible && \
  rm -Rf /var/lib/apt/lists/* && \
  apt-get clean  

ENV LC_All en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN mkdir -p /var/run/sshd && chmod 0755 /var/run/sshd
RUN echo 'root:toor' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN echo "X11UseLocalhost no" >> /etc/ssh/sshd_config
RUN mkdir /root/.ssh

RUN useradd -c "student" \
            -p $(openssl passwd -1 student) \
            -d /home/student -m \
            -u 27274 \
            -s /bin/bash \
            --groups sudo student
RUN mkdir /home/student/.ssh
ADD .ssh/ /home/student/.ssh
RUN chown -R student:student /home/student/.ssh
RUN chmod 600 /home/student/.ssh/id_rsa
ADD ansible /home/student/ansible
RUN chown -R student:student /home/student/ansible
ADD files/studentmachine_motd /etc/motd
RUN echo "cat /etc/motd" >> /etc/bash.bashrc

EXPOSE 22

CMD   ["/usr/sbin/sshd", "-D"]
