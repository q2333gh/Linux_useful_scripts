 how to check docker container --restart  policy for all container ?
 ```
 docker ps -aq | xargs docker inspect --format '{{ .Name }}: {{ .HostConfig.RestartPolicy }}'
 ```

 
## mew a ubuntu with name specified.
 btwl@btwl-virtual-machine ~/c/open-chat (master)> docker ps -a | grep ubuntu
c6a2b1c712af   ubuntu                         "/bin/bash"              7 minutes ago   Up 3 minutes                         intelligent_knuth
btwl@btwl-virtual-machine ~/c/open-chat (master)> docker rename intelligent_knuth pic_test
btwl@btwl-virtual-machine ~/c/open-chat (master)> docker exec pic_test ls /opt/


btwl@btwl-virtual-machine ~/c/open-chat (master)> ls^C
btwl@btwl-virtual-machine ~/c/open-chat (master)> docker cp ^C
btwl@btwl-virtual-machine ~/c/open-chat (master)> docker cp /opt/pocket-ic pic_test:/opt/


Successfully copied 44.5MB to pic_test:/opt/
btwl@btwl-virtual-machine ~/c/open-chat (master)> docker run -it ubuntu^C

## enable proxy in docker container ?

