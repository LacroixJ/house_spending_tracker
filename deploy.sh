#!/bin/bash

sudo cp -r app.py run.py static templates /var/www/money
sudo cp __wsgi.py /var/www/money/wsgi.py

sudo chown -R root:webapps /var/www/money
sudo chmod 775 -R /var/www/money

sed -i 's/db\.db/\/var\/www\/money\/db\.db/g' /var/www/money/app.py

#Make sure to update the apache config if neccesary
#Also don't forget to setup the database if changes were made there!

sudo systemctl restart apache2
