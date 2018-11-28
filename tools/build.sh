#!/bin/sh

MAKE_LOG="make.log"

echo 'begin build'

echo 'downloading local sphinx libraries'
#pip install -U sphinx
#apt-get install -y libxml2-dev

cd /app/documentation
echo 'building html'
make clean
make html 2>&1 | tee $MAKE_LOG
NUM_ERROR=$(grep -c "ERROR:" "$MAKE_LOG")
NUM_WARNING=$(grep -c "WARNING:" "$MAKE_LOG")
NUM_TOTAL=`expr $NUM_ERROR + $NUM_WARNING`
if [ $NUM_TOTAL -eq 0 ]; then
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
  echo
  echo 'build failed due to the following warnings or errors:'
  if [ $NUM_ERROR -gt 0 ]; then
    echo
    echo 'Errors:'
    grep 'ERROR:' $MAKE_LOG
  fi
  if [ $NUM_WARNING -gt 0 ]; then
    echo
    echo 'Warnings:'
    grep 'WARNING:' $MAKE_LOG
  fi
  echo
  exit_status = 1
fi
exit $exit_status
