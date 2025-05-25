import os
import subprocess
from pathlib import Path

def run(command):
    print(f"\n[Running] {command}")
    subprocess.run(command, shell=True, check=True)

def write_file(path, content):
    with open(path, "w") as f:
        f.write(content.strip())

def main():
    # Update and install packages
    run("sudo apt update")
    run("sudo apt install -y python3 python3-venv python3-pip docker.io unzip curl git")

    # Create project folder
    project_dir = Path.home() / "flask-aws-project"
    project_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(project_dir)

    # Step 1: Create app.py
    write_file("app.py", """
    from flask import Flask
    import logging

    app = Flask(__name__)
    logging.basicConfig(filename='app.log', level=logging.INFO)

    @app.route("/")
    def home():
        app.logger.info("Homepage accessed")
        return {"message": "Hello from AWS + Docker!"}

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
    """)

    # Step 2: Create requirements.txt
    write_file("requirements.txt", "flask")

    # Step 3: Dockerfile
    write_file("Dockerfile", """
    FROM python:3.9-slim
    WORKDIR /app
    COPY requirements.txt .
    RUN pip install -r requirements.txt
    COPY . .
    CMD ["python", "app.py"]
    """)

    # Step 4: Docker build and run
    run("sudo docker build -t flask-aws-app .")
    run("sudo docker run -d -p 5000:5000 flask-aws-app")

    # Step 5: Install CloudWatch Agent
    os.chdir(Path.home())
    run("wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb")
    run("sudo dpkg -i amazon-cloudwatch-agent.deb")

    # Step 6: CloudWatch Agent config
    config_path = Path("config.json")
    write_file(config_path, """
    {
      "logs": {
        "logs_collected": {
          "files": {
            "collect_list": [
              {
                "file_path": "/home/ubuntu/flask-aws-project/app.log",
                "log_group_name": "flask-app-logs",
                "log_stream_name": "app-stream"
              }
            ]
          }
        }
      }
    }
    """)

    # Step 7: Start CloudWatch agent
    run(f"sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:{config_path} -s")

    # Step 8: Create upload script
    upload_script_path = Path("upload_logs.sh")
    write_file(upload_script_path, """
    #!/bin/bash
    aws s3 cp /home/ubuntu/flask-aws-project/app.log s3://your-bucket-name/logs/$(date +%F)-app.log
    """)
    run(f"chmod +x {upload_script_path}")

    # Step 9: Add cron job
    cron_cmd = f"(crontab -l 2>/dev/null; echo \"0 0 * * * {upload_script_path}\") | crontab -"
    run(cron_cmd)

    print("\n✅ Flask app deployed, Dockerized, and CloudWatch monitoring is active!")

if __name__ == "__main__":
    main()
