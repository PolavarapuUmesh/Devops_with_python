# FROM ubuntu
# RUN apt-get update && apt-get install -y \
#     wget \
#     jenkins \
#     openjdk-11-jdk \
#     net-tools \
#     git \
#     python3 \
#     sudo
# ADD https://pkg.jenkins.io/debian-stable/jenkins.list /etc/apt/sources.list.d/jenkins.list
# RUN apt-get update
# RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" | EDITOR="tee -a" visudo
# RUN echo "/etc/init.d/jenkins start" >> /etc/bash.bashrc
# COPY sendmail.py /
# EXPOSE 8081
# CMD ["/etc/init.d/jenkins", "start"]

FROM ubuntu
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    git \
    openjdk-11-jdk \
    net-tools \
    python3 \
    sudo
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -
RUN sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt-get update && apt-get install -y jenkins
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" | EDITOR="tee -a" visudo
RUN echo "/etc/init.d/jenkins start" >> /etc/bash.bashrc
COPY sendmail.py /
COPY automation.py /
EXPOSE 8081
CMD ["/etc/init.d/jenkins", "start"]