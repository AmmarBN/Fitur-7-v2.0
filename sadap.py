#Jangan Di Recode Masih Update Gan
import os,sys,time,requests
import subprocess
os.system("clear")
logo = """
  ___    __    __  __    _   _    __     ___  _  _  ____  ____  ___
 / __)  /__\  (  \/  )  ( )_( )  /__\   / __)( )/ )( ___)(  _ \/ __)
( (__  /(__)\  )    (    ) _ (  /(__)\ ( (__  )  (  )__)  )   /\__ \

\033[1;31m \___)(__)(__)(_/\/\_)  (_) (_)(__)(__) \___)(_)\_)(____)(_)\_)(___/
"""
print ("Your Device")
os.system ("neofetch")
# mengetik otomatis
def mengetik(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)

def lagi():
       f = raw_input("Login Lagi? (y/t):")
       if f == "y":
           os.system("python2 sadap.py")
       elif f == "t":
              os.system("bash main.sh")
              sys.exit()


localtime = time.asctime(time.localtime(time.time()))
IPITLY = """http://194.184.218.106:80
 http://109.239.247.151:5000
 http://79.5.248.181:80
 http://195.31.81.138:80
 http://213.182.91.27:8082
 http://91.143.192.75:80
 http://79.13.24.130:80
 http://95.252.207.172:80
 http://79.41.121.165:80
 http://188.217.174.162:8080
 http://2.192.135.163:8080
 http://2.193.128.163:90
 http://2.193.128.163:91
 http://87.13.83.166:80
 http://82.60.41.166:60001
 http://82.61.212.165:90
 http://89.21.198.165:60001
 http://95.255.33.169:50000
 http://79.27.160.156:80
 http://62.94.217.162:80
 http://79.44.140.158:80
 http://89.107.104.141:8082
 http://78.134.18.148:80
 http://79.33.250.155:80
 http://79.35.70.150:80
 http://80.117.209.146:8081
 http://213.45.244.146:60001
 http://37.101.28.143:60001
 http://134.90.254.142:60001
 http://79.20.106.94:81
 http://79.37.95.137:90
 http://79.37.95.137:91
 http://83.224.128.124:80
 http://82.49.24.134:1024
 http://79.46.78.127:80
 http://2.194.225.136:8080
 http://62.11.245.134:60001
 http://62.211.81.119:8082
 http://5.157.105.106:80
 http://2.192.228.118:8080
 http://87.3.154.117:89
 http://87.4.139.79:8888
 http://151.65.245.77:80
 http://78.134.115.75:5000
 http://128.116.233.73:9000
 http://151.56.39.71:60001
 http://87.5.195.73:90
 http://79.50.47.67:84
 http://5.157.108.66:84
 http://5.157.108.66:82
 http://5.157.108.66:83
 http://151.97.132.61:8080
 http://62.94.90.51:81
 http://82.54.76.8:8082
 http://80.116.178.177:82
 http://194.116.8.10:83
 http://194.116.8.10:84
 http://194.116.8.10:86
 http://194.116.8.10:85
 http://194.116.8.10:89
 http://37.247.87.21:80
 http://79.31.26.22:60001
 http://95.254.108.5:8080
 http://109.117.196.220:80
 http://109.117.159.213:85
 http://93.48.236.215:60001
 http://77.32.73.207:80
 http://79.49.58.196:80
 http://151.42.204.178:80
 http://78.134.44.194:82
 http://78.134.44.194:81
 http://78.134.44.194:83
 http://93.49.2.196:8081
 http://93.49.2.196:8083
 http://93.49.2.196:8082
 http://93.49.2.196:8080
 http://93.49.2.196:8084
 http://2.230.196.171:60001
 http://80.181.99.120:8083
 http://80.181.99.120:8081
 http://159.255.152.116:60001
 http://5.94.201.90:60001
 http://185.9.151.99:8081
 http://79.51.208.66:82
 http://188.12.182.58:81
 http://2.224.143.62:60001
 http://195.254.245.37:82
 http://109.116.122.33:3000
 http://2.115.227.30:81
 http://93.51.77.29:80
 http://78.134.70.26:8080
 http://82.143.33.187:60001
 http://82.58.161.193:90
 http://82.62.98.148:90
 http://82.62.98.148:91
 http://194.116.8.136:83
 http://88.149.137.113:84
 http://188.14.157.66:80
 http://93.45.124.25:8888
 http://79.59.190.14:82
 http://79.59.190.14:81
 http://95.246.129.18:8082
 http://79.59.190.14:84
 http://87.26.188.210:3000
 http://188.13.69.205:81
 http://87.26.188.210:2000
 http://93.56.204.213:60001
 http://78.4.42.214:8080
 http://79.2.219.198:10000
 http://79.8.143.171:80
 http://88.202.119.149:83
 http://128.116.151.151:80
 http://185.37.205.130:80
 http://2.236.250.107:80
 http://93.56.119.30:8080
 http://188.217.189.19:60001
 http://31.196.1.214:84
 http://2.38.209.213:60001
 http://93.56.204.213:80
 http://88.36.179.194:8082
 http://83.211.37.161:81
 http://95.253.40.130:80
 http://217.133.29.142:80
 http://188.152.36.126:80
 http://93.48.229.81:60001
 http://88.61.54.9:8081
 http://188.11.27.179:80
 http://185.135.94.87:80
 http://93.70.236.56:85
 http://5.94.112.60:60001
 http://2.39.103.182:8080
http://79.11.31.7:8090
 http://95.255.183.164:8080
 http://195.103.108.145:82
 http://195.103.108.145:83
 http://195.103.108.145:81
 http://195.103.108.145:85
 http://195.103.108.145:84
 http://93.39.91.135:5000
 http://94.81.229.117:81
 http://94.81.229.117:82
 http://94.81.229.117:85
 http://109.115.124.92:81
 http://2.34.188.200:80
 http://85.41.46.10:60001
 http://62.69.134.221:82
 http://217.133.85.197:81
 http://93.70.58.198:60001
 http://95.210.248.83:8081
 http://185.128.149.65:8082
 http://93.51.121.30:60001
 http://188.14.157.65:80
 http://31.14.184.209:88"""

