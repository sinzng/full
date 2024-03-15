#!/bin/bash

if [ $# == 0 ]; then
	echo "Enter the country name~!!" 
else
	case "$1" in
		ko) echo "Seoul" ;;
		us) echo "Washington" ;;
		cn) echo "Beiging" ;;
		jp) echo "Tokyo" ;;
		*) echo "Enter the country name~!!" 
	esac
fi

