# Simple AWS EC2 Deployment (SQLite3)

## DB Model: JobPrediction
- job_title (str)
- ai_exposure_index (float 0-1)
- tech_growth_factor (float)
- years_experience (float)
- average_salary (float)
- automation_probability (float opt)
- risk_category (str opt)
- prediction_type (str)
- created_at (datetime)

## EC2 (Amazon Linux) - From Windows PuTTY

1. Launch t2.micro EC2 (Amazon Linux 2023), open SSH/80, save .pem

2. Connect PuTTY (ec2-user@ip)

3. Setup:
```
sudo yum update -y
sudo yum install git python3 python3-pip nginx -y
```

4. Clone:
```
cd /opt
git clone YOUR_GITHUB_REPO_URL aijob
cd aijob
```

5. Venv:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Static:
```
python manage.py collectstatic --noinput
```

7. Gunicorn systemd (/etc/systemd/system/gunicorn.service):
```
[Unit]
Description=gunicorn
After=network.target

[Service]
User=ec2-user
WorkingDirectory=/opt/aijob
ExecStart=/opt/aijob/venv/bin/gunicorn --bind 0.0.0.0:8000 AIjob.wsgi
[Install]
WantedBy=multi-user.target
```

8. Nginx (/etc/nginx/conf.d/aijob.conf):
```
server {
    listen 80;
    location /static/ {
        root /opt/aijob;
    }
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

9. Start:
```
sudo nginx -t && sudo systemctl restart nginx
sudo systemctl daemon-reload && sudo systemctl start gunicorn && sudo systemctl enable gunicorn
```

10. Visit http://EC2-IP

SQLite3 works out-of-box (db.sqlite3 copied). DEBUG=False, change SECRET_KEY in settings.py.
