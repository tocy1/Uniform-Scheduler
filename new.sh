#!/bin/bash
to_lower_case () {
    result=$(echo "$*" | tr '[:upper:]' '[:lower:]') 
    echo $result
    return 0
}

to_lower_case "WindowsXP" "Windows 1W0" "WindowsME" "Windows8.1"
