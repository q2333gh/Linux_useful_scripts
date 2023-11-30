https://www.cyberciti.biz/faq/linux-unix-running-sudo-command-without-a-password/#:~:text=The%20procedure%20to%20configure%20sudo%20without%20a%20password,5%20Save%20and%20exit%20the%20file.%20More%20items

```bash
cp /etc/sudoers /root/sudoers.bak
sudo chmod 777 /etc/sudoers 
# give vivek sudo no need passwd
echo 'vivek ALL = NOPASSWD: /bin/systemctl restart httpd.service, /bin/kill' >> /etc/sudoers 
# test 
chmod 777 xxx 

# maybe sudo chmod 777 /etc/sudoers  is not a good approach for production vm. local testing vm look fine ?

btwl@btwl-virtual-machine ~/D/i/tax_lint (master)> tldr visudo
visudo
Safely edit the sudoers file.More information: https://www.sudo.ws/docs/man/visudo.man.

 - Edit the sudoers file:
   sudo visudo

 - Check the sudoers file for errors:
   sudo visudo -c

 - Edit the sudoers file using a specific editor:
   sudo EDITOR={{editor}} visudo

 - Display version information:
   visudo --version




```