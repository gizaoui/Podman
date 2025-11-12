# Firefox


```bash
podman --version
podman info
podman ps
podman ps -a
systemctl --user status dbus.socket
systemctl --user enable --now dbus.socket
```

```bash
flatpak update --user io.podman_desktop.PodmanDesktop
flatpak run io.podman_desktop.PodmanDesktop
```

```bash

```


```bash
# https://infotechys.com/deploying-mysql-using-podman/
# https://podman.io/blogs/2018/10/03/podman-remove-content-homedir
podman pull docker.io/library/mysql:latest

rm -rf /home/gizaoui/db_data && \
mkdir /home/gizaoui/db_data && \
podman unshare chown -R 999:999 /home/gizaoui/db_data && \
ls -l -d /home/gizaoui/db_data

rm -rf /home/gizaoui/db_data && \
mkdir /home/gizaoui/db_data && \
ls -l -d /home/gizaoui/db_data

podman run -d --name mysql-container \
-e MYSQL_USER=gzi \
-e MYSQL_PASSWORD=gzipwd \
-e MYSQL_DATABASE=dev_data \
-e MYSQL_ROOT_PASSWORD=gzipwdadm \
-v /home/gizaoui/db_data:/var/lib/mysql:Z \
--publish 3306:3306 \
mysql:latest

ls -l /home/gizaoui/db_data

podman container logs mysql-container

podman exec -it mysql-container /bin/bash # -c "mkdir /testdir; touch /testdir/testfile; chown -R 1:1 /testdir"

rootlesskit bash
rm -rf /home/gizaoui/db_data

```

```bash
podman unshare cat /proc/self/uid_map
         0       1001          1
         1     165536      65536

podman unshare cat /proc/self/gid_map
         0       1001          1
         1     165536      65536

podman unshare chown 27:27 /home/gizaoui/db_data/
$ ll -d ~/db_data/
drwxr-xr-x 2 165562 165562 4096  9 nov.  08:34 /home/gizaoui/db_data/
```


```bash
podman create --name c1 centos:7 sleep infinity
podman images
podman image ls
podman ps -a
podman start c1
podman restart c1
podman stop c1
podman rm -f c1
podman ps -a -q | xargs podman rm -f
podman run --privileged --name c1 -ti --rm --env="DISPLAY" --net=host  --mount type=bind,source=/home/gizaoui,destination=/root mycentos /usr/bin/bash
podman create --name c1  --env="DISPLAY" --net=host  --mount type=bind,source=/home/gizaoui,destination=/root mycentos sleep infinity
podman exec -ti c1 /usr/bin/bash
podman info | grep graphRoot: # graphRoot: /home/gizaoui/.local/share/containers/storage
podman login docker.io
```

**JVM**


```bash
ENV JAVA_OPTS="-XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap "

java -XX:+PrintFlagsFinal -XX:+UnlockExperimentalVMOptions -XX:+UseCGroupMemoryLimitForHeap -XX:MaxRAM=4g -XX:MaxRAMPercentage=80.0 -Xms2g -Xmx4g -version | grep -Ei "InitialHeapSize|maxheapsize|maxram|UnlockExperimentalVMOptions"

/root/jdk/jdk1.8.0_202/bin/jconsole

cd /root/jdk && javac Main.java && java -XX:+UnlockExperimentalVMOptions -XX:MaxRAM=2g -XX:MaxRAMPercentage=100.0 -Xms512m -Xmx2048m -cp . Main

cd /root/jdk && javac Main.java && java -Xms2g -Xmx4g -cp . Main

```

```bash
docker pull centos:7
xhost local:root # This permits the root user on the local machine to connect to X windows display.
xhost + # /!\ A EVITER : La commande "xhost +" désactive le contrôle d'accès à votre serveur X11
docker container run -it --name=sap --env="DISPLAY" --net=host -v /tmp:/tmp centos:7
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum install -y gvim
yum install -y xclock
dbus-uuidgen > /etc/machine-id

# Error: no DISPLAY
gvim 
```


