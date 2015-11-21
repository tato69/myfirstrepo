#!/bin/bash

function main {

date=`date +"%d/%m/%Y" `
echo "hello, i'm first exercise, today is $date and my master is Yoda"
echo -e "how many people are there?"
read -r people
echo "siamo $people"
count="0"
names=()
ages=()

while [ "$people" -gt "$count" ]
	do
	echo -e "enter your name :"
	read -r name
	names+=("$name")
	echo "age"
	read -r age
	ages+=($age)
	count=$(( $count + 1 ))
done

echo  '#################################################################'
echo -e "we are in total $people people\n"
count="0"
while [ "$people" -gt "$count" ]
	do
	echo -e "i'm `echo ${names[$count]}` and i'm ${ages[$count]} years old\n"
	count=$(( $count + 1 ))
done

count="0"
agesum="0"
while [ "$people" -gt "$count" ] 
	do
	agesum=$(( $agesum + ${ages[$count]} ))
	count=$(( $count + 1 ))
done

echo -e "The sum of our ages is $agesum\n"
echo -e "Our names are ${names[@]}\n"
echo  '#################################################################'
}

main
