#!/bin/sh

echo 'begin build'

echo 'downloading local sphinx libraries'
pip install -U sphinx
apt-get install -y libxml2-dev

cd /app/documentation
echo 'building html'
make clean
make html
exit_status=$?
if [ $exit_status -eq 0 ]; then
  echo 'build succeeded'
  echo 'building tarball'
  cd _build/html
  tar -czvf /tmp/codeship.tar.gz *
  exit_status=$?
  if [ $exit_status -gt 0 ]; then
    echo 'tarball failed'
  else
    echo 'tarball succeeded'
  fi
else
  echo 'build failed'
fi
exit $exit_status
