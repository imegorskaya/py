#!/bin/sh
echo "This script checks the existence of the message file/"
echo "Checking..."
if [ -f /var/log/messages ]
    then
        echo "/var/log/message exists.'
echo
echo "done."