```bash
env | grep '^DISPLAY='
xhost local:root # This permits the root user on the local machine to connect to X windows display.
xhost + # /!\ A EVITER : La commande "xhost +" désactive le contrôle d'accès à votre serveur X11
docker start sap
docker exec -ti sap bash
xclock
```

https://github.com/gizaoui/Tools/tree/main/debian

```bash
# Dockerfile
FROM centos:7
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum install -y gvim
CMD ["/usr/bin/gvim"]
sh -c "sleep infinity"
```

```bash
docker build -t mygvim .
docker container run -it --env="DISPLAY" --net=host -v /tmp:/tmp mygvim
```

---

## bind mount


```bash
# en root
mkdir /data
mkdir /data2
touch /data/toto
findmnt # liste les pts de mountage
mount --bind /data/ /data2/
findmnt # liste les pts de mountage
ls /data2 # présebce du fichier 'toto'
umount /data2
rm -rf /data2 /data
```

```bash
docker run -d --name c1 --mount type=bind,source=/data/,destination=/usr/share/ngnix/html nginx:latest

docker exec -ti c1 bash
docker inspect --format "{{.Mount}}" c1 # Liste des mounts
```

## Volume Docker

```bash
docker volume create myvolume
docker volume ls
docker run -d --name c2 --mount type=volume,src=myvolume,destination=/usr/share/ngnix/html nginx:latest
docker exec -ti c2 bash
```

   
## TMPFS

```bash
docker run -d --name c3 --mount type=tmpfs,destination=/usr/share/ngnix/html nginx:latest
docker exec -ti c3 bash
```

---

```bash
useradd -m mysql --uid 166534 --shell /bin/bash
id mysql # usertst:x:1002:1002::/home/usertst:/bin/bash
userdel -r mysql
```

```bash
FROM centos:7
RUN dbus-uuidgen > /etc/machine-id
RUN useradd -m gizaoui --uid 1001 --shell /bin/bash
RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
RUN yum install -y gvim firefox
```


```bash
xhost local:gizaoui
docker builder prune && docker build -t mycentos .
dpsaq | xargs docker rm -f # Suppression des container
docker container run -it --name c1 -u $USER --env="DISPLAY" --net=host -v '/tmp:/tmp' mycentos
docker container run -it --name c1 -u $USER --env="DISPLAY" --net=host -v '/home/gizaoui/data:/tmp' mycentos # creation de 'data' en 'root'
docker container run -it --name c1 -u $USER --env="DISPLAY" --net=host  --mount type=bind,source=/home/gizaoui,destination=/home/gizaoui mycentos
docker start c1
docker exec -ti c1 bash
```




- https://www.mastertheboss.com/soa-cloud/docker/how-to-configure-java-memory-in-a-docker-container/
- https://b.agilob.net/programming/java/jvm-considerations-on-kubernetes/
- https://www.jmdoudoux.fr/java/dej/chap-jvm-docker.htm
- https://www.youtube.com/watch?v=kwEutvibzCU&t=227s
- https://blog.stackademic.com/5-ways-i-tune-jvm-in-a-docker-image-ace1d8dba4b3
- https://willsena.dev/building-kubernetes-style-pods-with-podman/
- https://www.linkedin.com/pulse/using-podman-generate-test-kubernetes-yaml-manifest-tom-dean



66.3. Le support de Docker par la JVM







-  469  for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do  apt-get remove $pkg; done
-  470  apt-get install ca-certificates curl
-  471   install -m 0755 -d /etc/apt/keyrings
-  472  curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
-  473  chmod a+r /etc/apt/keyrings/docker.asc
-  474  echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
-  475    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |    tee /etc/apt/sources.list.d/docker.list > /dev/null
-  476  cat /etc/apt/sources.list.d/docker.list
-  478   apt-get update
-  479   apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
-  480  systemctl status docker
-  481  systemctl restart docker
-  482  systemctl status docker
-  483  systemctl enable docker
-  486  chmod 777 /var/run/docker.sock
-  489  usermod -a -G docker gizaoui
-  490  groupmod -g gizaoui docker


 
