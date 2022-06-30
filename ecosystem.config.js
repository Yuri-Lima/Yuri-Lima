module.exports = {
  apps : 
  [
    {
      name:'YuriLima_WebSite',
      script: 'manage.py',
      args: ["runserver", "127.0.0.1:8042"], 
      exec_mode: "fork",
      wait_ready: true, 
      autorestart: false,
      interpreter : "/www/wwwroot/projects/Yuri/env/bin/python3",
      watch: false
    },
  ]
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
