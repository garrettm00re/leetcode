#! /bin/bash

# Compile and run a C++ file
file=$1

# Shift the first argument (filename)
shift

# Store remaining arguments
args="$@"


g++ $file -o ${file%.cpp}

if [ $? -eq 0 ]; then
    ./${file%.cpp} $args
else
    echo "Compilation failed"
fi

