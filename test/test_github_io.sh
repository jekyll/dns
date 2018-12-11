#!/bin/bash

echo "--> Using curl"
curl --version
echo ; echo

echo "--> Using grep"
grep --version
grep --help
echo ; echo

for domain in $(script/list-domains | grep CNAME | grep '\-> jekyll.github.io' | awk '{print $2}'); do
  echo "--> Testing $domain"
  echo "---------------------------------"

  outfile=$(mktemp)
  trap 'rm $outfile' EXIT
  curl -sSfLv "https://$domain" > /dev/null 2>"$outfile"

  statuscode=$(grep '< HTTP/' $outfile | tail -n1 | awk '{print $3}')
  echo "Got $statuscode Status from $domain"

  [ "$statuscode" = "200" ] || {
      cat "$outfile"
      echo " !!! Not a 200: '$statuscode'"
      exit 1
  }

  echo ; echo;
done
