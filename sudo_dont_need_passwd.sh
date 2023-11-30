#/bin/bash


# <!-- <!-- TODO  -->
# current manually do these : 
# make user_name as para 1 input .
# and automate these :  -->

sudo cp /etc/sudoers ~/sudoers.bak

sudo visudo
# sudo EDITOR=vim visudo

# maybe echo this conetent in ? 
user_name ALL=(ALL) NOPASSWD:ALL



