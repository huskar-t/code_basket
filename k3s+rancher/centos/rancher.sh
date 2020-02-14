#!/bin/sh
set -e
#rancher
docker run -d -v /data/docker/rancher-server/var/lib/rancher/:/var/lib/rancher/ --restart=unless-stopped --name rancher-server -p 9443:443 rancher/rancher:stable

echo https://$(curl http://ip.cip.cc/):9443