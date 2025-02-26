#!/bin/bash

helloWorld(){
    echo "Hello world"
}

helloWorld

var1='a'
var2='b'

function testVar(){
    var1='c'
    local var2='d'

    echo "Inside function: $var1, $var2"
}

echo "Before function call: $var1, $var2"

testVar

echo "After function call: $var1, $var2"

function testRet(){
    return="some result"
    return 255
}

testRet
echo $?
echo $return

function testRes2(){
    local result="some result 2"
    echo "$result"
}

res="$(testRes2)"
echo $res

hi=$1
sayHello(){
    echo "Hello $hi!!!"
}

sayHello