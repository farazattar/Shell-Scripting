#!/bin/bash
CMD_STR1=`ifconfig -a`
CMD_STR2=`curl api.ipify.org`
cat << EOF >show-ip.html
<html>
<head>
My IP Address
</head>
<body>
<h3>
This is my NICs
</h3>
<pre>
$CMD_STR1
</pre>
<h3>
This is my public IP Address
</h3>
<pre>
$CMD_STR2
</pre>
</body>
</html>
EOF
firefox show-ip.html
