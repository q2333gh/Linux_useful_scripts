 how to check docker container --restart  policy for all container ?
 ```
 docker ps -aq | xargs docker inspect --format '{{ .Name }}: {{ .HostConfig.RestartPolicy }}'
 ```

 