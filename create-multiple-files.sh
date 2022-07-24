#!/bin/bash
echo "Please enter the first variable:"
read var1
echo "Please enter the second variable:"
read var2
touch "$var1$var2"{1..9}
ls -al | grep $var1$var2 | wc -l
