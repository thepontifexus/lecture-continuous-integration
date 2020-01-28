#From localhost:5000/ubuntu1804
From ubuntu:18.04
MAINTAINER Frank Gut 

Run apt-get update -q 

Run DEBIAN_FRONTEND='noninteractive' apt-get install -y --no-install-recommends \
    locales software-properties-common iputils-ping net-tools iproute2 openssh-server nano less netcat vim nano less netcat figlet sudo

RUN mkdir -p /var/run/sshd && chmod 0755 /var/run/sshd 

RUN echo 'root:toor' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN mkdir /root/.ssh

RUN useradd -c "student" \
            -p $(openssl passwd -1 student) \
            -d /home/student -m \
            -u 999 \
            --shell /bin/bash \
            -G sudo student

RUN mkdir /home/student/.ssh
ADD .ssh/ /home/student/.ssh
RUN chown -R student:student /home/student/.ssh
RUN chmod 600 /home/student/.ssh/id_rsa

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD files/sshmachine_motd /etc/motd
RUN echo "cat /etc/motd" >> /etc/bash.bashrc

EXPOSE 22

CMD   ["/usr/sbin/sshd", "-D"]

