#!/bin/bash

for i in 1 2 3 4 5
do
   echo $i
done

i=0
for p in $@
do
    i=$(($i + 1))
   echo argument $i = $p
done