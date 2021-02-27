FROM jenkins/jenkins:lts-alpine
USER root

RUN mkdir -p /usr/src/rep/
WORKDIR /usr/src/rep
VOLUME /Users/dmytro.maksymov/.jenkins /var/jenkins_home
COPY . /usr/src/rep/

EXPOSE 8080

RUN apk update \
&& apk add --upgrade \
&& apk add --update --no-cache python3 && \
 python3 -m ensurepip && \
 pip3 install --upgrade pip setuptools && \
 if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
 if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
 rm -r /root/.cache
RUN apk add pkgconf
RUN apk add build-base
RUN apk add python3-dev
#&& apt-get -y install python3-pip
