#!/bin/bash

echo 'checking branch name'

if [[ $CI_COMMIT_BRANCH = master ]]; then
  TARGET_DIR=public_html/documentation-dev
elif [[ $CI_COMMIT_BRANCH =~ ^maint ]]; then
  TARGET_DIR=public_html/documentation
else
  echo 'Deployment skipped since this branch is not deployable. It must be merged to the master or a maintenance branck: ' $CI_COMMIT_BRANCH
  exit 0
fi

echo 'beginning deployment'

echo "$SSH_PRIVATE_KEY" | base64 -d > ./key.txt
chmod 600 ./key.txt

echo 'transfering tarball'
scp -P 2222 -i ./key.txt -oHostKeyAlgorithms=+ssh-dss -oStrictHostKeyChecking=no ./gitlab.tar.gz pflotran@108.167.189.107:~
exit_status=$?
if [ $exit_status -eq 0 ]; then
  echo 'transfer successful'
  echo 'extracting tarball to' $TARGET_DIR
  ssh -p 2222 -i ./key.txt -oHostKeyAlgorithms=+ssh-dss -oStrictHostKeyChecking=no pflotran@108.167.189.107 "/bin/rm -Rf $TARGET_DIR/* && tar -xzvf gitlab.tar.gz -C $TARGET_DIR/. && /bin/rm gitlab.tar.gz"
  exit_status=$?
  if [ $exit_status -eq 0 ]; then
    echo 'extraction successful'
    echo 'successful deployment'
  else
    echo 'extraction failed'
  fi
else
  echo 'transfer failed'
fi
exit $exit_status
