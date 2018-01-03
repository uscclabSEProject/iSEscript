#!/bin/bash
lastTimeFile=/tmp/writeLastTime

# check last time file exist
if [ ! -f $lastTimeFile ]; then
    date +%s > $lastTimeFile
    exit 1
fi

lastTime=$(head -n1 $lastTimeFile)
nowTime=$(date +%s)

IFS=$'\n'
for line in $(grep "type=AVC" audit.log.1); do
    for pid in  $(echo $line  | grep -o '\bpid=[1-9][0-9]\+' | cut -d '=' -f 2); do
        allPspid=$(ps aux |  ps aux | awk -F ' ' '{print $2}')
        for psPid in $allPspid; do
            if [ "$psPid" == "$pid" ]; then 
                ps --pid $psPid -u
                echo $line
                echo "";
                echo "";
            fi
        done
        
    done
done
# Regex matching with =~ operator within [[ double brackets ]].
#if [[ "$variable" =~ T.........fin*es* ]]
## NOTE: As of version 3.2 of Bash, expression to match no longer quoted.
#then
#  echo "match found"
#  echo ${BASH_REMATCH[@]}
#fi
