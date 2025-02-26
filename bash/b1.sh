#!/bin/bash

x=5
y=10

z=$(($x+$y))
echo $z

x=8
y=3

z=$(($x/$y))
echo $z

x=8.5
y=3.8

echo $x + $y | bc

x="hello"
y="world"

echo $x $y

# if CONDITION; then
#     ...
# fi

# if CONDITION
# then
#     ...
# fi

x=4
y=8

for i in `seq 1 5`
do
    if [ $i -gt 4 ]; then
        echo $i " is greater than 4"
    else
        echo $i " is not greater than 4"
    fi

    if [ $i -ge 4 ]; then
        echo $i " is greater or equal than 4"
    else
        echo $i " is not greater or equal than 4"
    fi
done

echo "\n\n\n\n"

if [ $2 ]; then
    echo "string 2 exists"
else
    echo "string 2 does not exist"
fi

if [ -z $3 ]; then
    echo "string 2 does not exist"
else
    echo "string 2 exists"
fi

if [ -n $3 ]; then
    echo "string 2 exists"
else
    echo "string 2 does not exist"
fi
