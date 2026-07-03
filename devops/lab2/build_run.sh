#!/bin/bash
docker build -t myimage:single-stage .
docker run -d --name mycontainer -p 80:80 myimage:single-stage