https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/#:~:text=The%20procedure%20to%20configure%20sudo%20without%20a%20password,5%20Save%20and%20exit%20the%20file.%20More%20items

```bash
cp /etc/sudoers /root/sudoers.bak
sudo chmod 777 /etc/sudoers 
# give vivek sudo no need passwd
echo 'vivek ALL = NOPASSWD: /bin/systemctl restart httpd.service, /bin/kill' >> /etc/sudoers 
# test 
chmod 777 xxx 
```