IPISRL = """http://95.35.30.163:80
 http://82.80.63.83:80
 http://31.168.150.154:82
 http://80.178.208.109:81
 http://62.219.135.70:1000                                                                            http://79.176.229.162:60001
 http://85.64.1.162:60001
 http://109.66.36.75:60001
 http://109.66.28.144:60001
 http://109.64.209.135:60001
 http://109.64.242.135:60001
 http://77.139.239.76:91
 http://87.71.60.56:60001
 http://95.35.31.41:80
 http://109.65.164.4:60001
 http://77.139.177.208:60001
 http://87.71.46.188:60001
 http://84.108.60.146:60001
 http://85.65.17.58:60001
 http://95.215.131.163:60001
 http://77.139.64.140:60001
 http://77.139.82.67:60001
 http://82.102.164.18:80
 http://176.229.131.145:60001
 http://141.226.239.119:8080
 http://176.12.130.194:80
 http://85.64.51.104:60001
 http://77.138.77.207:90
 http://77.137.176.190:80
 http://176.229.254.185:80
 http://176.12.133.181:80
 http://77.139.179.87:60001
 http://176.12.134.50:80
 http://87.68.95.27:60001
 http://188.120.159.200:90
 http://84.228.91.179:91
 http://5.29.77.149:85
 http://81.218.193.89:86
 http://77.139.183.213:60001
 http://5.28.140.97:90
 http://84.109.176.78:60001
 http://89.208.3.29:90
 http://77.139.202.44:60001
 http://82.81.78.30:60001
 http://176.12.134.15:80
 http://84.108.174.139:60001
 http://89.208.3.29:91
 http://109.253.5.192:80
 http://85.64.88.49:60001
 http://84.108.216.73:90
 http://84.108.216.73:91
 http://147.234.39.35:80
http://84.109.213.143:60001
 http://82.81.248.6:8080
 http://81.218.205.132:90
 http://37.142.30.101:90                                                                              http://37.142.30.101:91
 http://81.218.136.68:88
 http://213.57.166.68:80
 http://176.12.134.26:80
 http://77.139.16.211:80
 http://62.90.155.203:88
 http://81.218.157.139:91
 http://84.108.38.155:60001
 http://31.168.223.53:80
 http://85.64.87.206:60001
 http://82.81.200.39:60001
 http://31.154.209.26:90
 http://62.219.162.19:90
 http://82.166.131.0:60001
 http://82.81.2.221:90
 http://194.90.217.12:90
 http://93.175.63.136:60001
 http://31.168.62.120:60001
 http://62.219.237.201:60001
 http://185.108.80.153:90
 http://82.81.57.92:60001
 http://81.218.180.195:88
 http://199.203.11.115:90
 http://80.250.155.174:80
 http://80.250.155.242:80
 http://95.35.30.170:80
 http://176.12.131.175:80"""

