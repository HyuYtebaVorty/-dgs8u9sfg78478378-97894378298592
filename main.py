import telebot
from telebot import types
import random
from datetime import datetime
import requests
from dotenv import load_dotenv
import os


load_dotenv()
API_TOKEN = (os.getenv("TOKEN"))
bot = telebot.TeleBot(API_TOKEN)


used_commands = {}

combinations = [
    "161.35.49.235:22 root:Passw@rd",
    "139.91.130.117:22 admin:admin",
    "111.21.232.126:22 root:root",
    "34.126.69.239:22 daemon:daemon",
    "198.13.38.7:22 root:root",
    "174.77.224.21:22 operator:operator",
    "139.99.246.194:22 root:Passw@rd",
    "195.211.98.224:22 root:Passw@rd",
    "77.233.25.176:22 admin:admin",
    "125.32.178.25:22 admin:admin",
    "201.210.129.208:22 admin:admin",
    "5.78.65.121:22 root:root",
    "192.46.229.129:22 root:Passw@rd",
    "166.195.49.56:22 admin:admin",
    "58.69.57.251:22 admin:1234",
    "73.180.89.15:22 daemon:daemon",
    "45.228.20.185:22 admin:admin",
    "149.248.56.211:22 root:root",
    "45.76.131.85:22 root:root",
    "103.242.57.219:22 root:root",
    "153.143.238.147:22 admin:admin",
    "218.22.252.75:22 root:root",
    "209.193.27.121:22 cisco:cisco",
    "66.46.166.210:22 maintainer:admin",
    "45.77.234.84:22 root:root",
    "45.56.79.78:22 root:root",
    "66.230.114.130:22 service: smile",
    "124.152.131.149:22 admin:admin",
    "45.36.27.198:22 root:GM8182",
    "103.113.26.36:22 root:1234",
    "47.122.62.117:22 root:root",
    "70.169.112.226:22 root:Passw@rd",
    "72.205.20.4:22 root:alpine",
    "184.190.47.163:22 root:Passw@rd",
    "47.108.138.102:22 root:root",
    "5.144.133.132:22 root:Passw@rd",
    "45.239.45.61:22 root:Passw@rd",
    "141.11.89.228:22 root:Passw@rd",
    "136.244.119.173:22 root:root",
    "193.104.84.67:22 admin:admin",
    "209.183.10.169:22 default:OxhlwSG8",
    "176.122.123.98:22 root:root",
    "103.204.172.136:22 admin:admin",
    "8.142.14.233:22 root:root",
    "14.98.74.33:22 root:root",
    "178.254.23.228:22 root:alpine",
    "1.164.33.177:22 root:root",
    "117.72.74.191:22 root:root",
    "98.62.15.62:22 root:root",
    "220.94.82.231:22 admin:admin",
    "142.171.26.166:22 root:root",
    "51.195.220.42:22 root:Passw@rd",
    "122.185.33.234:22 root:root",
    "209.193.26.25:22 root:Menara",
    "46.247.112.219:22 support:support",
    "111.8.62.110:22 root:root",
    "181.215.208.253:22 root:Passw@rd",
    "52.251.89.168:22 root:root",
    "14.195.192.185:22 root:root",
    "107.174.176.18:22 root:Passw@rd",
    "45.79.95.198:22 root:root",
    "103.170.233.253:22 admin:admin",
    "146.59.91.216:22 root:Passw@rd",
    "104.145.234.91:22 root:Passw@rd",
    "111.16.55.79:22 root:root",
    "111.53.104.232:22 root:root",
    "103.216.223.36:22 root:Passw@rd",
    "116.63.130.30:22 root:root",
    "46.38.231.51:22 root:Passw@rd",
    "47.96.234.130:22 root:root",
    "104.234.24.133:22 root:Passw@rd",
    "139.84.166.211:22 root:root",
    "114.251.96.100:22 root:root",
    "195.158.82.221:22 admin:admin",
    "82.118.235.50:22 admin:admin",
    "139.91.130.115:22 root:root",
    "47.122.60.157:22 root:root",
    "202.62.80.58:22 admin:admin",
    "47.253.105.175:22 root:root",
    "35.229.214.237:22 root:root",
    "50.35.94.75:22 root:root",
    "12.18.235.142:22 operator:operator",
    "46.38.231.63:22 root:Passw@rd",
    "122.187.230.194:22 admin:admin",
    "113.108.59.146:22 admin:admin",
    "119.3.149.225:22 root:Passw@rd",
    "216.126.80.23:22 root:alpine",
    "119.8.11.131:22 root:alpine",
    "193.214.158.52:22 root:root",
    "46.38.231.59:22 daemon:daemon",
    "14.99.19.81:22 root:root",
    "81.161.246.64:22 root:Passw@rd",
    "69.164.213.137:22 root:root",
    "45.32.136.140:22 root:root",
    "185.16.61.26:22 root:alpine",
    "148.67.210.89:22 admin:admin",
    "172.232.70.68:22 root:root",
    "47.98.134.232:22 root:root",
    "176.32.195.57:22 root:Passw@rd",
    "139.9.140.255:22 root:root",
    "124.105.27.248:22 user:user",
    "194.36.90.164:22 root:root",
    "207.135.234.248:22 root:alpine",
    "115.147.53.115:22 admin:1234",
    "195.226.142.123:22 admin:admin",
    "216.67.79.101:22 root:1qazxsw2",
    "212.101.137.64:22 admin:1988",
    "20.48.180.58:22 root:root",
    "139.91.130.149:22 root:root",
    "46.183.184.119:22 root:Passw@rd",
    "212.101.137.10:22 admin:1988",
    "109.122.74.85:22 admin:admin",
    "74.63.247.217:22 root:Passw@rd",
    "5.8.71.164:22 root:Passw@rd",
    "14.140.246.84:22 root:root",
    "49.249.40.209:22 root:root",
    "120.77.68.2:22 root:root",
    "122.54.187.83:22 admin:1234",
    "50.116.47.203:22 admin:admin",
    "206.207.71.238:22 root:root",
    "184.178.35.247:22 root:Passw@rd",
    "63.144.23.99:22 operator:operator",
    "172.104.34.63:22 root:alpine",
    "210.226.80.204:22 root:root",
    "122.54.133.94:22 user:user",
    "5.253.19.134:22 root:Passw@rd",
    "122.52.149.103:22 admin:1234",
    "151.236.24.85:22 root:root",
    "78.36.201.239:22 root:root",
    "178.62.196.4:22 root:root",
    "153.158.255.112:22 admin:admin",
    "167.172.41.71:22 root:root",
    "182.43.17.93:22 root:root",
    "139.91.130.111:22 root:root",
    "184.184.247.199:22 root:Passw@rd",
    "98.153.190.34:22 operator:operator",
    "114.143.61.218:22 root:root",
    "96.125.135.182:22 root:root",
    "111.90.148.180:22 admin:admin",
    "76.80.87.202:22 operator:operator",
    "1.169.225.149:22 root:root",
    "14.98.51.182:22 root:root",
    "217.71.253.14:22 daemon:daemon",
    "93.171.141.81:22 root:root",
    "123.131.164.228:22 root:root",
    "111.93.58.218:22 root:root",
    "217.107.192.1:22 root:root",
    "37.0.12.23:22 root:Passw@rd",
    "39.100.95.30:22 root:root",
    "137.220.55.98:22 admin:admin",
    "216.67.82.163:22 root:root",
    "119.178.100.118:22 root:root",
    "185.70.187.53:22 daemon:daemon",
    "106.178.132.127:22 root:root",
    "38.34.77.189:22 admin:admin",
    "114.105.99.10:22 root:root",
    "138.197.163.224:22 root:Passw@rd",
    "123.7.14.94:22 root:root",
    "169.255.58.109:22 admin:admin",
    "8.209.64.208:22 root:root",
    "185.26.239.120:22 root:Passw@rd",
    "160.242.59.238:22 root:root",
    "78.141.230.187:22 root:root",
    "218.84.134.140:22 root:root",
    "84.73.80.35:22 root:root",
    "222.190.126.246:22 root:root",
    "121.52.219.42:22 root:root",
    "184.181.249.160:22 root:Passw@rd",
    "36.227.183.37:22 root:root",
    "122.54.187.82:22 admin:1234",
    "139.91.130.206:22 root:root"
]

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет бро, здесь ты можешь получить 1 бесплатный Дедик, просто введи команду /free Dedik")


