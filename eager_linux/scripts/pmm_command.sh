#!/bin/bash

echo Hi
echo Just makemigartions then migrate [app Optional]

while getopts app: option
do 
    case "${option}"
        in
        p)app=${OPTARG};;
    esac
done
echo $app

python manage.py makemigrations $app &&\
python manage.py migrate $app
