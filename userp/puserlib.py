import json
import re
import aiohttp
import re
from bs4 import BeautifulSoup as bs
import os
from .killdd import ddk
from .hh import hh
from .hh17 import hh17
from os.path import abspath
from .tpg import tpg

async def get_data(url: str, fmt: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,timeout=aiohttp.ClientTimeout(total=20)) as req:
            if hasattr(req, fmt):
                return await getattr(req, fmt)()
            else:
                raise ValueError(f"NoSuchMethod: {fmt}")

async def PUser1(url, str3,ss,User,Gender,Registration):
    q = str3
    url2 = url+'/api.php?action=query&meta=allmessages&ammessages=mainpage&format=json'
    file2 = await get_data(url2,'json')
    try:
        Wikiname = file2['query']['allmessages'][0]['*']
    except Exception:
        Wikiname = 'Unknown'
    d= abspath('./assests/Favicon/'+ss+'/')
    if not os.path.exists(d):
        os.mkdir(d)
    ddd = abspath('./assests/Favicon/'+ss+'/Wiki.png')
    if not os.path.exists(ddd):
        from .dpng import dpng
        dpng(url,ss)
    url2 = url+'/UserProfile:'+q
    res = await get_data(url2,'text')
    soup = bs(res, 'html.parser')
    stats = soup.find('div', class_='section stats')
    point = soup.find('div', class_='score').text
    dd = stats.find_all('dd')
    for tag in dd:
        pass
    g = re.sub('User:', '', str3)
    tpg(favicon=abspath('./assests/Favicon/'+ss+'/Wiki.png'),wikiname=hh(Wikiname),\
        username=User,gender=Gender,registertime=Registration,\
        contributionwikis=ddk(str(dd[0])),createcount=ddk(str(dd[1])),\
        editcount=ddk(str(dd[2])),deletecount=ddk(str(dd[3])),patrolcount=ddk(str(dd[4])),\
        sitetop=ddk(str(dd[5])),globaltop=ddk(str(dd[6])),wikipoint=point)
async def PUser1ban(url, str3,ss,User,Gender,Registration,Blockedby,Blockedtimestamp,Blockexpiry,Blockreason):
    q = str3
    url2 = url+'/api.php?action=query&meta=allmessages&ammessages=mainpage&format=json'
    file2 = await get_data(url2,'json')
    try:
        Wikiname = file2['query']['allmessages'][0]['*']
    except Exception:
        Wikiname = 'Unknown'
    d=abspath('./assests/Favicon/'+ss+'/')
    if not os.path.exists(d):
        os.mkdir(d)
    ddd=abspath('./assests/Favicon/'+ss+'/Wiki.png')
    if not os.path.exists(ddd):
        from .dpng import dpng
        dpng(url,ss)
    url2 = url+'/UserProfile:'+q
    res = await get_data(url2,'text')
    soup = bs(res, 'html.parser')
    stats = soup.find('div', class_='section stats')
    point = soup.find('div', class_='score').text
    dd = stats.find_all('dd')
    for tag in dd:
        pass
    g = re.sub('User:', '', str3)
    tpg(favicon=abspath('./assests/Favicon/'+ss+'/Wiki.png'),wikiname=hh(Wikiname),username=User,\
        gender=Gender,registertime=Registration,contributionwikis=ddk(str(dd[0])),\
        createcount=ddk(str(dd[1])),editcount=ddk(str(dd[2])),deletecount=ddk(str(dd[3])),\
        patrolcount=ddk(str(dd[4])),sitetop=ddk(str(dd[5])),globaltop=ddk(str(dd[6])),\
        wikipoint=point,blockbyuser=Blockedby,blocktimestamp1=Blockedtimestamp,blocktimestamp2=Blockexpiry,\
        blockreason=hh17(Blockreason),bantype='Y')
async def PUser1bann(url, str3,ss,User,Gender,Registration,Blockedby,Blockedtimestamp,Blockexpiry):
    q = str3
    url2 = url+'/api.php?action=query&meta=allmessages&ammessages=mainpage&format=json'
    file2 = await get_data(url2,'json')
    try:
        Wikiname = file2['query']['allmessages'][0]['*']
    except Exception:
        Wikiname = 'Unknown'
    d=abspath('./assests/Favicon/'+ss+'/')
    if not os.path.exists(d):
        os.mkdir(d)
    ddd = abspath('./assests/Favicon/'+ss+'/Wiki.png')
    if not os.path.exists(ddd):
        from .dpng import dpng
        dpng(url,ss)
    url2 = url+'/UserProfile:'+q
    res = await get_data(url2,'text')
    soup = bs(res, 'html.parser')
    stats = soup.find('div', class_='section stats')
    point = soup.find('div', class_='score').text
    dd = stats.find_all('dd')
    for tag in dd:
        pass
    g = re.sub('User:', '', str3)
    tpg(favicon=abspath('./assests/Favicon/'+ss+'/Wiki.png'),wikiname=hh(Wikiname),username=User,\
        gender=Gender,registertime=Registration,contributionwikis=ddk(str(dd[0])),\
        createcount=ddk(str(dd[1])),editcount=ddk(str(dd[2])),deletecount=ddk(str(dd[3])),\
        patrolcount=ddk(str(dd[4])),sitetop=ddk(str(dd[5])),globaltop=ddk(str(dd[6])),\
        wikipoint=point,blockbyuser=Blockedby,blocktimestamp1=Blockedtimestamp,blocktimestamp2=Blockexpiry,\
        bantype='YN')