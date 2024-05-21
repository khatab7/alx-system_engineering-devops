#!/usr/bin/env bash
# connect a server

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/school
