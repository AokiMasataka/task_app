#!/bin/sh
# entrypoint.sh
echo "Waiting for backend to be up..."
until nc -z task-app-back 8000; do
  sleep 1
done

echo "Starting nginx..."
nginx -g 'daemon off;'