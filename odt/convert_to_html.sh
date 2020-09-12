#/bin/bash

for filename in ./*.odt
do
    libreoffice --headless --invisible --norestore --convert-to html "$filename"
done;


