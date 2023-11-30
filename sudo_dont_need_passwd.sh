#/bin/bash


# <!-- <!-- TODO  -->
# current manually do these : 
# make user_name as para 1 input .
# and automate these :  -->

sudo cp /etc/sudoers ~/sudoers.bak

sudo visudo
# sudo EDITOR=vim visudo

# maybe echo this conetent in ? 

append this into :

all cmds:
user_name ALL=(ALL) NOPASSWD:ALL

specific cmds:
user_name ALL=(ALL) NOPASSWD:/usr/bin/apt update, /usr/bin/apt upgrade