@bot.message_handler(commands=['free'])
def issue_combination(message):
    command_parts = message.text.split()
    if len(command_parts) != 2 or command_parts[1].lower() != 'dedik':
        bot.reply_to(message, "Пиши /free Dedik")
        return

    username = message.from_user.username
    if username in used_commands:
        bot.reply_to(message, "Ля ты крыса!")
        return

    combination = random.choice(combinations)
    used_commands[username] = combination
    print(f"Дедик получил: @{username}: {combination},{current_time}")
#вебхук для обычных людей:
    webhook_url = "https://discord.com/api/webhooks/1310925671945474058/lsWi3A_W0UKnpoO6APKFtuvNj8NKyUuOsJOaju_DtwSKbzhelIuiBP9ZkXGEH67943il"
    requests.post(webhook_url, json={"content": f"@here Дедик получил: @{username}: ,{current_time}"})
#вебхук для админов
    webhook_url = "https://discord.com/api/webhooks/1310929050344231014/I1PqoTo2ri7iwgaNMWW3uMCOkUm2z_hKAxYc8CybyNOVE1WKZrNDDge0nO-UX5kttU9o"
    requests.post(webhook_url, json={"content": f"@here Дедик получил: @{username}: {combination},{current_time}"})



    bot.reply_to(message, f"Вход по ssh: {combination}")


bot.polling()

