#!/bin/bash

echo "What is your name?"

read name

echo "What is your age?"

read age

echo "Hello $name, you are $age years old."

sleep 1

echo "Loading..."

sleep 1

getrich=$((( $RANDOM % 15) + $age ))

echo "$name you will be $getrich years old soon."
