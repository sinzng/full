#!/bin/bash

count=1
cat test | while read line
do
	echo "line $count : $line"
	count=$[ $count + 1 ]
done
echo "Finishing processing the file"
