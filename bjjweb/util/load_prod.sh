#!/bin/bash
 
# This script does the following:
# 1/ capture and download the latest backup
# 2/ load it to your local database
# 3/ run your app and open Safari
 
# Just replace any uppercase string with your own data
 
#
# CAPTURE
#
cd /tmp/
heroku pgbackups:capture --expire --app bjjweb
file_path="db_$(date +%Y_%m_%d-%H_%M_%S).dump"
curl `heroku pgbackups:url --app bjjweb` > $file_path
 
#
# LOAD
#
dropdb bjjweb
createdb bjjweb
pg_restore --verbose --clean --no-acl --no-owner --superuser=postgres -h localhost -U postgres -d bjjweb $file_path
