# define the list 
list=(108 109 110 111 112 113 114 115 117 119 120 121 122 123 124 125 126 127 129)

# get length of $list 
# (ref) https://www.cyberciti.biz/faq/finding-bash-shell-array-length-elements/

len=${#list[@]}


# Bash range:
# (ref) https://linuxhint.com/bash_range/
# (ref) https://stackoverflow.com/questions/169511/how-do-i-iterate-over-a-range-of-numbers-defined-by-variables-in-bash

for i in $(seq 0 $len);
    do 
        mkdir ${list[$i]}  
    done   
