module.exports = {
  apps : 
  [
    {
      name:'YuriLima_WebSite',
      script: 'manage.py',
      args: ["runserver", "127.0.0.1:8041"],
      exec_mode: "fork",
      instances: "1",
      wait_ready: true, 
      autorestart: false, 
      max_restarts: 5, 
      interpreter : "/usr/bin/python3",
      watch: '.'
    },
  ],
  deploy : 
  {
    production : 
    {
      user : 'SSH_USERNAME',
      host : 'SSH_HOSTMACHINE',
      ref  : 'origin/main',
      repo : 'https://github.com/Yuri-Lima/Yuri-Lima.git',
      path : '/www/wwwroot/resume.yurilima.com.br/Yuri-Lima',
      'pre-deploy-local': '',
      'post-deploy' : 'npm install && pm2 reload ecosystem.config.js --env production',
      'pre-setup': ''
    }
  }
};

// "apps": [{
    //     "name": "YuriLima_WebSite",
    //     "script": "manage.py",
    //     "args": ["runserver", "127.0.0.1:8041"],
    //     "exec_mode": "fork",
    //     "instances": "1",
    //     "wait_ready": true,
    //     "autorestart": false,
    //     "max_restarts": 5,
    //     "interpreter": "/usr/bin/python3",
    //     "watch": ".", 
    //     "repo" : "https://github.com/Yuri-Lima/Yuri-Lima.git",
    // }]
