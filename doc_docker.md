# Docker Commands
## Docker Build
```
sudo docker build -t ktalant/api4:v1 .
```
## Docker Run
```
 sudo docker run --name api4  -d -p 8080:5000 ktalant/api4:v1
```
## Remove all stopped containers
```
for i in $(sudo docker ps -aq); do sudo docker rm $i; done

```