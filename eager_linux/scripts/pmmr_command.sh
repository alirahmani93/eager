#!/bin/bash

echo Hi
while getopts p: option
do 
    case "${option}"
        in
        p)port=${OPTARG};;
    esac
done
echo $port

python manage.py makemigrations &&\
python manage.py migrate &&\
python manage.py runserver $port