IPCHN = """http://183.233.177.152:85
 http://218.17.185.106:91
 http://61.161.192.107:2000
 http://183.167.236.6:60001
 http://183.196.235.201:60001
 http://36.22.255.159:60001
 http://221.208.231.161:60001
 http://39.88.0.162:60001
 http://113.231.201.161:60001
 http://61.176.225.162:60001
 http://110.7.244.149:60001
 http://110.255.252.62:60001
 http://120.11.58.67:60001
 http://111.59.175.2:91
 http://101.26.49.47:60001
 http://119.250.64.39:60001
 http://114.135.102.7:90
 http://119.113.190.188:8081
 http://120.209.226.166:86
 http://117.141.81.123:90
 http://111.40.95.128:60001
 http://27.220.99.89:60001
 http://111.59.77.58:90
 http://111.59.253.30:90
 http://114.248.239.103:60001
 http://120.194.76.140:90
 http://111.59.161.62:90
 http://39.165.19.47:91
 http://111.59.87.29:90
 http://111.59.155.210:90
 http://111.59.119.137:90
 http://111.12.69.70:90
 http://111.59.222.44:91
 http://117.158.166.212:60001
 http://183.239.73.179:60001
 http://221.2.161.103:81
 http://117.141.81.25:90
 http://219.159.108.124:90
 http://60.10.63.45:90
 http://117.159.249.17:91
 http://111.59.215.3:91
 http://117.141.32.2:90
 http://58.49.40.214:88
 http://183.249.29.198:60001
 http://219.159.253.49:90
 http://116.131.169.162:90
 http://116.131.169.166:90
 http://113.195.92.116:91
 http://116.132.48.46:91
 http://120.238.131.217:60001
 http://113.12.75.148:91
 http://39.165.18.146:91
 http://218.77.107.56:91
 http://117.146.169.2:90
 http://39.165.22.15:91
http://58.48.184.198:88
 http://117.159.86.163:91
 http://112.80.25.114:5000
 http://117.156.114.71:90
 http://218.31.200.102:90
 http://111.62.24.60:91
 http://111.12.121.55:91
 http://111.59.94.51:90
 http://218.65.34.152:91
 http://218.69.22.142:90
 http://61.48.20.118:80
 http://58.49.205.67:88
 http://58.48.162.34:88
 http://39.165.18.24:91
 http://117.172.168.132:8000
 http://218.64.218.73:91
 http://112.14.29.67:60001
 http://117.141.209.25:91
 http://125.35.228.18:91
 http://202.103.203.143:81
 http://61.49.113.150:8090                                                                            http://60.8.246.162:60001"""

IPFRNC = """http://80.14.150.52:88
 http://82.127.163.2:88
 http://80.15.7.114:88
 http://82.127.180.180:88
 http://90.108.44.160:80
 http://83.112.252.159:8080
 http://92.158.253.159:80
 http://81.49.184.157:80
 http://2.8.19.149:80
 http://86.248.45.148:80
 http://86.248.45.148:81
 http://86.199.8.152:1024
 http://93.16.94.144:80
 http://92.141.107.135:80
 http://83.193.198.148:80
 http://78.125.48.138:60001
 http://86.233.215.147:8080
 http://90.3.227.133:8080
 http://78.207.28.119:8082
 http://92.149.84.89:81
 http://86.236.120.91:8080
 http://90.119.152.86:80
 http://83.193.13.63:8081
 http://78.125.203.79:60001
 http://90.118.235.65:8082
 http://86.196.235.60:8083
 http://86.212.96.61:82
 http://90.17.22.27:80
 http://86.250.156.48:82
 http://93.24.192.179:8090
 http://92.138.81.216:8080
 http://86.236.45.21:80
 http://86.227.105.7:85
 http://82.66.110.175:8888
 http://90.65.2.0:8001
 http://90.120.55.177:8080
 http://83.205.183.187:80
 http://90.0.194.156:8081
 http://176.141.167.156:60001
 http://90.90.21.159:8082
 http://90.104.87.151:8080
 http://90.49.80.137:80
 http://86.246.49.128:80
 http://2.3.207.128:8081
 http://86.236.149.110:8081
 http://83.197.246.90:8081
 http://78.115.3.44:60001
 http://86.211.153.93:8081
 http://86.208.246.96:8081
 http://90.66.203.70:8081
 http://78.228.31.60:8080
 http://2.7.199.57:8084
 http://5.51.206.54:81
 http://90.52.97.36:80
 http://90.17.66.46:8083
 http://80.14.198.34:82
 http://90.24.119.25:8080
 http://82.121.7.208:81
 http://86.196.167.194:1024
 http://81.53.17.153:8083
 http://5.183.214.127:81
 http://82.64.148.115:88
 http://86.192.199.110:10000
 http://88.162.143.102:60001
 http://77.135.210.109:80
http://80.14.67.36:80
 http://79.83.98.28:60001
 http://81.250.209.4:8888
 http://217.128.43.5:81
 http://80.11.165.166:80
 http://86.237.35.166:83
 http://86.237.35.166:85
 http://86.237.35.166:82
 http://86.237.35.166:84
 http://176.154.170.73:60001
 http://91.172.255.65:8080
 http://82.64.197.54:80
 http://77.141.18.15:8080
 http://80.11.62.20:1024
 http://109.219.157.181:8081
 http://77.207.7.156:8081
 http://217.128.94.112:8082
 http://82.127.249.27:8000
 http://78.124.33.19:83
 http://78.124.33.19:81
 http://217.175.186.179:80
 http://176.145.222.175:60001
 http://5.50.42.157:80
 http://176.169.102.145:81
 http://82.64.90.142:1024
 http://82.120.0.72:80
 http://88.168.92.48:82
 http://78.127.117.214:60001
 http://83.193.211.152:50001
 http://178.238.4.121:8084
 http://178.238.4.121:8083
 http://176.151.189.201:8082
 http://88.171.48.10:8080
 http://77.193.208.216:80
 http://90.63.255.188:81"""

