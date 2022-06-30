# Source for unblock watchers
    https://askubuntu.com/questions/828779/failed-to-add-run-systemd-ask-password-to-directory-watch-no-space-left-on-dev

# Source PM2
    https://pm2.keymetrics.io/docs/usage/quick-start/

# Pm2 Usefull Commands
    pm2 restart app_name
    pm2 delete app_name
    pm2 reload app_name
    pm2 stop app_name
    pm2 monit
    pm2 logs
    pm2 start app.js --name [here] --namespace [here] --watch --ignore-watch="node_modules"
    pm2 start app.js --name Service4 --namespace 8054 --watch

    pm2 start echosystem.config.json --name YuriLima --namespace 8041 --update-env

    pm2 start ecosystem.config.js --name YuriLima --namespace 8041

# Scan and Kill Ports
    sudo netstat -tlpn| grep chrome
    sudo netstat -tlpn| grep LISTEN
    sudo netstat -tlpn| grep python3
    fuser -k 8080/tcp

# Source Deploy Django app to VPS
    https://selmiabderrahim.medium.com/how-to-deploy-your-django-app-on-ovh-vps-with-nginx-ssl-certificate-domain-name-4da01aa5e44a

# Create a service for Gunicorn to run on VPS under Nginx
    1 - sudo nano /etc/systemd/system/yurilimaWebSite.service

    [Unit]
    Description=gunicorn_yurilima_website daemon  
    After=network.target

    [Service]
    User=yurilima
    Group=root
    WorkingDirectory=/www/wwwroot/projects/Yuri
    ExecStart=/www/wwwroot/resume.yurilima.com.br/Yuri-Lima/venv1/bin/gunicorn --access-logfile - --workers 3 --bind unix:/www/wwwroot/resume.yurilima.com.br/Yuri-Lima/yurilima.sock yurilima.wsgi:application

    [Install]
    WantedBy=multi-user.target

# Usefull Commands
    systemctl daemon-reload
    sudo systemctl start yurilimaWebSite
    sudo systemctl enable yurilimaWebSite
    sudo systemctl status yurilimaWebSite
    sudo systemctl restart yurilimaWebSite
    sudo systemctl stop yurilimaWebSite
    gunicorn yurilima.wsgi --preload --log-file - -b 0.0.0.0:8041

    proxy: http://unix:/www/wwwroot/resume.yurilima.com.br/Yuri-Lima/yurilima.sock