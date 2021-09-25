#!/bin/bash
check_string () {
    typeset -a data=("$@")
    typeset -i count=0
    #for string in ${data[@]};
    for string in "$@";
    do 
        
        if [[ $string =~ \.*[A-Z]+\.* ]];
        then
            count=$(($count + 1))
        fi
    done
    echo $count
    return 0
}

check_string "WindowsXP" "Windows 1W0" "WindowsME" "Windows8.1"
