from core.builtins import Bot
from core.component import on_command
from config import Config
import requests
import json
import subprocess
import redis
import random

redis_ = Config('redis').split(':')
db = redis.StrictRedis(host=redis_[0], port=int(redis_[1]), db=0, decode_responses=True)


def write(data: str):
    json_data = json.dumps(data)
    db.set(f"cave", json_data)


def read():
    data = db.get(f"cave")
    return data


cave = on_command('cave', alias={'hitokoto': 'cave hitokoto',
                                 'cow': 'cave cowsay'
                                 },
                  desc='回声洞', developers=['haoye_qwq'])


@cave.handle('hitokoto {一言}')
async def hitokoto(msg: Bot.MessageSession):
    url = 'https://v1.hitokoto.cn/'
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        json_dict = json.loads(content)
        yee = json_dict.get('hitokoto')
        frm = json_dict.get('from')
        who = json_dict.get('from_who')
        await msg.sendMessage(f"[{yee}]\n    ——{who}《{frm}》")
    else:
        await msg.sendMessage('请求失败')


@cave.handle('cowsay {哲学牛牛}')
async def cowsay(msg: Bot.MessageSession):
    result = subprocess.getoutput('fortune | cowsay')
    await msg.sendMessage(result.replace('Process finished with exit code 0', ''))

# @cave.handle('echo_cave add <sth> {添加回声洞}',
#              'echo_cave del <num> {删除回声洞}',
#              'echo_cave {显示回声洞}')
# async def ___(msg: Bot.MessageSession):
#     if 'add' in msg.parsed_msg:
#
# cq = await msg.asDisplay()
# cq = re.findall(r'^\[CQ:image,(\s\S)*\]', cq, re.I | re.M)


@cave.handle('{回声洞}')
async def ___():
    mode = ['hitokoto', 'cowsay']
    if random.choice(mode) == 'hitokoto':
        await hitokoto
    else:
        await cowsay

