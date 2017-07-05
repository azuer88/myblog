Title: Setting up fileshackproject on CentOS 6
Date: 2017-07-05 13:33:45 PHT+0800
Category: django
Slug: setting-up-fileshackproject-on-centos-6
Tags: filedrop,centos,apache,configure,setup
Authors: Blue Cuenca
Summary: Setting the django app fileshackproject on CentOS 6 running apache 2.2


<!-- start here -->
**NB: This will install global django, DOES NOT use virtualenv.**

Install the necessary packages:

```
yum install mod_wsgi 
yum install python-pip
yum install git
```

Install the correct version of django (v1.4.22)
```
pip install django\<1.5
```
(I haven't tested this with any other version of django)

Create project directory (and change into)
```
mkdir /opt/www/django/
```

Download project from github
```
git git://github.com/peterkuma/fileshackproject.git 
```

Change owner of all these files to apache
```
chown -R apache:apache /opt/www
```

Create the apache configuration file (in /etc/httpd/conf.d/fileshack.conf) with the following content:
```
WSGIScriptAlias / /opt/www/django/fileshackproject/fileshackproject/wsgi.py
WSGIPythonPath /opt/wwww/django/fileshackproject

Alias /static/ /opt/www/django/fileshackproject/static/
Alias /media/ /opt/www/django/fileshackproject/media/

<Directory /opt/www/django/fileshackproject>
    <Files wsgi.py>
	Order deny,allow
        Allow from all
    </Files>
</Directory>
```

(Optional) update SELinux Permissions
```
setsebool -P httpd_can_network_connect 1
chcon -R -t httpd_sys_content_t /opt/www/django
chcon -R -t httpd_sys_content_rw_t /opt/www/django
```

Restart apache
```
apachectl -k restart
```

And we are done!

