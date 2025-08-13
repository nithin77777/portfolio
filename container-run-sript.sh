#!/bin/bash

# Stop and remove old containers if they exist
sudo docker rm -f container1 container2 container3 2>/dev/null

# Run all three containers with different ports
sudo docker run -d --env-file .env -p 8001:8000 --name container1 production:v1.0
sudo docker run -d --env-file .env -p 8002:8000 --name container2 production:v1.0
sudo docker run -d --env-file .env -p 8003:8000 --name container3 production:v1.0

echo "✅ All SkillDesk containers started:"
sudo docker ps --filter "name=container"

