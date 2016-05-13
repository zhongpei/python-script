import os
import popen2

def dmesg():
    r,w,e = popen2.popen3('dmesg')
    return r.readlines()

def formart_time(t):
    r,w,e = popen2.popen3("""date -d "1970-01-01 UTC `echo "$(date +%s)-$(cat /proc/uptime|cut -f 1 -d' ')+"""+t+""""|bc ` seconds" """)
    return "".join( r.readlines() )

def fomart(lines):
    for l in lines:
        s = l.find('[')
        e = l.find(']')
        t = l[s+1:e]
        print formart_time( t).replace("\n","") + l[e+1:].replace("\n","")


lines = dmesg()
fomart(lines)
