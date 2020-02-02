#!/bin/bash

if [ $? -ne 0 ]; then
    echo
    echo "It appears that pdftools is not installed...would you like to install it? y/n"
else
    exit 0
fi

read answer
if [ $answer == 'y' ]; then
    sudo apt-get install poppler-utils
else
    exit 0
fi


