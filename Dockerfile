FROM centos

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum search python36
RUN yum install python36u
RUN python3.6 -m venv venv
RUN source venv/bin/activate
RUN pip install Django==2.0
RUN yum install httpd-devel
RUN yum install python36u-mod_wsgi
