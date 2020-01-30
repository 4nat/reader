#!/bin/bash
echo "Type your secret code"
read secret
otext=`echo 'Nzc3Nzk5Cg==' | base64 --decode`
if [ $secret == $otext ]; then
echo "You are authenticated"
else
echo "You are not authenticated"
fi