IPJPN = """http://202.245.13.80:80
 http://220.254.147.41:80
 http://210.128.188.40:80
 http://202.237.132.50:80
 http://211.1.102.182:80
 http://146.160.66.75:80
 http://114.149.84.158:80
 http://121.95.66.162:80
 http://115.162.246.129:60001
 http://61.115.74.162:80
 http://114.162.168.150:60001
 http://153.217.157.115:80
 http://126.162.179.156:81
 http://126.170.172.156:50001
 http://60.34.167.158:83
 http://153.234.79.160:50000
 http://153.234.79.160:80
 http://101.141.39.162:84
 http://153.186.195.164:81
 http://133.175.152.150:8080
 http://122.20.106.144:50001
 http://60.38.143.141:8081
 http://121.119.67.150:8090
 http://114.159.27.150:50001
 http://157.101.146.144:50000
 http://180.40.229.155:50001
 http://202.95.43.81:8001
 http://133.142.31.150:80
 http://210.165.102.137:80
 http://118.6.198.142:60001
 http://101.1.193.152:80
 http://111.89.246.143:80
 http://146.99.73.144:85
 http://146.99.73.144:86
 http://114.176.80.132:83
 http://175.28.186.147:81
 http://118.4.122.127:8081
 http://118.4.122.127:8080
 http://58.138.39.94:80
 http://160.13.181.139:50001                                                                          http://182.164.28.132:60001
 http://114.182.62.132:60001
 http://101.141.70.132:60001
 http://175.28.251.139:60001
 http://119.240.13.136:80
 http://126.162.171.136:50001
 http://218.221.5.132:50000
 http://180.16.199.135:80
 http://125.174.129.127:50001
 http://146.99.238.118:8080
 http://114.186.68.117:60001
 http://220.98.95.120:80
http://153.144.192.118:80
 http://119.241.220.117:81
 http://124.86.2.88:80
 http://61.125.8.39:80
 http://153.229.194.116:80
 http://203.136.160.116:50000
 http://203.136.160.116:50001
 http://133.159.189.105:80
 http://125.192.219.38:60001
 http://210.156.169.88:8082
 http://114.176.47.79:50001
 http://218.46.203.86:8080
 http://211.128.48.79:60001
 http://183.76.165.79:80
 http://126.19.186.81:80
 http://126.130.63.73:60001
 http://210.165.244.66:80
 http://203.168.64.67:50000
 http://220.107.100.72:8080
 http://153.209.152.62:5000
 http://157.101.130.77:50000
 http://113.20.240.72:8080
 http://153.164.204.2:8082
 http://153.142.251.61:8081
 http://153.164.204.2:8081
 http://211.132.51.61:85
 http://211.132.51.61:86
 http://180.31.40.62:80
 http://118.2.28.56:50001
 http://153.158.203.61:50000
 http://114.173.217.51:8001
 http://153.229.88.60:81
 http://121.1.180.49:5000
 http://60.56.214.8:80
 http://123.226.96.59:8001
 http://123.226.96.59:8000
 http://125.30.176.41:50001
 http://180.5.1.42:60001"""

