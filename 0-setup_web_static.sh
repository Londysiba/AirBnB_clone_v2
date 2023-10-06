#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static

apt-get update
apt-get install -y nginx
ufw allow 'Nginx HTTP'

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

echo "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By \"$HOSTNAME\";

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
                try_files \$uri \$uri/ =404;
        }

        location /hbnb_static {
                alias /data/web_static/current;
                index index.html index.htm;
        }

        location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
        }
        error_page 404 /error_404.html;
}" > /etc/nginx/sites-available/default

service nginx restart
