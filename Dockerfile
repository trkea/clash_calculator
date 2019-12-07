FROM centos:centos7

#start
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm

# python3.6 and django
RUN yum search python36
RUN yum -y install python36u python36u-pip python36u-libs python36u-devel 
RUN python3.6 -m pip install --upgrade pip
RUN python3.6 -m venv venv
RUN source venv/bin/activate
RUN pip install django requests
RUN yum -y install httpd-devel
RUN yum -y install python36u-mod_wsgi

# git
RUN yum -y install git2u yum-utils
RUN yum-config-manager --disable ius
RUN git --version
