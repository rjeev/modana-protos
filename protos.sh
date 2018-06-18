#!/usr/bin/env bash


PROTOS_PATH="protos"

if [ "$#" -ne 1 ]; then
    echo "Invalid parameters, pass 'pull' or 'push'"
    exit
fi

if [ $1 == "pull" ]
then
  echo "Pulling latest protos"
  git subtree pull --prefix=${PROTOS_PATH} https://github.com/sharad23/modana-protos.git master --squash
elif [ $1 == "push" ]
then
  echo "Pushing protos"
  git subtree push --prefix=${PROTOS_PATH} https://github.com/sharad23/modana-protos.git master --squash
elif [ $1 == "init" ]
then
  echo "Initializing protos"
  git subtree add --prefix=${PROTOS_PATH} https://github.com/sharad23/modana-protos.git master --squash
else
  echo "Invalid parameters, pass 'init', 'pull' or 'push'"
fi