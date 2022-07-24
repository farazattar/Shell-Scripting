#!/bin/sh
echo "Please enter your name:"
read name
echo "Please enter your family name:"
read family
echo -e "\033[0;31mYour name is $name."
echo -e "\033[0;36mYour name is $family.\n\n"
echo -e "\033[0mPlease enter your birthday's year:"
read year
echo "You are born in $year."
current_year=`date "+%Y"`
age=$((($current_year)-($year))) 
echo "You are $age years old."
months=$((age*12))
echo "$months months are passed."
days=$((months*30))
echo "$days days are passed."