IPIND = """\033[1;31mhttp://192.135.76.230:80
http://66.188.76.157:8080
 http://184.60.2.160:80
 http://108.77.13.163:8080
 http://66.225.67.156:8888
 http://73.120.172.157:80
 http://173.184.66.160:60001
 http://108.45.86.160:60001
 http://68.55.208.164:60001
 http://72.92.228.162:60001
 http://69.122.39.163:60001
 http://74.192.241.162:60001
 http://63.153.111.158:8090
 http://162.247.60.158:8080
 http://65.35.46.163:80
 http://96.67.147.157:1024
 http://96.232.246.162:5000
 http://23.247.248.162:8888
 http://74.77.247.129:1024
 http://166.149.241.155:8000
 http://67.140.159.144:60001
 http://47.6.138.144:60001
 http://73.51.160.143:60001
 http://23.88.187.155:60001
 http://69.137.12.153:8081
 http://100.37.85.141:80
 http://70.89.144.137:8001
 http://47.145.69.94:8084
 http://76.28.82.132:8001
 http://98.204.130.120:8080
 http://73.200.255.139:91
 http://70.100.14.135:81
 http://204.116.229.74:60001
 http://73.119.36.134:60001
 http://24.12.128.126:60001
 http://24.217.12.136:60001
 http://173.53.1.135:80
 http://70.184.6.137:81
 http://23.247.248.131:8888
 http://99.103.244.119:84
 http://192.173.155.111:80
 http://98.151.225.119:1024
 http://162.191.146.123:81
 http://73.115.74.118:8001
 http://71.223.190.74:60001
 http://73.49.43.39:60001
 http://35.135.178.123:80
 http://97.80.64.120:81
 http://23.247.248.118:8888
http://23.247.248.123:8888
 http://23.247.248.116:8888
 http://23.247.248.52:8888
 http://66.128.166.74:85
 http://99.85.27.87:81
 http://96.93.176.94:8082
 http://96.93.176.94:8083
 http://100.40.27.88:8084
 http://24.168.235.94:80
 http://162.191.105.87:8081
 http://71.38.173.86:8001
 http://24.197.119.86:60001
 http://173.185.200.90:80
 http://98.224.235.79:60001
 http://70.183.112.86:60001
 http://71.57.128.20:80
 http://172.222.200.75:80
 http://98.47.42.73:1024
 http://70.184.69.67:8000
 http://72.202.102.72:1024
 http://64.90.70.68:50001
 http://50.44.248.61:8082
 http://143.55.52.62:81
 http://24.20.61.62:60001
 http://73.24.160.61:60001
 http://45.51.17.62:60001
 http://97.114.196.67:80
 http://100.7.11.56:60001
 http://74.83.96.68:9000
 http://24.180.123.50:8001
 http://98.110.161.49:60001
 http://24.255.245.49:60001
 http://24.49.220.8:60001
 http://100.0.197.49:8084
 http://24.126.148.51:8084
 http://166.252.52.49:83
 http://216.14.224.48:80
 http://100.0.27.40:8888
 http://216.71.29.43:80
 http://72.15.84.51:60001
 http://67.219.168.8:60001
 http://100.14.76.48:60001
 http://76.189.161.46:8080
 http://100.2.192.179:8001
 http://68.170.125.44:50000
 http://64.19.81.38:83
 http://98.45.115.8:8080
 http://65.61.83.8:8080
 http://162.191.221.9:81
 http://162.191.221.9:82
 http://172.114.50.38:60001
 http://47.6.51.26:80
 http://74.102.184.9:60001
 http://68.198.250.9:5000
"""
print (logo)
print ("\033[1;93m==================================")
print ("Creator : AmmarBN")
print ("penemu ip : Ariffb,Rendi Noober")
print ("\033[1;95mWaktu\033[1;91m:\033[1;93m"),localtime
print "(1) Indonesia"
print "(2) Japan"
print "(3) France"
print "(4) China"
print "(5) Israel"
print "(6) Italy"
print "(7) exit"
print ("===========================================")
print
pilih = input("Options : ")
if pilih == 1:
        print ("Loading......")
        time.sleep(10)
        print (IPIND)
if pilih == 2:
        print ("Loading......")
        time.sleep(10)
        print (IPJPN)
if pilih == 3:
        print ("Loading......")
        time.sleep(10)
        print (IPFRNC)
if pilih == 4:
        print ("Loading......")
        time.sleep(10)
        print (IPCHN)
if pilih == 5:
        print ("Loading......")
        time.sleep(10)
        print (IPISRL)
if pilih == 6:
        print ("Loading......")
        time.sleep(10)
        print (IPITLY)
if pilih == 6:
	print ("TerimaKasih Telah Menggunakan Tools Ini")
	time.sleep(3)
	
lagi()
