#!/bin/bash
TERRAFORM_VERSION="0.9.4"
docker run --rm -v $(pwd):/data --workdir=/data hashicorp/terraform:$TERRAFORM_VERSION plan
if [ $? -ne 0 ]; then
  exit 1
fi
RETRIES=0
while [ $RETRIES -lt 3 ]; do
  docker run --rm -v $(pwd):/data --workdir=/data hashicorp/terraform:$TERRAFORM_VERSION apply
  if [ $? -eq 0 ]; then
    break
  fi
  let RETRIES=RETRIES+1
done
