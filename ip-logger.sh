#!/bin/bash
cat <<EOF >sample.log
My ID is : $(whoami)
My Uptime is : $(uptime)
My Path is : $(pwd)
EOF
