# -*- coding: utf-8 -*-

import TBA
from TBA.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, ctypes, urllib, urllib2, urllib3, wikipedia, tempfile
from bs4 import BeautifulSoup
from urllib import urlopen
import requests
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

adhi1 = TBA.LINE()
#kr1.login(qr=True)
adhi1.login(token="Ep7O9zheBCexGx69asT9.TnGPW4QBZeVXjFVsPbzXgq.ZfxfY+9MTiDH/aiRpZYhYL5d0ke1Wb6lVn3MKuDVumI=")
adhi1.loginResult()

adhi2 = TBA.LINE()
#kr2.login(qr=True)
adhi2.login(token="Ep4QQL9B9aM1EJxQpmf2.nMPTh/y4WGrFNUltavunCG.Ko08m0whxzijbquT5kRMgu3BmhveXz6MleapSQNadl8=")
adhi2.loginResult()

adhi3 = TBA.LINE()
#kr3.login(qr=True)
adhi3.login(token="EpUW9XJ5S4CZIDAIfGQ8.WhcCLZJQLjnFnQgxHWc6ga.N3JiRgSeYFNAb7rD97JxabSg9cGUd1AarYgotNGWFl0=")
adhi3.loginResult()

adhi4 = TBA.LINE()
#kr4.login(qr=True)
adhi4.login(token="EpIaJWcVZziN0sgWQx56.c6Qowq+EGzzmeMzhC+J3XG.2ZLlsnJgfovG/HQVoNOQMsxzoIYxfcXSrj6oQgLSYO0=")
adhi4.loginResult()

adhi5 = TBA.LINE()
#kr5.login(qr=True)
adhi5.login(token="Ep5f3ptphWLlL4erpa7d.VnulOwe8gWeSQbKjn6JvVq.7vo7p7RBpo52AkuA/AUCWZwRsQqodWUI4j5AMXXDVFo=")
adhi5.loginResult()

#adhi6 = KRIS.LINE()
#adhi6.login(qr=True)
#adhi6.login(token="")#satpam
#adhi6.loginResult()


print "╔══════BABANG-SUKSESs═════"
reload(sys)
sys.setdefaultencoding('utf-8')

helpmsg ="""
 Owner :(􀰂􀰂􀠁􀠁􀠁 ༺BANG-ADHI༻ (2 stars))
line://ti/p/~jkp4678
═════════════
╔════════════
Help2\3
Youtube
Yt
Music
google (text)
playstore (text)
instagram (username)
wikipedia (text)
image (text)
lirik (text)
Kiss
Gcreator
idline (text)
time
Salam1/Salam2
Creator
Kelahiran
Kalender/waktu
say
Gift8
Gift/Gift1/2/3
reinvite
time
Kapan
Apakah
Tuh
Absen
runtime
speed
Anu/crot (Tagall)
mode on/off
protect on/off
qr on/off
invite on/off
cancel on/off
Intip on/off (Lurking)
ciduk/intip (Lurkers)
Setimage: (link)
Papimage
Setvideo: (link)
Papvideo
mymid
Getcover @
Myname
Mybot
Mybio
Mypict
Myvid
Urlpict
Mycover
Urlcover
Getmid @
Getinfo @
Getbio @
Getname @
Getprofile @
Getcontact @
Getpict @
Getvid @
Picturl @
Getcover @
Coverurl @
Mycopy @
Mybackup
Testext: (text)
Steal contact
Auto add
Spam add:@
Spam:@
spam txt/on/jml
Micadd @
Micdel @
Miclist
Mimic target @
Mimic on/off
╚═════════════"""

helpset ="""
╠═════════════
Owner :(􀰂􀰂􀠁􀠁􀠁 ༺BANG-ADHI༻ (2 stars))
╔════════════
Gurl
Grup cancel:
share on/off
foto on/off
Datang on/off
Keluar on/off
Tag on/off
Tag2 on/off
contact on/off
autojoin on/off
autoleave on/off
autoadd on/off
Sider on/off
like friend
Like me
link on/off
simisimi on/off
Autoread on/off
update
Pesan set:
Coment Set:
Comment on/off
Com
Com hapus Bl
Com Bl cek
jam on/off
Jam say:
╚═════════════"""

helpgrup ="""
╠═════════════
 Owner :(􀰂􀰂􀠁􀠁􀠁 ༺BANG-ADHI༻ (2 stars))
╔════════════
Link on
Url
Cancel
Gcreator
Kick @
Kiss @
Gname:
Gbroadcast:
Cbroadcast:
Glist
Flist
Blacklist
Ban @
Unban @
Clearban
friendpp:
Checkmid:
Checkid:
Memlist
Finfo:
Fpict:
Flistmid
Blocklist
Gclist
Glistmid
Gcimage:
Gcname
Gcid
Gcinfo:
infogrup
grup id
gcancel
Sita join/. (manggil bot)
Sita Balik
Sita out
Getgrup image
Urlgrup image
Set
Ban:
Unban:
Ban:on
Unban:on
Banlist
Contact ban
Midban
scan blacklist
Bcast
║Translate-id
║Translate-en
║Translate-ar
║Translate-jp
║Translate-ko
║Id@en
║En@id
║Id@jp
║Jp@id
║Id@th
║Th@id
║Id@ar
║Ar@id
║Id@ko
║Ko@id
║Say-id
║Say-en
║Say-jp
║Say-ar
║Say-ko
║welcome
║Dl (Nk)
║ifconfig
║system
║kernel
║cpu
║Restart
║Turn off
║Speed\Sp
║crash
║crash kontak @
║Attack
║Spamcontact @
║Sbot
║Restart
║Invite/Undang/Jepit
║Tbot:(txt)
║Tbot1/2/3/4/5: 
║TBio: (txt)
║Gcreator:inv
║Gcreator:kick
║Ts spamtag @
║muach
║list gc
║list gc2
║Rasita
║T bye
║T sita
║#Sita
║T spin
║Tes
║Salam3
╚═════════════
════=Babang-Adhi═╠══
line://ti/p/~jkp4678
Tanks For You Guys
╚═════════════"""

KAC=[adhi1,adhi2,adhi3,adhi4,adhi5]
mid = adhi1.getProfile().mid
["ub4d829c38a9bcc4bf125fbd2a4167119"]
mid2 = adhi2.getProfile().mid
["u366a6d1fe638c2045f9ee2d301550d72"]
mid3 = adhi3.getProfile().mid
["uc0709c9738ea94935f36a1978700ba18"]
mid4 = adhi4.getProfile().mid
["u0baa8e590fde81964c12664773f8f7c6"]
mid5 = adhi5.getProfile().mid
["ubcd50ba1613c1b012ca8190937a8d5bd"]
#mid6 = kr6.getProfile().mid

Bots=[mid,mid2,mid3,mid4,mid5]
owner=["ub4d829c38a9bcc4bf125fbd2a4167119","u366a6d1fe638c2045f9ee2d301550d72"]
admin=["ub4d829c38a9bcc4bf125fbd2a4167119","u366a6d1fe638c2045f9ee2d301550d72",mid,mid2,mid3,mid4,mid5]

wait = {
    'likeOn':False,
    'alwayRead':False,
    'detectMention':False, 
    'potoMention':False,
    'kickMention':False,
    'steal':True,
    'pap':{},
    'invite':{},
    'spam':{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":5},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"""👉╠════════Thanks For Add kak═╠════════,,""",
    "lang":"JP",
    "comment":"👉╠════════=Rasita═╠════════",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cNames1":"",
    "cNames2":"",
    "cNames3":"",
    "cNames4":"",
    "cNames5":"",
    "Wc":False,
    "Lv":False,
    "MENTION":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Sider":{},
    "protect":True,
    "cancelprotect":True,
    "inviteprotect":True,
    "linkprotect":True,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = adhi1.getProfile()
mybackup = adhi1.getProfile()
contact = adhi2.getProfile()
mybackup = adhi2.getProfile()
contact = adhi3.getProfile()
mybackup = adhi3.getProfile()
contact = adhi4.getProfile()
mybackup = adhi4.getProfile()
contact = adhi5.getProfile()
mybackup = adhi5.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus


mulai = time.time()

agent = {'User-Agent' : "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30)"}

def translate(to_translate, to_language="auto", language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':'Mozilla/5.0'}
    cari_hasil = 'class="t0">'
    request = urllib2.Request(url, headers=agent)
    page = urllib2.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

#def autolike():
#			for zx in range(0,100):
#				hasil = kr1.activity(limit=100)
#				if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#					try:
#						kr1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#						kr1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By TobyBots!!\nID LINE : line://ti/p/~tobyg74\nIG : instagram.com/tobygaming74")
#						print "DiLike"
#					except:
#							pass
#				else:
#						print "Sudah DiLike"
#			time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

#def autolike():
#    for zx in range(0,100):
#      hasil = kr1.activity(limit=100)
#      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
#        try:
#          kr1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
#          kr1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By✰ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰😊\n\n☆º°˚˚☆ tɛǟʍ ċʏɮɛʀ-ǟʀʍʏ ɮօt ✰°˚˚☆（＾ω＾）\nąµţ๏ℓɨЌ€ by Kris ⭐👈 »»» http://line.me/ti/p/GkwfNjoPDH «««")
#          print "Like"
#        except:
#          pass
#      else:
#          print "Already Liked"
#time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = adhi1.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendImage(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M_id = self.Talk.adhi1.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = adhi1.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n9§9" + Name
                wait2['ROM'][op.param1][op.param2] = "9§9" + Name
        else:
            pass
    except:
        pass

def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M_id = self.Talk.adhi1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }

        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        print r
        if r.status_code != 201:
            raise Exception('Upload audio failure.')


def sendAudioWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
            raise e
def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
         raise e

def sendVoice(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentPreview = None
        M_id = self._adhi1.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'voice_message',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload voice failure.')
        return True

def sendVideoWithURL(self, to_, url):
      path = 'pythonLines.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendVideo(to_, path)
      except Exception as e:
         raise e

def mention(to,nama):
    aa = ""
    bb = ""
    strt = int(12)
    akh = int(12)
    nm = nama
    #print nm
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "► @c \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "「Mention」\n"+bb
    msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    #print msg
    try:
         adhi1.sendMessage(msg)
    except Exception as error:
        print error
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={"MENTION":'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       adhi1.sendMessage(msg)
    except Exception as error:
       print error

def removeAllMessages(self, lastMessageId):
     return self._adhi1.removeAllMessages(0, lastMessageId)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True
     
def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait['autoAdd'] == True:
                adhi1.findAndAddContactsByMid(op.param1)
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    adhi1.sendText(op.param1,str(wait['message']))
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        adhi1.sendText(msg.to,text)
        if op.type == 13:
            print op.param3
            if op.param3 in mid:
                if op.param2 in admin:
                    adhi1.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in admin:
                    adhi2.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in admin:
                    adhi3.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in admin:
                    adhi4.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in admin:
                    adhi5.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid:
                if op.param2 in mid2:
                    adhi1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid3:
                    adhi1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid4:
                    adhi1.acceptGroupInvitation(op.param1)
            if op.param3 in mid:
                if op.param2 in mid5:
                    adhi1.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid2:
                if op.param2 in mid:
                    adhi2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid3:
                    adhi2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid4:
                    adhi2.acceptGroupInvitation(op.param1)
            if op.param3 in mid2:
                if op.param2 in mid5:
                    adhi2.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid3:
                if op.param2 in mid:
                    adhi3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid2:
                    adhi3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid4:
                    adhi3.acceptGroupInvitation(op.param1)
            if op.param3 in mid3:
                if op.param2 in mid5:
                    adhi3.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid4:
                if op.param2 in mid:
                    adhi4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid2:
                    adhi4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid3:
                    adhi4.acceptGroupInvitation(op.param1)
            if op.param3 in mid4:
                if op.param2 in mid5:
                    adhi4.acceptGroupInvitation(op.param1)
                    
            if op.param3 in mid5:
                if op.param2 in mid:
                    adhi5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid2:
                    adhi5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid3:
                    adhi5.acceptGroupInvitation(op.param1)
            if op.param3 in mid5:
                if op.param2 in mid4:
                    adhi5.acceptGroupInvitation(op.param1)
                    
        if op.type == 13:
            if mid in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in admin or Bots:
                  adhi1.acceptGroupInvitation(op.param1)
                else:
                  adhi1.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid2 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in admin or Bots:
                  adhi2.acceptGroupInvitation(op.param1)
                else:
                  adhi2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid3 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in admin or Bots:
                  adhi3.acceptGroupInvitation(op.param1)
                else:
                  adhi3.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid4 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in admin or Bots:
                  adhi4.acceptGroupInvitation(op.param1)
                else:
                  adhi4.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if mid5 in op.param3:
              if wait['autoJoin'] == True:
                if op.param2 in Bots or admin:
                  adhi5.acceptGroupInvitation(op.param1)
                else:
                  adhi5.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
        if op.type == 19: #bot Ke Kick
          if op.param2 in Bots:
            pass
          if op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in admin or Bots:
                try:
                  G = adhi2.getGroup(op.param1)
                  G = adhi3.getGroup(op.param1)
                  adhi2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  adhi3.updateGroup(G)
                  Ticket = adhi3.reissueGroupTicket(op.param1)
                  adhi1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  adhi1.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  adhi1.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid2:
              if op.param2 not in admin or Bots:
                try:
                  G = adhi3.getGroup(op.param1)
                  G = adhi4.getGroup(op.param1)
                  adhi3.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  adhi4.updateGroup(G)
                  Ticket = adhi4.reissueGroupTicket(op.param1)
                  adhi2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  adhi2.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  adhi2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid3:
              if op.param2 not in admin or Bots:
                try:
                  G = adhi4.getGroup(op.param1)
                  G = adhi5.getGroup(op.param1)
                  kr4.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  adhi5.updateGroup(G)
                  Ticket = adhi5.reissueGroupTicket(op.param1)
                  adhi3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  adhi3.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  adhi3.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid4:
              if op.param2 not in admin or Bots:
                try:
                  G = adhi5.getGroup(op.param1)
                  G = adhi1.getGroup(op.param1)
                  kr5.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  adhi1.updateGroup(G)
                  Ticket = adhi1.reissueGroupTicket(op.param1)
                  adhi4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  adhi4.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  adhi4.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in mid5:
              if op.param2 not in admin or Bots:
                try:
                  G = adhi1.getGroup(op.param1)
                  G = adhi2.getGroup(op.param1)
                  adhi2.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  adhi1.updateGroup(G)
                  Ticket = adhi1.reissueGroupTicket(op.param1)
                  adhi5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  adhi5.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  adhi5.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                  
            if op.param3 in admin:
              if op.param2 not in Bots:
                try:
                  adhi1.kickoutFromGroup(op.param1,[op.param2])
                  adhi1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  try:
                    adhi1.kickoutFromGroup(op.param1,[op.param2])
                    adhi1.inviteIntoGroup(op.param1,[admin])
                    wait["blacklist"][op.param2] = True
                  except:
                    try:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                      wait["blacklist"][op.param2] = True

            if op.param3 in admin or Bots:
                if op.param2 in admin or Bots:
                    try:
                        adhi1.inviteIntoGroup(op.param1,admin)
                        adhi1.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,[admin])
                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

            if op.param3 in admin or owner:
              if op.param2 not in Bots:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  adhi1.inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                  wait["blacklist"][op.param2] = True
                  
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait['leaveRoom'] == True:
                adhi1.leaveRoom(op.param1)
                adhi2.leaveRoom(op.param1)
                adhi3.leaveRoom(op.param1)
                adhi4.leaveRoom(op.param1)
                adhi5.leaveRoom(op.param1)
        if op.type == 24:
            if wait['leaveRoom'] == True:
                adhi1.leaveRoom(op.param1)
                adhi2.leaveRoom(op.param1)
                adhi3.leaveRoom(op.param1)
                adhi4.leaveRoom(op.param1)
                adhi5.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            adhi1.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = adhi1.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            adhi1.updateGroup(G)
                        except:
                            adhi1.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait['leaveRoom'] == True:
                    adhi1.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                adhi1.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        adhi1.sendText(msg.to,text)
        if op.type == 25:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data["status"] == 200:
                            if data['result']['result'] == 100:
                                adhi1.sendText(msg.to, "[From Simi]\n" + data['result']['response'].encode('utf-8'))

        if op.type == 26:
            msg = op.message
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = adhi1.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
                     ret_ = "[Auto Respon] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  adhi1.sendText(msg.to,ret_ + cName)
                                  adhi1.sendAudio(msg.to,"tts.mp3")
                                  break

            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['potoMention'] == True:
                     contact = adhi1.getContact(msg.from_)
                     cName = contact.pictureStatus
                     balas = ["http://dl.profile.line-cdn.net/" + cName]
                     ret_ = random.choice(balas)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention["MENTIONEES"]
                     for mention in mentionees:
                           if mention["M"] in Bots:
                                  adhi1.sendImageWithURL(msg.to,ret_)
                                  break  
                    
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['kickMention'] == True:
                     contact = adhi1.getContact(msg.from_)
                     cName = contact.displayName
                     balas = [cName + "Kangenkah sampai ngetag mulu?",cName + " nah mending pc aja klo penting..!", "kenapa, ", cName + " kangen ya?","kangen bilang, gak usah ngetag mulu, " + cName, "sekali lagi ngetag, bayar ya..!!! " + cName, "Tuh kan" + cName + "ngetag lagi, mojok aja yux...!!!"]
                     ret_ = "[Auto Respon] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  adhi1.sendText(msg.to,ret_)
                                  adhi1.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = adhi1.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             adhi1.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 adhi1.findAndAddContactsByMid(target)
                                 adhi1.inviteIntoGroup(msg.to,[target])
                                 adhi1.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      adhi1.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break

        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["winvite"] == True:
                    if msg.from_ in admin or Bots:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = adhi1.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                adhi1.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                adhi1.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                adhi1.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    adhi1.findAndAddContactsByMid(target)
                                    adhi1.inviteIntoGroup(msg.to,[target])
                                    adhi1.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        adhi1.findAndAddContactsByMid(invite)
                                        adhi1.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        adhi1.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break

                    if msg.from_ in admin or Bots:
                        _name = msg.contentMetadata["displayName"]
                        invite = msg.contentMetadata["mid"]
                        groups = adhi2.getGroup(msg.to)
                        pending = groups.invitee
                        targets = []
                        for s in groups.members:
                            if _name in s.displayName:
                                adhi2.sendText(msg.to,"-> " + _name + " ada di room ini")
                                break
                            elif invite in wait["blacklist"]:
                                adhi2.sendText(msg.to,"Maaf, " + _name + " kena Blacklist")
                                adhi2.sendText(msg.to,"hubungi owner kami ya !, \n➡Unban: " + invite)
                                break
                            else:
                                targets.append(invite)
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    adhi2.findAndAddContactsByMid(target)
                                    adhi2.inviteIntoGroup(msg.to,[target])
                                    adhi2.sendText(msg.to,"Selesai di Invite : \n➡" + _name)
                                    wait["winvite"] = False
                                    break
                                except:
                                    try:
                                        adhi2.findAndAddContactsByMid(invite)
                                        adhi2.inviteIntoGroup(op.param1,[invite])
                                        wait["winvite"] = False
                                    except:
                                        adhi2.sendText(msg.to,"Negative, Error detected")
                                        wait["winvite"] = False
                                        break

            #if msg.contentType == 13:
            #    if wait['steal'] == True:
            #        _name = msg.contentMetadata["displayName"]
            #        copy = msg.contentMetadata["mid"]
            #        groups = kr1.getGroup(msg.to)
            #        pending = groups.invitee
            #        targets = []
            #        for s in groups.members:
            #            if _name in s.displayName:
            #                print "[Target] Stealed"
            #                break                             
            #            else:
            #                targets.append(copy)
            #        if targets == []:
            #            pass
            #        else:
            #            for target in targets:
            #                try:
            #                    kr1.findAndAddContactsByMid(target)
            #                    contact = kr1.getContact(target)
            #                    cu = kr1.channel.getCover(target)
            #                    path = str(cu)
            #                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            #                    kr1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
            #                    kr1.sendText(msg.to,"Profile Picture " + contact.displayName)
            #                    kr1.sendImageWithURL(msg.to,image)
            #                    kr1.sendText(msg.to,"Cover " + contact.displayName)
            #                    kr1.sendImageWithURL(msg.to,path)
            #                    wait['steal'] = False
            #                    break
            #                except:
            #                        pass    
                                
            if wait['alwayRead'] == True:
                if msg.toType == 0:
                    adhi1.sendChatChecked(msg.from_,msg.id)
                else:
                    adhi1.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        adhi1.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        adhi1.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        adhi1.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        adhi1.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        adhi1.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        adhi1.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        adhi1.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        adhi1.sendText(msg.to,"Done")
                elif wait['contact'] == True:
                    msg.contentType = 0
                    adhi1.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = adhi1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = adhi1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        adhi1.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = adhi1.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = adhi1.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        adhi1.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait['timeline'] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    adhi1.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,helpmsg)
                    else:
                        adhi1.sendText(msg.to,helpmsg)
            elif msg.text.lower() == 'help2':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,helpset)
                    else:
                        adhi1.sendText(msg.to,helpset)
            elif msg.text.lower() == 'help3':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,helpgrup)
                    else:
                        adhi1.sendText(msg.to,helpgrup)
#            elif msg.text.lower() == 'keyself':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        kr1.sendText(msg.to,helpself)
#                    else:
#                        kr1.sendText(msg.to,helpself)
#            elif msg.text.lower() == 'keygrup':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        kr1.sendText(msg.to,helpgrup)
#                    else:
#                        kr1.sendText(msg.to,helpgrup)
#            elif msg.text.lower() == 'keyset':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        adhi1.sendText(msg.to,helpset)
#                    else:
#                        adhi1.sendText(msg.to,helpset)
#            elif msg.text.lower() == 'keytran':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        adhi1.sendText(msg.to,helptranslate)
#                    else:
#                        adhi1.sendText(msg.to,helptranslate)
#            elif msg.text.lower() == 'keyrhs':
#                if msg.from_ in admin:
#                    if wait["lang"] == "JP":
#                        kr1.sendText(msg.to,helprhs)
#                    else:
#                        kr1.sendText(msg.to,helprhs)
                        
            elif msg.text in ["Sp","Speed","speed"]:
                if msg.from_ in admin:
                    start = time.time()
                    adhi1.sendText(msg.to, "􀰂􀰂􀰂􀰂􀠁􀠁􀠁 ༺Waiitt༻ 􀂳􏿿.....")
                    elapsed_time = time.time() - start
                    time.sleep(0.06)
                    adhi1.sendText(msg.to, "%sseconds" % (elapsed_time))
            elif msg.text.lower() == 'crash':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub4d829c38a9bcc4bf125fbd2a4167119',"}
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi2.sendMessage(msg)
                    adhi2.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                adhi1.sendMessage(msg)
                
#            elif "facebook " in msg.text:
#                if msg.from_ in admin:
#                    a = msg.text.replace("facebook ","")
#                    b = urllib.quote(a)
#                    adhi1.sendText(msg.to,"
#                    adhi1.sendText(msg.to, "https://www.facebook.com" + b)
#                    adhi1.sendText(msg.to
#======================== FOR COMMAND MODE ON STARTING ==========================#
            elif msg.text.lower() == 'mode on':
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protecion Already On")
                        else:
                            adhi1.sendText(msg.to,"Protecion Already On")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protecion Already On")
                        else:
                            adhi1.sendText(msg.to,"Protecion Already On")
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already On")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already On")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already On")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already On")
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Invite already On")
                        else:
                            adhi1.sendText(msg.to,"Protection Invite already On")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
#======================== FOR COMMAND MODE OFF STARTING ==========================#
            elif msg.text.lower() == 'mode off':
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection already Off")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                        else:
                            adhi1.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already off")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already off")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already Off")
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
#========================== FOR COMMAND BOT STARTING =============================#
            elif msg.text.lower() == 'contact on':
                if msg.from_ in admin:
                    if wait['contact'] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                    else:
                        wait['contact'] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
                        else:
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ ση")
            elif msg.text.lower() == 'contact off':
                if msg.from_ in admin:
                    if wait['contact'] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
                    else:
                        wait['contact'] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ ςεϯ ϯσ σƒƒ")
                        else:
                            adhi1.sendText(msg.to,"ɕσηϯαɕϯ αʆɾεαδψ σƒƒ")
            elif msg.text.lower() == 'protect on':
                if msg.from_ in admin:
                    if wait["protect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protecion Already On")
                        else:
                            adhi1.sendText(msg.to,"Protecion Already On")
                    else:
                        wait["protect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protecion Already On")
                        else:
                            adhi1.sendText(msg.to,"Protecion Already On")
            elif msg.text.lower() == 'qr on':
                if msg.from_ in admin:
                    if wait["linkprotect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already On")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already On")
                    else:
                        wait["linkprotect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already On")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already On")
            elif msg.text.lower() == 'invite on':
                if msg.from_ in admin:
                    if wait["inviteprotect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Invite already On")
                        else:
                            adhi1.sendText(msg.to,"Protection Invite already On")
                    else:
                        wait["inviteprotect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"ρяσтє¢тισи ιиνιтє αℓяєα∂у σи")
            elif msg.text.lower() == 'cancel on':
                if msg.from_ in admin:
                    if wait["cancelprotect"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
                    else:
                        wait["cancelprotect"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"¢αи¢єℓ ρяσтє¢тισи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin on':
                if msg.from_ in admin:
                    if wait['autoJoin'] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
                    else:
                        wait['autoJoin'] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σи")
                        else:
                            adhi1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σи")
            elif msg.text.lower() == 'autojoin off':
                if msg.from_ in admin:
                    if wait['autoJoin'] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            adhi1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
                    else:
                        wait['autoJoin'] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"αυтσʝσιи ѕєт тσ σff")
                        else:
                            adhi1.sendText(msg.to,"αυтσʝσιи αℓяєα∂у σff")
            elif msg.text.lower() == 'protect off':
                if msg.from_ in admin:
                    if wait["protect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection already Off")
                    else:
                        wait["protect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"ρяσтє¢тισи ѕєт тσ σff")
                        else:
                            adhi1.sendText(msg.to,"ρяσтє¢тισи αℓяєα∂у σff")
            elif msg.text.lower() == 'qr off':
                if msg.from_ in admin:
                    if wait["linkprotect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already off")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already off")
                    else:
                        wait["linkprotect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Qr already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Qr already Off")
            elif msg.text.lower() == 'invit off':
                if msg.from_ in admin:
                    if wait["inviteprotect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                    else:
                        wait["inviteprotect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Invite already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Invite already Off")
            elif msg.text.lower() == 'cancel off':
                if msg.from_ in admin:
                    if wait["cancelprotect"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
                    else:
                        wait["cancelprotect"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
                        else:
                            adhi1.sendText(msg.to,"Protection Cancel already Off")
            elif "Grup cancel:" in msg.text:
                if msg.from_ in admin:
 		    try:
                        strnum = msg.text.replace("Grup cancel:","")
                        if strnum == "off":
                            wait['autoCancel']["on"] = False
                            if wait["lang"] == "JP":
                                adhi1.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                            else:
                                adhi1.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                        else:
                            num =  int(strnum)
                            wait['autoCancel']["on"] = True
                            if wait["lang"] == "JP":
                                adhi1.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                            else:
                                adhi1.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                    except:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Nilai tidak benar")
                        else:
                            adhi1.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'autoleave on':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            adhi1.sendText(msg.to,"Auto Leave room already on")
                    else:
                        wait['leaveRoom'] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto Leave room set to on")
                        else:
                            adhi1.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if msg.from_ in admin:
                    if wait['leaveRoom'] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            adhi1.sendText(msg.to,"Auto Leave room already off")
                    else:
                        wait['leaveRoom'] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto Leave room set to off")
                        else:
                            adhi1.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
                if msg.from_ in admin:
                    if wait['timeline'] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Share set to on")
                        else:
                            adhi1.sendText(msg.to,"Share already on")
                    else:
                        wait['timeline'] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Share set to on")
                        else:
                            adhi1.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if msg.from_ in admin:
                    if wait['timeline'] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Share set to off")
                        else:
                            adhi1.sendText(msg.to,"Share already off")
                    else:
                        wait['timeline'] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Share set to off")
                        else:
                            adhi1.sendText(msg.to,"Share already off")
            elif msg.text.lower() == "set":
                if msg.from_ in admin:
                    md = """􀰂􀰂􀰂􀰂􀠁􀠁􀠁 ༺T-B-A༻ 􀂳􏿿"""
                    if wait['contact'] == True: md+="Contact:on [✅]\n"
                    else: md+="Contact:off [❌]\n"
                    if wait['autoJoin'] == True: md+="Auto Join:on [✅]\n"
                    else: md +="Auto Join:off [❌]\n"
                    if wait['autoCancel']["on"] == True:md+="╠❂➣Auto cancel:" + str(wait['autoCancel']["members"]) + "[✅]\n"
                    else: md+= "Group cancel:off [❌]\n"
                    if wait['leaveRoom'] == True: md+="Auto leave:on [✅]\n"
                    else: md+="Auto leave:off [❌]\n"
                    if wait['timeline'] == True: md+="Share:on [✅]\n"
                    else:md+="Share:off [❌]\n"
                    if wait['autoAdd'] == True: md+="Auto add:on [✅]\n"
                    else:md+="Auto add:off [❌]\n"
                    if wait["protect"] == True: md+="Protect:on [✅]\n"
                    else:md+="Protect:off [❌]\n"
                    if wait["linkprotect"] == True: md+="Link Protect:on [✅]\n"
                    else:md+="Link Protect:off [❌]\n"
                    if wait["inviteprotect"] == True: md+="Invitation Protect:on [✅]\n"
                    else:md+="Invitation Protect:off [❌]\n"
                    if wait["cancelprotect"] == True: md+="Cancel Protect:on [✅]\n"
                    else:md+="Cancel Protect:off [❌]\n╚═════════════"
                    adhi1.sendText(msg.to,md)

            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u350cc7408cc6cc82e056ee046131f925"}
                adhi1.sendMessage(msg)
                adhi1.sendText(msg.to,'Creator yang Ganteng dan kalem 􀰂􀰂􀰂􀰂􀠁􀠁􀠁 ༺T-B-A༻ 􀂳􏿿')
            elif msg.text.lower() == 'autoadd on':
                if msg.from_ in admin:
                    if wait['autoAdd'] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto add set to on")
                        else:
                            adhi1.sendText(msg.to,"Auto add already on")
                    else:
                        wait['autoAdd'] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto add set to on")
                        else:
                            adhi1.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if msg.from_ in admin:
                    if wait['autoAdd'] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto add set to off")
                        else:
                            adhi1.sendText(msg.to,"Auto add already off")
                    else:
                        wait['autoAdd'] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Auto add set to off")
                        else:
                            adhi1.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                if msg.from_ in admin:
                    wait['message'] = msg.text.replace("Pesan set:","")
                    adhi1.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if msg.from_ in admin:
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
                    else:
                        adhi1.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait['message'])
            elif "Coment Set:" in msg.text:
                if msg.from_ in admin:
                    c = msg.text.replace("Coment Set:","")
                    if c in [""," ","\n",None]:
                        adhi1.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                    else:
                        wait["comment"] = c
                        adhi1.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Comment on"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Aku berada di")
                        else:
                            adhi1.sendText(msg.to,"To open")
                    else:
                        wait["commentOn"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Comment Actived")
                        else:
                            adhi1.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Coment off"]:
                if msg.from_ in admin:
                    if wait["commentOn"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Hal ini sudah off")
                        else:
                            adhi1.sendText(msg.to,"It is already turned off")
                    else:
                        wait["commentOn"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Off")
                        else:
                            adhi1.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                if msg.from_ in admin:
                    adhi1.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                if msg.from_ in admin:
                    wait["wblack"] = True
                    adhi1.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                if msg.from_ in admin:
                    wait["dblack"] = True
                    adhi1.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if msg.from_ in admin:
                    if wait["commentBlack"] == {}:
                        adhi1.sendText(msg.to,"Nothing in the blacklist")
                    else:
                        adhi1.sendText(msg.to,"The following is a blacklist")
                        mc = ""
                        for mi_d in wait["commentBlack"]:
                            mc += "ãƒ»" +kr1.getContact(mi_d).displayName + "\n"
                        adhi1.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        adhi1.sendText(msg.to,"Jam already on")
                    else:
                        wait["clock"] = True
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = adhi1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        adhi1.updateProfile(profile)
                        adhi1.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if msg.from_ in admin:
                    if wait["clock"] == False:
                        adhi1.sendText(msg.to,"Jam already off")
                    else:
                        wait["clock"] = False
                        adhi1.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                if msg.from_ in admin:
                    n = msg.text.replace("Jam say:","")
                    if len(n.decode("utf-8")) > 30:
                        adhi1.sendText(msg.to,"terlalu lama")
                    else:
                        wait["cName"] = n
                        adhi1.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if msg.from_ in admin:
                    if wait["clock"] == True:
                        now2 = datetime.now()
                        nowT = datetime.strftime(now2,"?%H:%M?")
                        profile = adhi1.getProfile()
                        profile.displayName = wait["cName"] + nowT
                        adhi1.updateProfile(profile)
                        adhi1.sendText(msg.to,"Diperbarui")
                    else:
                        adhi1.sendText(msg.to,"Silahkan Aktifkan Jam")
            elif "Image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        adhi1.sendImageWithURL(msg.to,path)
                    except:
                        pass
#========================== FOR COMMAND BOT FINISHED =============================#
            elif "Spam change:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam change:","")
                        adhi1.sendText(msg.to,"spam changed")

            elif "Spam add:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        wait['spam'] = msg.text.replace("Spam add:","")
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"spam changed")
                        else:
                            adhi1.sendText(msg.to,"Done")

            elif "Spam:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        strnum = msg.text.replace("Spam:","")
                        num = int(strnum)
                        for var in range(0,num):
                            adhi1.sendText(msg.to, wait['spam'])
#=====================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        bctxt = msg.text.replace("Spam ", "")
                        t = adhi1.getAllContactIds()
                        t = 500
                        while(t):
                            adhi1.sendText(msg.to, (bctxt))
                            t-=1
#==============================================
            elif "Spamcontact @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Spamcontact @","")
                    _nametarget = _name.rstrip(' ')
                    gs = adhi1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(g.mid,'spam')
                            adhi1.sendText(msg.to, "Selesai di Spam")
                            print " Spammed !"

            elif "crashkontak @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("crashkontak @","")
                    _nametarget = _name.rstrip(' ')
                    gs = adhi1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName + g.mid
                            xlen = str(len(xname)+1)
                            msg.contentType = 13
                            msg.text = 'mid'+xname+''
                            msg.contentMetadata = {'mid': "ub4d829c38a9bcc4bf125fbd2a4167119',"}
                            adhi1.sendMessage(msg)
                            adhi1.sendText("crash kontak selesai")
                            print " Spammed crash !"
#==============================================================================#
            elif msg.text in ["Invite"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    adhi1.sendText(msg.to,"Kirim Contact")
            elif msg.text in ["Jepit"]:
                if msg.from_ in admin:
                    wait["invite"] = True
                    adhi1.sendText(msg.to,"Kirim Contact")
                    
            elif msg.text in ["Undang"]:
                if msg.from_ in admin:
                    wait["winvite"] = True
                    adhi2.sendText(msg.to,"Kirim Contact")
            
            elif msg.text in ["Steal contact"]:
                if msg.from_ in admin:
                    wait['contact'] = True
                    adhi1.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    adhi1.sendText(msg.to,"Like Status Owner")
                    try:
                        likeme()
                    except:
                        pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                if msg.from_ in admin:
                    print "[Command]Like executed"
                    adhi1.sendText(msg.to,"Like Status Teman")
                    try:
                        likefriend()
                    except:
                        pass
            
            elif msg.text in ["Like:on","Like on"]:
                if msg.from_ in admin:
                    if wait['likeOn'] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if msg.from_ in admin:
                    if wait['likeOn'] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Done")
                    else:
                        wait['likeOn'] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Already")
                        
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = True
                    adhi1.sendText(msg.to,"Simi mode On")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                if msg.from_ in admin:
                    settings["simiSimi"][msg.to] = False
                    adhi1.sendText(msg.to,"Simi mode Off")
                
            elif msg.text in ["Autoread on","Read on"]:
                if msg.from_ in admin:
                    wait['alwayRead'] = True
                    adhi1.sendText(msg.to,"Auto read On")
                
            elif msg.text in ["Autoread off","Read off"]:
                if msg.from_ in admin:
                    wait['alwayRead'] = False
                    adhi1.sendText(msg.to,"Auto read Off")
                
            elif msg.text in ["Tag on","tag on"]:
                if msg.from_ in admin:
                    wait['detectMention'] = True
                    adhi1.sendText(msg.to,"Auto respon tag On")
                
            elif msg.text in ["Tag off","tag off"]:
                if msg.from_ in admin:
                    wait['detectMention'] = False
                    adhi1.sendText(msg.to,"Auto respon tag Off")
            
            elif msg.text in ["foto on","foto on"]:
                if msg.from_ in admin:
                    wait['potoMention'] = True
                    adhi1.sendText(msg.to,"Auto respon tag poto On")
                
            elif msg.text in ["Foto off","foto off"]:
                if msg.from_ in admin:
                    wait['potoMention'] = False
                    adhi1.sendText(msg.to,"Auto respon tag poto Off")
            
            elif msg.text in ["Tag2 on","tag2 on"]:
                if msg.from_ in admin:
                    wait['kickMention'] = True
                    adhi1.sendText(msg.to,"Auto Kick tag ON")
                
            elif msg.text in ["Tag2 off","tag2 off"]:
                if msg.from_ in admin:
                    wait['kickMention'] = False
                    adhi1.sendText(msg.to,"Auto Kick tag OFF")
            elif "Time" in msg.text:
                if msg.toType == 2:
                    adhi1.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
#==============================================================================#
            elif msg.text in ["Datang on","datang on"]:
                if msg.from_ in admin:
                    if wait["Wc"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"noтιғ yg joιn on")
                    else:
                        wait["Wc"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"already on")
            elif msg.text in ["Datang off","datang off"]:
                if msg.from_ in admin:
                    if wait["Wc"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"noтιғ yg joιn oғғ")
                    else:
                        wait["Wc"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif msg.text in ["Keluar on","keluar on"]:
                if msg.from_ in admin:
                    if wait["Lv"] == True:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"noтιғ yg leave on")
                    else:
                        wait["Lv"] = True
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"already on")
            elif msg.text in ["Keluar off","keluar off"]:
                if msg.from_ in admin:
                    if wait["Lv"] == False:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"noтιғ yg leave oғғ")
                    else:
                        wait["Lv"] = False
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"already oғғ")
#==============================================================================#
            elif "Dl" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        if msg.toType == 2:
                            print "ok"
                            _name = msg.text.replace("Dl","")
                            gs = adhi1.getGroup(msg.to)
                            gs = adhi2.getGroup(msg.to)
                            gs = adhi3.getGroup(msg.to)
                            gs = adhi4.getGroup(msg.to)
                            adhi1.sendText(msg.to,"Jangan panik, santai aja ya ô")
                            adhi2.sendText(msg.to,"Group di bersihkan...!!")
                            targets = []
                            for g in gs.members:
                                if _name in g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                adhi1.sendText(msg.to,"Tidak di temukan")
                                adhi2.sendText(msg.to,"Tidak di temukan")
                            else:
                                for target in targets:
                                    try:
                                        klist=[adhi1,adhi2,adhi3,adhi4]
                                        kicker=random.choice(klist)
                                        kicker.kickoutFromGroup(msg.to,[target])
                                        print (msg.to,[g.mid])
                                    except:
                                        adhi1.sendText(msg.to,"Group Bersih")
                                        adhi2.sendText(msg.to,"Group Bersih")
            elif msg.text in ["Salam1"]:
                adhi1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                adhi2.sendText(msg.to,"Assalamu'alaikum")
            elif msg.text in ["Salam2"]:
                adhi1.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                adhi2.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
            elif "Salam3" in msg.text:
                if msg.from_ in admin:
                    adhi1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                    adhi2.sendText(msg.to,"Assalamu'alaikum")
                    adhi3.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                    adhi4.sendText(msg.to,"Wa'alaikumsallam.Wr,Wb")
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Salam3","")
                        gs = adhi1.getGroup(msg.to)
                        gs = adhi2.getGroup(msg.to)
                        gs = adhi3.getGroup(msg.to)
                        gs = adhi4.getGroup(msg.to)
                        adhi1.sendText(msg.to,"maaf kalo gak sopan")
                        adhi2.sendText(msg.to,"Qo salamnya gak ada yang jawab ya..!!")
                        adhi3.sendText(msg.to,"hehehhehe")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            adhi1.sendText(msg.to,"Tidak di temukan")
                        else:
                            for target in targets:
                              if target not in admin:
                                try:
                                    klist=[adhi1,adhi2,adhi3,adhi4]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    adhi1.sendText(msg.to,"السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                                    adhi2.sendText(msg.to,"وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُهُ")
                                    adhi3.sendText(msg.to,"Nah salamnya jawab sendiri jadinya wkwkwk..!!")
            elif ("Kick " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           adhi1.kickoutFromGroup(msg.to,[target])
                       except:
                           adhi1.sendText(msg.to,"Error")
            
            elif ("kiss " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           adhi1.kickoutFromGroup(msg.to,[target])
                           adhi1.inviteIntoGroup(msg.to,[target])
                           adhi1.cancelGroupInvitation(msg.to,[target])
                       except:
                           adhi1.sendText(msg.to,"Error")
            
#            elif "Tajong " in msg.text:
#                if msg.from_ in admin:
#                    nk0 = msg.text.replace("Tajong ","")
#                    nk1 = nk0.lstrip()
#                    nk2 = nk1.replace("@","")
#                    nk3 = nk2.rstrip()
#                    _name = nk3
#                    gs = kr1.getGroup(msg.to)
#                    ginfo = kr1.getGroup(msg.to)
#                    gs.preventJoinByTicket = False
#                    kr1.updateGroup(gs)
#                    invsend = 0
#                    Ticket = kr1.reissueGroupTicket(msg.to)
#                    kr6.acceptGroupInvitationByTicket(msg.to,Ticket)
#                    time.sleep(0.01)
#                    targets = []
#                    for s in gs.members:
#                        if _name in s.displayName:
#                           targets.append(s.mid)
#                    if targets == []:
#                       sendMessage(msg.to,"user does not exist")
#                       pass
#                    else:
#                       for target in targets:
#                          try:
#                            kr6.kickoutFromGroup(msg.to,[target])
#                            print (msg.to,[g.mid])
#                          except:
#                            kr6.leaveGroup(msg.to)
#                            gs = kr1.getGroup(msg.to)
#                            gs.preventJoinByTicket = True
#                            kr1.updateGroup(gs)
#                            gs.preventJoinByTicket(gs)
#                            kr1.updateGroup(gs)
            
            elif "Kick: " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Kick: ","")
                    adhi1.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                if msg.from_ in admin:
                    key = msg.text[-33:]
                    adhi1.findAndAddContactsByMid(key)
                    adhi1.inviteIntoGroup(msg.to, [key])
                    contact = adhi1.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adhi1.getGroup(msg.to)
                        if group.invitee is not None:
                            gInviMids = [contact.mid for contact in group.invitee]
                            adhi1.cancelGroupInvitation(msg.to, gInviMids)
                        else:
                            if wait["lang"] == "JP":
                                adhi1.sendText(msg.to,"Tidak ada undangan")
                            else:
                                adhi1.sendText(msg.to,"Invitan tidak ada")
                    else:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"Tidak ada undangan")
                        else:
                            adhi1.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'link on':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adhi1.getGroup(msg.to)
                        group.preventJoinByTicket = False
                        adhi1.updateGroup(group)
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"URL open")
                        else:
                            adhi1.sendText(msg.to,"URL open")
                    else:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            adhi1.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'link off':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adhi1.getGroup(msg.to)
                        group.preventJoinByTicket = True
                        adhi1.updateGroup(group)
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"URL close")
                        else:
                            adhi1.sendText(msg.to,"URL close")
                    else:
                        if wait["lang"] == "JP":
                            adhi1.sendText(msg.to,"It can not be used outside the group")
                        else:
                            adhi1.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url","Gurl"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        g = adhi1.getGroup(msg.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            adhi1.updateGroup(g)
                        gurl = adhi1.reissueGroupTicket(msg.to)
                        adhi1.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif "Gcreator" == msg.text:
                try:
                    group = adhi1.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    adhi1.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    adhi1.sendMessage(M)
                    adhi1.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.from_ in admin:
                    if msg.toType == 2:
                           ginfo = adhi1.getGroup(msg.to)
                           try:
                               gcmid = ginfo.creator.mid
                           except:
                               gcmid = "Error"
                           if wait["lang"] == "JP":
                               adhi1.inviteIntoGroup(msg.to,[gcmid])
                           else:
                               adhi1.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.from_ in admin:
                    if msg.toType == 2:
                        X = adhi1.getGroup(msg.to)
                        X.name = msg.text.replace("Gname: ","")
                        adhi1.updateGroup(X)
            
            elif msg.text.lower() == 'infogrup':
                if msg.from_ in admin:
                    group = adhi1.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    adhi1.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                if msg.from_ in admin:
                    gid = adhi1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "[%s]:%s\n" % (kr1.getGroup(i).name,i)
                    adhi1.sendText(msg.to,h)
#==============================================================================#
            elif msg.text in ["Glist"]:
                if msg.from_ in admin:
                    gid = adhi1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                        h += "%s\n" % (kr1.getGroup(i).name +" ? ["+str(len(kr1.getGroup(i).members))+"]")
                    adhi1.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                if msg.from_ in admin:
                    gid = adhi1.getGroupIdsInvited()
                    for i in gid:
                        adhi1.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,"Aku menolak semua undangan")
                    else:
                        adhi1.sendText(msg.to,"He declined all invitations")
                         
            elif "Auto add" in msg.text:
                if msg.from_ in admin:
                    thisgroup = adhi1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    adhi1.findAndAddContactsByMids(mi_d)
                    adhi1.sendText(msg.to,"Success Add all")
                    
            elif "Admin add @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = adhi1.getGroup(msg.to)
                gs = adhi2.getGroup(msg.to)
                gs = adhi3.getGroup(msg.to)
                gs = adhi4.getGroup(msg.to)
                gs = adhi5.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            adhi1.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                adhi1.sendText(msg.to,"Perintah Ditolak.")
                adhi1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in admin:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = adhi1.getGroup(msg.to)
                gs = adhi2.getGroup(msg.to)
                gs = adhi3.getGroup(msg.to)
                gs = adhi4.getGroup(msg.to)
                gs = adhi5.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            adhi1.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                adhi1.sendText(msg.to,"Perintah Ditolak.")
                adhi1.sendText(msg.to,"Hanya Owner Yang bisa Gunain Perintah ini.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  adhi1.sendText(msg.to,"The stafflist is empty")
              else:
                  adhi1.sendText(msg.to,"Tunggu...")
                  mc = "╔═════════════\n║Admin 􀰂􀰂􀰂􀰂􀠁􀠁􀠁 ༺T-B-A༻ 􀂳􏿿\n╠═════════════\n"
                  for mi_d in admin:
                      mc += "║••>" +adhi1.getContact(mi_d).displayName + "\n╠═════════════\n"
                  adhi1.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
                    
            elif msg.text in ["Sita Join","."]: #Panggil Semua Bot
                if msg.from_ in admin:
                    G = adhi1.getGroup(msg.to)
                    ginfo = adhi1.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    adhi1.updateGroup(G)
                    invsend = 0
                    Ticket = adhi1.reissueGroupTicket(msg.to)
                    adhi2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    adhi3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    adhi4.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    adhi5.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.01)
                    G = adhi1.getGroup(msg.to)
                    ginfo = adhi1.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    adhi1.updateGroup(G)
                    adhi5.sendText(msg.to,"Hallo...!!! " + str(ginfo.name) + "\n\nSemoga Selalu Bahagia...!!!")
                    print "Semua Sudah Lengkap"

            elif "Sita out" in msg.text: #keluar semua bots
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = adhi1.getGroup(msg.to)
                        ginfo = adhi2.getGroup(msg.to)
                        ginfo = adhi3.getGroup(msg.to)
                        ginfo = adhi4.getGroup(msg.to)
                        ginfo = adhi5.getGroup(msg.to)
                        try:
                            adhi1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            adhi2.leaveGroup(msg.to)
                            adhi3.leaveGroup(msg.to)
                            adhi4.leaveGroup(msg.to)
                            adhi5.leaveGroup(msg.to)
                            adhi1.leaveGroup(msg.to)
                        except:
                            pass
            elif "Sita Balik" in msg.text: #keluar bot kecuali bot induk
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = adhi1.getGroup(msg.to)
                        ginfo = adhi2.getGroup(msg.to)
                        ginfo = adhi3.getGroup(msg.to)
                        ginfo = adhi4.getGroup(msg.to)
                        ginfo = adhi5.getGroup(msg.to)
                        try:
                            adhi2.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            adhi3.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            adhi4.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            adhi5.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nJangan Lupa Bahagia...!!!")
                            adhi2.leaveGroup(msg.to)
                            adhi3.leaveGroup(msg.to)
                            adhi4.leaveGroup(msg.to)
                            adhi5.leaveGroup(msg.to)
                            #kr1.leaveGroup(msg.to)
                        except:
                            pass
#==============================================================================#
            elif "Anu" == msg.text.lower():
                if msg.from_ in admin:
                    group = adhi1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    adhi1.sendMessage(cnt)

            elif "crot" == msg.text.lower():
                if msg.from_ in admin:
                    group = adhi1.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                    if jml <= 100:
                        summon(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                    if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                    if jml > 500:
                         print "Terlalu Banyak Men 500+"
                    cnt = Message()
                    cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                    cnt.to = msg.to
                    adhi1.sendMessage(cnt)

            elif "Intip on" == msg.text.lower():
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            adhi1.sendText(msg.to,"Setpoint already on")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(wait2, fp, sort_keys=True, indent=4)
                            adhi1.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                            print wait2

                    
            elif "Intip off" == msg.text.lower():
                if msg.from_ in admin:
                    if msg.to not in wait2['readPoint']:
                        adhi1.sendText(msg.to,"Setpoint already off")
                    else:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                             pass
                        adhi1.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

            elif msg.text in ["cctv"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "\nRead aktif..."
                        if msg.to in wait2['readPoint']:
                            if wait2['ROM'][msg.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2['ROM'][msg.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            adhi1.sendText(msg.to, "╔═════════════ \n╠Sider :\n╠═════════════                     %s\n╠\n╠═════════════\n╠Reader :\n╠═════════════ %s\n╠\n╠═════════════\n╠In the last seen point:\n╠[%s]\n╚═════════════" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                            print "\nReading Point Set..."
                            try:
                                del wait2['readPoint'][msg.to]
                                del wait2['readMember'][msg.to]
                            except:
                                pass
                            wait2['readPoint'][msg.to] = msg.id
                            wait2['readMember'][msg.to] = ""
                            wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                            wait2['ROM'][msg.to] = {}
                            print "sider ready"
                            adhi1.sendText(msg.to, "Auto Read Point!!" + (wait2['setTime'][msg.to]))
                        else:
                            adhi1.sendText(msg.to, "Ketik [Intip on] dulu, baru ketik [cctv]")



            elif "Ciduk" == msg.text.lower():
                if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                            adhi1.sendText(msg.to, "Reader:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = adhi1.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = ''
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nBefore: %s\nAfter: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={"MENTION":str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                            adhi1.sendMessage(msg)
                        except Exception as error:
                            print error
                        pass

                    else:
                        adhi1.sendText(msg.to, "Lurking has not been set.")
            elif "Gbroadcast: " in msg.text:
                if msg.from_ in owner:
                    bc = msg.text.replace("Gbroadcast: ","")
                    gid = adhi1.getGroupIdsJoined()
                    for i in gid:
                        adhi1.sendText(i, bc)
                    
            elif "Cbroadcast: " in msg.text:
                if msg.from_ in admin:
                    bc = msg.text.replace("Cbroadcast: ","")
                    gid = adhi1.getAllContactIds()
                    for i in gid:
                        adhi1.sendText(i, bc)
            
            elif "Spam change: " in msg.text:
                if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam change: ","")
                    adhi1.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                if msg.from_ in admin:
                    wait['spam'] = msg.text.replace("Spam add: ","")
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,"spam changed")
                    else:
                        adhi1.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                if msg.from_ in admin:
                    strnum = msg.text.replace("Spam: ","")
                    num = int(strnum)
                    for var in range(0,num):
                        adhi1.sendText(msg.to, wait['spam'])
            
            elif "Spamtag @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = adhi1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                        else:
                            pass
            
            elif "spam" in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "on":
                        if jmlh <= 100000:
                           for x in range(jmlh):
                               adhi1.sendText(msg.to, teks)
                        else:
                            adhi1.sendText(msg.to, "Out of Range!")
                    elif txt[1] == "off":
                        if jmlh <= 100000:
                            adhi1.sendText(msg.to, tulisan)
                        else:
                            adhi1.sendText(msg.to, "Out Of Range!")
                        
            elif ("Micadd " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            adhi1.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            adhi1.sendText(msg.to,"Fail !")
                            break
                    
            elif ("Micdel " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            adhi1.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            adhi1.sendText(msg.to,"Fail !")
                            break
                    
            elif msg.text in ["Miclist"]:
                if msg.from_ in admin:
                    if mimic["target"] == {}:
                        adhi1.sendText(msg.to,"nothing")
                    else:
                        mc = "Target mimic user\n"
                        for mi_d in mimic["target"]:
                            mc += "?? "+adhi1.getContact(mi_d).displayName + "\n"
                        adhi1.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                if msg.from_ in admin:
                    if mimic["copy"] == True:
                        siapa = msg.text.replace("Mimic target ","")
                        if siapa.rstrip(' ') == "me":
                            mimic["copy2"] = "me"
                            adhi1.sendText(msg.to,"Mimic change to me")
                        elif siapa.rstrip(' ') == "target":
                            mimic["copy2"] = "target"
                            adhi1.sendText(msg.to,"Mimic change to target")
                        else:
                            adhi1.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("Mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            adhi1.sendText(msg.to,"Reply Message on")
                        else:
                            adhi1.sendText(msg.to,"Sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            adhi1.sendText(msg.to,"Reply Message off")
                        else:
                            adhi1.sendText(msg.to,"Sudah off")
            elif "Setimage: " in msg.text:
                if msg.from_ in admin:
                    wait['pap'] = msg.text.replace("Setimage: ","")
                    adhi1.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim",'pap']:
                if msg.from_ in admin:
                    adhi1.sendImageWithURL(msg.to,wait['pap'])
            elif "Setvideo: " in msg.text:
                if msg.from_ in admin:
                    wait['pap'] = msg.text.replace("Setvideo: ","")
                    adhi1.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                if msg.from_ in admin:
                    adhi1.sendVideoWithURL(msg.to,wait['pap'])
            elif "TL:" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        tl_text = msg.text.replace("TL:","")
                        adhi1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
#==============================================================================#
            elif msg.text.lower() == 'mymid':
                adhi1.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                if msg.from_ in admin:
                    tl_text = msg.text.replace("Timeline: ","")
                    adhi1.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr1.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "TB bot: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("TB bot: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi1.getProfile()
                        profile.displayName = string
                        adhi1.updateProfile(profile)
                        adhi1.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi2.getProfile()
                        profile.displayName = string
                        adhi2.updateProfile(profile)
                        adhi2.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi3.getProfile()
                        profile.displayName = string
                        adhi3.updateProfile(profile)
                        adhi3.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi4.getProfile()
                        profile.displayName = string
                        adhi4.updateProfile(profile)
                        adhi4.sendText(msg.to,"Changed " + string + "")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi5.getProfile()
                        profile.displayName = string
                        adhi5.updateProfile(profile)
                        adhi5.sendText(msg.to,"Changed " + string + "")
            elif "Tbot1: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("Tbot1: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi1.getProfile()
                        profile.displayName = string
                        adhi1.updateProfile(profile)
                        adhi1.sendText(msg.to,"Changed " + string + "")
            elif "Tbot2: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("Tbot2: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi2.getProfile()
                        profile.displayName = string
                        adhi2.updateProfile(profile)
                        adhi2.sendText(msg.to,"Changed " + string + "")
            elif "Tbot3: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("Tbot3: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi3.getProfile()
                        profile.displayName = string
                        adhi3.updateProfile(profile)
                        adhi3.sendText(msg.to,"Changed " + string + "")
            elif "Tbot4: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("Tbot4: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi4.getProfile()
                        profile.displayName = string
                        adhi4.updateProfile(profile)
                        adhi4.sendText(msg.to,"Changed " + string + "")
            elif "Tbot5: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("Tbot5: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi5.getProfile()
                        profile.displayName = string
                        adhi5.updateProfile(profile)
                        adhi5.sendText(msg.to,"Changed " + string + "")
            elif "TBio: " in msg.text:
                if msg.from_ in admin:
                    string = msg.text.replace("TBio: ","")
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi1.getProfile()
                        profile.statusMessage = string
                        adhi1.updateProfile(profile)
                        adhi1.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi2.getProfile()
                        profile.statusMessage = string
                        adhi2.updateProfile(profile)
                        adhi2.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi3.getProfile()
                        profile.statusMessage = string
                        adhi3.updateProfile(profile)
                        adhi3.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi4.getProfile()
                        profile.statusMessage = string
                        adhi4.updateProfile(profile)
                        adhi4.sendText(msg.to,"Changed " + string)
                    if len(string.decode('utf-8')) <= 10000000000:
                        profile = adhi5.getProfile()
                        profile.statusMessage = string
                        adhi5.updateProfile(profile)
                        adhi5.sendText(msg.to,"Changed " + string)
            elif msg.text in ["Tbname"]:
                    h = adhi1.getContact(mid)
                    adhi1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["TBbot"]:
                    h = adhi1.getContact(mid)
                    h = adhi2.getContact(mid2)
                    h = adhi3.getContact(mid3)
                    h = adhi4.getContact(mid4)
                    h = adhi5.getContact(mid5)
                    adhi1.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    adhi2.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    adhi3.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    adhi4.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
                    adhi5.sendText(msg.to,"═══[DisplayName]═══\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = adhi1.getContact(mid)
                    adhi1.sendText(msg.to,"═══[StatusMessage]═══\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = adhi1.getContact(mid)
                    adhi1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = adhi1.getContact(mid)
                    adhi1.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = adhi1.getContact(mid)
                    adhi1.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = adhi1.getContact(mid)
                    cu = adhi1.channel.getCover(mid)          
                    path = str(cu)
                    adhi1.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = adhi1.getContact(mid)
                    cu = adhi1.channel.getCover(mid)          
                    path = str(cu)
                    adhi1.sendText(msg.to, path)
#===========================================================================================#
            elif msg.text in ["Sider on","sider on"]:
                if msg.from_ in admin:
                   try:
                       del cctv['point'][msg.to]
                       del cctv['sidermem'][msg.to]
                       del cctv['cyduk'][msg.to]
                   except:
                       pass
                   cctv['point'][msg.to] = msg.id
                   cctv['sidermem'][msg.to] = ""
                   cctv['cyduk'][msg.to]=True
                   wait["Sider"] == True
                   adhi1.sendText(msg.to,"Cek Sider on..!!!")

            elif msg.text in ["Sider off","sider off"]:
                if msg.from_ in admin:
                   if msg.to in cctv['point']:
                       cctv['cyduk'][msg.to]=False
                       wait["Sider"] = False
                       adhi1.sendText(msg.to,"Cek Sider di off")
                   else:
                       adhi1.sendText(msg.to,"Belum di set dul")
#======================================================================================#
            elif "Getmid @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Getmid @","")
                    _nametarget = _name.rstrip(' ')
                    gs = adhi1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            adhi1.sendText(msg.to, g.mid)
                        else:
                            pass
            elif "Getinfo" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = adhi1.getContact(key1)
                    cu = adhi1.channel.getCover(key1)
                    try:
                        adhi1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                    except:
                        adhi1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = adhi1.getContact(key1)
                    cu = adhi1.channel.getCover(key1)
                    try:
                        adhi1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                    except:
                        adhi1.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = adhi1.getContact(key1)
                    cu = adhi1.channel.getCover(key1)
                    try:
                        adhi1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                    except:
                        adhi1.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    contact = adhi1.getContact(key1)
                    cu = adhi1.channel.getCover(key1)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        adhi1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        adhi1.sendText(msg.to,"Profile Picture " + contact.displayName)
                        adhi1.sendImageWithURL(msg.to,image)
                        adhi1.sendText(msg.to,"Cover " + contact.displayName)
                        adhi1.sendImageWithURL(msg.to,path)
                    except:
                        pass
            elif "Getcontact" in msg.text:
                if msg.from_ in admin:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]                
                    mmid = adhi1.getContact(key1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": key1}
                    adhi1.sendMessage(msg)
            elif "Getpict @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getpict @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = adhi1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                adhi1.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getvid @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = adhi1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                adhi1.sendVideoWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Picturl @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = adhi1.getContact(target)
                                path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                adhi1.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Getcover @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = adhi1.getContact(target)
                                cu = adhi1.channel.getCover(target)          
                                path = str(cu)
                                adhi1.sendImageWithURL(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]cover executing"
                    _name = msg.text.replace("Coverurl @","")    
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi1.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = adhi1.getContact(target)
                                cu = adhi1.channel.getCover(target)
                                path = str(cu)
                                adhi1.sendText(msg.to, path)
                            except Exception as e:
                                raise e
                    print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                if msg.from_ in admin:
                    group = adhi1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    adhi1.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                if msg.from_ in admin:
                    group = adhi1.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    adhi1.sendText(msg.to,path)
            elif "Mycopy @" in msg.text:
                if msg.from_ in admin:
                    print "[COPY] Ok"
                    _name = msg.text.replace("Mycopy @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi1.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                                adhi1.CloneContactProfile(target)
                                adhi1.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                if msg.from_ in admin:
                    try:
                        adhi1.updateDisplayPicture(backup.pictureStatus)
                        adhi1.updateProfile(backup)
                        adhi1.sendText(msg.to, "Refreshed.")
                    except Exception as e:
                        adhi1.sendText(msg.to, str(e))
#==============================================================================#
            elif "Testext: " in msg.text:
                if msg.from_ in admin:
                    txt = msg.text.replace("Testext: ", "")
                    adhi1.kedapkedip(msg.to,txt)
                    print "[Command] Kedapkedip"
                    
            elif "Translate-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                adhi1.sendText(msg.to, A)
            elif "Translate-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                adhi1.sendText(msg.to, A)
            elif "Translate-ar" in msg.text:
                isi = msg.text.replace("Tr-ar ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                adhi1.sendText(msg.to, A)
            elif "Translate-jp" in msg.text:
                isi = msg.text.replace("Tr-jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                adhi1.sendText(msg.to, A)
            elif "Translate-ko" in msg.text:
                isi = msg.text.replace("Tr-ko ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                adhi1.sendText(msg.to, A)
            
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO ENGLISH**\n" + "" + result + "\n**SUKSES**")
            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"**FROM EN**\n" + "" + kata + "\n**TO ID**\n" + "" + result + "\n**SUKSES**")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"**FROM ID**\n" + "" + kata + "\n**TO JP**\n" + "" + result + "\n**SUKSES**")
            elif "Jp@id" in msg.text:
                bahasa_awal = 'ja'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Jp@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM JP----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@th" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'th'
                kata = msg.text.replace("Id@th ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO TH----\n" + "" + result + "\n------SUKSES-----")
            elif "Th@id" in msg.text:
                bahasa_awal = 'th'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Th@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM TH----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@jp" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ja'
                kata = msg.text.replace("Id@jp ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO JP----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ar" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ar'
                kata = msg.text.replace("Id@ar ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO AR----\n" + "" + result + "\n------SUKSES-----")
            elif "Ar@id" in msg.text:
                bahasa_awal = 'ar'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ar@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM AR----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
            elif "Id@ko" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'ko'
                kata = msg.text.replace("Id@ko ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM ID----\n" + "" + kata + "\n----TO KO----\n" + "" + result + "\n------SUKSES-----")
            elif "Ko@id" in msg.text:
                bahasa_awal = 'ko'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("Ko@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                adhi1.sendText(msg.to,"----FROM KO----\n" + "" + kata + "\n----TO ID----\n" + "" + result + "\n------SUKSES-----")
                
            elif msg.text.lower() == 'welcome':
                ginfo = adhi1.getGroup(msg.to)
                adhi1.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                adhi1.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
                tts = gTTS(text=jawaban1, lang='id')
                tts.save('tts.mp3')
                adhi1.sendAudio(msg.to,'tts.mp3')
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adhi1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adhi1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adhi1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adhi1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                adhi1.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                tanya = msg.text.replace("Kapan ","")
                jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                adhi1.sendAudio(msg.to,'tts.mp3')
                adhi1.sendText(msg.to,jawaban)
                adhi2.sendText(msg.to,jawaban)
                adhi2.sendText(msg.to,jawaban)
                  
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                adhi1.sendAudio(msg.to,'tts.mp3')
                adhi1.sendText(msg.to,jawaban)
                adhi2.sendText(msg.to,jawaban)
                adhi2.sendText(msg.to,jawaban)
                  
            elif "Tuh" in msg.text:
                adhi1.sendText(msg.to,'Kan')
                adhi1.sendText(msg.to,'Kan')
                adhi1.sendText(msg.to,'Kan')
            
            elif "Absen" in msg.text:
                if msg.from_ in admin:
                    adhi1.sendText(msg.to,"👉★★★√")
                    adhi2.sendText(msg.to,"👉★★★★√")
                    adhi3.sendText(msg.to,"👉★★★★★√")
                    adhi4.sendText(msg.to,"👉★★★★★★√")
                    adhi5.sendText(msg.to,"👉★★★★★★★√")
                    adhi1.sendText(msg.to,"👉Semua Hadir Boss...!!!")

            elif "Bcast " in msg.text:
                if msg.from_ in admin:
                    bc = msg.text.replace("Bcast ","")
                    gid = adhi1.getGroupIdsJoined()
                    for i in gid:
                        adhi1.sendText(i,"●▬▬▬▬[BROADCAST]▬▬▬▬●\n\n"+bc+"\n\n#BROADCAST!!")
            
            elif 'Youtube ' in msg.text:
                if msg.from_ in admin:
                    try:
                        textToSearch = (msg.text).replace('Youtube ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        adhi1.sendVideoWithURL(msg.to, ght)
                    except:
                        adhi1.sendText(msg.to, "Could not find it")
            
            elif "Yt " in msg.text:
                if msg.from_ in admin:
                    query = msg.text.replace("Yt ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        adhi1.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Lirik ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            adhi1.sendText(msg.to, hasil)
                    except Exception as wak:
                            adhi1.sendText(msg.to, str(wak))
                            
            elif "Wikipedia " in msg.text:
                if msg.from_ in admin:
                    try:
                        wiki = msg.text.lower().replace("Wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=1)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        adhi1.sendText(msg.to, pesan)
                    except:
                        try:
                            pesan="Over Text Limit! Please Click link\n"
                            pesan+=wikipedia.page(wiki).url
                            adhi1.sendText(msg.to, pesan)
                        except Exception as e:
                            adhi1.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace("Music ","")
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'This is Your Music\n'
                            hasil += 'Judul : ' + song[0]
                            hasil += '\nDurasi : ' + song[1]
                            hasil += '\nLink Download : ' + song[4]
                            adhi1.sendText(msg.to, hasil)
                            adhi1.sendText(msg.to, "Please Wait for audio...")
                            adhi1.sendAudioWithURL(msg.to, song[4])
                    except Exception as njer:
                        adhi1.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("Image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        adhi1.sendImageWithURL(msg.to,path)
                    except:
                        pass           
            
            elif "Instagram " in msg.text:
                if msg.from_ in admin:
                    try:
                        instagram = msg.text.replace("Instagram ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        adhi1.sendImageWithURL(msg.to, profileIG)
                        adhi1.sendText(msg.to, str(text))
                    except Exception as e:
                        adhi1.sendText(msg.to, str(e))

            elif "Kelahiran " in msg.text:
                if msg.from_ in admin:
                    tanggal = msg.text.replace("Kelahiran ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    lahir = data["data"]["lahir"]
                    usia = data["data"]["usia"]
                    ultah = data["data"]["ultah"]
                    zodiak = data["data"]["zodiak"]
                    adhi1.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text in ["Kalender","Waktu"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                adhi1.sendText(msg.to, rst)
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    adhi1.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    adhi1.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    adhi1.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    adhi1.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif "Restart" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Restart"
                    try:
                        adhi1.sendText(msg.to,"Restarting...")
                        adhi1.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        adhi1.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                if msg.from_ in admin:
                    try:
                        import sys
                        sys.exit()
                    except:
                        pass
                
            elif msg.text.lower() == 'runtime':
                if msg.from_ in admin:
                    eltime = time.time() - mulai
                    van = "Bot has been active "+waktu(eltime)
                    adhi1.sendText(msg.to,van)

            elif msg.text in ["Sbot"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
                if msg.from_ in admin:
                    gid = adhi1.getGroupIdsJoined()
                    gid = adhi2.getGroupIdsJoined()
                    gid = adhi3.getGroupIdsJoined()
                    gid = adhi4.getGroupIdsJoined()
                    gid = adhi5.getGroupIdsJoined()
                    for i in gid:
                        adhi1.leaveGroup(i)
                        adhi2.leaveGroup(i)
                        adhi3.leaveGroup(i)
                        adhi4.leaveGroup(i)
                        adhi5.leaveGroup(i)
                    if wait["lang"] == "JP":
                        adhi1.sendText(msg.to,"Bye~Bye " + str(ginfo.name) + "\n\nBots Dipaksa Keluar oleh Owner Bots...!!!\nMakasih...!!!")
                    else:
                        adhi1.sendText(msg.to,"He declined all invitations")
                        
#            elif msg.text in ["BA","Dhi"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA1","Dhi1"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA2","Dhi2"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA3","Dhi3"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA4","Dhi4"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA5","Cab5"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA6","Dhi6"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["BA7","Dhi7"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
#                    kr1.sendImageWithURL(msg.to, url)
                
#            elif msg.text in ["Team","Logo"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
#                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
#                    url2 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168227_131451417647415_680587542176648285_n.jpg?oh=e714a97fec8d8c1e178ab6c0a3ca39cf&oe=5AC96AD3"
#                    url3 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26195387_131462840979606_8781956575640573461_n.jpg?oh=27ba5e875917c20df7dd8916bdd64847&oe=5ABB27F4"
#                    url4 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111928_131462844312939_2544207656543605714_n.jpg?oh=0fac796564e963d8b573826263bbc6c7&oe=5AFA67A8"
#                    url5 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26219732_131462837646273_1213898565647052451_n.jpg?oh=c5a8bcce115cdab488bde1b8e981e5dd&oe=5AC3A96E"
#                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
#                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
#                    kr1.sendImageWithURL(msg.to, url)
#                    kr1.sendImageWithURL(msg.to, url1)
#                    kr1.sendImageWithURL(msg.to, url2)
#                    kr1.sendImageWithURL(msg.to, url3)
#                    kr1.sendImageWithURL(msg.to, url4)
#                    kr1.sendImageWithURL(msg.to, url5)
#                    kr1.sendImageWithURL(msg.to, url6)
#                    kr1.sendImageWithURL(msg.to, url7)
                
#            elif msg.text in ["Kibar","kibar"]:
#                if msg.from_ in admin:
#                    url = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26168676_131451404314083_3952554270011807487_n.jpg?oh=6e90aa78daaf5e06b1078bbf15d5aa0f&oe=5AB9882D"
#                    url1 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26165506_131451400980750_8433498092579272217_n.jpg?oh=c85beaa35a6f5babd638edeaac9bccaa&oe=5AF760B2"
#                    url6 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26167549_131462897646267_3496884138024907307_n.jpg?oh=edc63b98f790e9bf2cbb57dce7df9b25&oe=5AB0DDF6"
#                    url7 = "https://scontent.fcgk2-1.fna.fbcdn.net/v/t1.0-9/26111931_131462894312934_151942458148573227_n.jpg?oh=2b0473a6caf4446df430180a47ca3355&oe=5AC37B56"
#                    kr1.sendImageWithURL(msg.to, url)
#                    kr1.sendImageWithURL(msg.to, url1)
#                    kr1.sendImageWithURL(msg.to, url6)
#                    kr1.sendImageWithURL(msg.to, url7)
#================================ KRIS SCRIPT STARTED ==============================================#
            elif "google " in msg.text:
                if msg.from_ in admin:
                    a = msg.text.replace("google ","")
                    b = urllib.quote(a)
                    adhi1.sendText(msg.to,"Sedang Mencari kak...")
                    adhi1.sendText(msg.to, "https://www.google.com/" + b)
                    adhi1.sendText(msg.to,"Ketemu om ^")

            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u350cc7408cc6cc82e056ee046131f925"}
                adhi1.sendMessage(msg)

            elif "friendpp: " in msg.text:
                if msg.from_ in admin:
                    suf = msg.text.replace('friendpp: ','')
                    gid = adhi1.getAllContactIds()
                    for i in gid:
                        h = adhi1.getContact(i).displayName
                        gna = adhi1.getContact(i)
                        if h == suf:
                            adhi1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)

            elif "Checkmid: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace("Checkmid: ","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":saya}
                    adhi1.sendMessage(msg)
                    contact = adhi1.getContact(saya)
                    cu = adhi1.channel.getCover(saya)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        adhi1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        adhi1.sendText(msg.to,"Profile Picture " + contact.displayName)
                        adhi1.sendImageWithURL(msg.to,image)
                        adhi1.sendText(msg.to,"Cover " + contact.displayName)
                        adhi1.sendImageWithURL(msg.to,path)
                    except:
                        pass
                
            elif "Checkid: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace("Checkid: ","")
                    gid = adhi1.getGroupIdsJoined()
                    for i in gid:
                        h = adhi1.getGroup(i).id
                        group = adhi1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                adhi1.sendText(msg.to,md)
                                adhi1.sendMessage(msg)
                                adhi1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"
                
            elif msg.text in ["Flist"]:
                if msg.from_ in admin:
                    contactlist = adhi1.getAllContactIds()
                    kontak = adhi1.getContacts(contactlist)
                    num=1
                    msgs="═════════List Friend═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                    adhi1.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:
                if msg.from_ in admin:
                    kontak = adhi1.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════-"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    adhi1.sendText(msg.to, msgs)
                
            elif "Finfo: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Finfo: ','')
                    gid = adhi1.getAllContactIds()
                    for i in gid:
                        h = adhi1.getContact(i).displayName
                        contact = adhi1.getContact(i)
                        cu = adhi1.channel.getCover(i)
                        path = str(cu)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        if h == saya:
                            adhi1.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                            adhi1.sendText(msg.to,"Profile Picture " + contact.displayName)
                            adhi1.sendImageWithURL(msg.to,image)
                            adhi1.sendText(msg.to,"Cover " + contact.displayName)
                            adhi1.sendImageWithURL(msg.to,path)
                
            elif "Fpict: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Fpict: ','')
                    gid = adhi1.getAllContactIds()
                    for i in gid:
                        h = adhi1.getContact(i).displayName
                        gna = adhi1.getContact(i)
                        if h == saya:
                            adhi1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Flistmid"]:
                if msg.from_ in admin:
                    gruplist = adhi1.getAllContactIds()
                    kontak = adhi1.getContacts(gruplist)
                    num=1
                    msgs="═════════ʆίςϯ ƒɾίεηδʍίδ═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.mid)
                        num=(num+1)
                    msgs+="\n═════════ʆίςϯ ƒɾίεηδʍίδ═════════\n\nTotal Friend : %i" % len(kontak)
                    adhi1.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]:
                if msg.from_ in admin:
                    blockedlist = adhi1.getBlockedContactIds()
                    kontak = adhi1.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    adhi1.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:
                if msg.from_ in admin:
                    gruplist = adhi1.getGroupIdsJoined()
                    kontak = adhi1.getGroups(gruplist)
                    num=1
                    msgs="═════════List Grup═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.name)
                        num=(num+1)
                    msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                    adhi1.sendText(msg.to, msgs)
            
            elif msg.text in ["Glistmid"]:
                if msg.from_ in admin:
                    gruplist = adhi1.getGroupIdsJoined()
                    kontak = adhi1.getGroups(gruplist)
                    num=1
                    msgs="═════════List GrupMid═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.id)
                        num=(num+1)
                    msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                    adhi1.sendText(msg.to, msgs)
                    
            elif "Gimage: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Gimage: ','')
                    gid = adhi1.getGroupIdsJoined()
                    for i in gid:
                        h = adhi1.getGroup(i).name
                        gna = adhi1.getGroup(i)
                        if h == saya:
                            adhi1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Gname" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Gname','')
                    gid = adhi1.getGroup(msg.to)
                    adhi1.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Gcid" in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Gcid','')
                    gid = adhi1.getGroup(msg.to)
                    adhi1.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Gcinfo: " in msg.text:
                if msg.from_ in admin:
                    saya = msg.text.replace('Gcinfo: ','')
                    gid = adhi1.getGroupIdsJoined()
                    for i in gid:
                        h = adhi1.getGroup(i).name
                        group = adhi1.getGroup(i)
                        if h == saya:
                            try:
                                creator = group.creator.mid 
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': creator}
                                md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                                if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                                else: md += "\n\nKode Url : Diblokir"
                                if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                                else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                                adhi1.sendText(msg.to,md)
                                adhi1.sendMessage(msg)
                                adhi1.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                            except:
                                creator = "Error"

#            elif "Spamtag @" in msg.text:
#                _name = msg.text.replace("Spamtag @","")
#                _nametarget = _name.rstrip(' ')
#                gs = kr1.getGroup(msg.to)
#                for g in gs.members:
#                    if _nametarget == g.displayName:
#                        xname = g.displayName
#                        xlen = str(len(xname)+1)
#                        msg.contentType = 0
#                        msg.text = "@"+xname+" "
#                        msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        kr1.sendMessage(msg)
#                        print "Spamtag Berhasil."

            elif "playstore " in msg.text.lower():
                if msg.from_ in admin:
                    tob = msg.text.lower().replace("playstore ","")
                    adhi1.sendText(msg.to,"Sedang Mencari boss...")
                    adhi1.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                    adhi1.sendText(msg.to,"Ketemu boss ^")
                    
            elif 'wikipedia ' in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        wiki = msg.text.lower().replace("wikipedia ","")
                        wikipedia.set_lang("id")
                        pesan="Title ("
                        pesan+=wikipedia.page(wiki).title
                        pesan+=")\n\n"
                        pesan+=wikipedia.summary(wiki, sentences=3)
                        pesan+="\n"
                        pesan+=wikipedia.page(wiki).url
                        adhi1.sendText(msg.to, pesan)
                    except:
                            try:
                                pesan="Teks nya kepanjangan! ketik link dibawah aja\n"
                                pesan+=wikipedia.page(wiki).url
                                adhi1.sendText(msg.to, pesan)
                            except Exception as e:
                                adhi1.sendText(msg.to, str(e))

            elif "say " in msg.text.lower():
                if msg.from_ in admin:
                    say = msg.text.lower().replace("say ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    adhi1.sendAudio(msg.to,"hasil.mp3")
                
            elif msg.text in ["Gift 8","Gift8","gift8"]:
                if msg.from_ in admin:
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '8'}
                    msg.text = None
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    
                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    msg.text = None
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)

                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    msg.text = None
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)

                    msg.contentType = 9
                    msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '7'}
                    msg.text = None
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
    
            elif msg.text in ["Gift","gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                adhi1.sendMessage(msg)


            elif msg.text in ["Gift1"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '696d7046-843b-4ed0-8aac-3113ed6c0733',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                adhi1.sendMessage(msg)

            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '8fe8cdab-96f3-4f84-95f1-6d731f0e273e',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '7'}
                msg.text = None
                adhi1.sendMessage(msg)

            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'ae3d9165-fab2-4e70-859b-c14a9d4137c4',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                adhi1.sendMessage(msg)
            elif msg.text in ["Gcreator:inv"]:
                if msg.from_ in admin:
                    ginfo = adhi1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       adhi1.findAndAddContactsByMid(gCreator)
                       adhi1.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass

            elif msg.text in ["Gcreator:kick"]:
                if msg.from_ in admin:
                    ginfo = adhi1.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       adhi1.findAndAddContactsByMid(gCreator)
                       adhi1.kickoutFromGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
                   
            elif 'lirik ' in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        songname = msg.text.lower().replace('lirik ','')
                        params = {'songname': songname}
                        r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                        data = r.text
                        data = json.loads(data)
                        for song in data:
                            hasil = 'Lyric Lagu ('
                            hasil += song[0]
                            hasil += ')\n\n'
                            hasil += song[5]
                            adhi1.sendText(msg.to, hasil)
                    except Exception as wak:
                            adhi1.sendText(msg.to, str(wak))       
                   
            elif "Getcover @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]dp executing"
                    _name = msg.text.replace("Getcover @","")
                    _nametarget = _name.rstrip('  ')
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        adhi2.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = adhi1.getContact(target)
                                cu = adhi1.channel.getCover(target)
                                path = str(cu)
                                adhi1.sendImageWithURL(msg.to, path)
                            except:
                                pass
                    print "[Command]dp executed"
                
            elif "idline: " in msg.text:
                if msg.from_ in admin:
                    msgg = msg.text.replace('idline: ','')
                    conn = adhi1.findContactsByUserid(msgg)
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        adhi1.sendText(msg.to,"http://line.me/ti/p/~" + msgg)
                        adhi1.sendMessage(msg)
                        
            elif "reinvite" in msg.text.split():
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adhi1.getGroup(msg.to)
                        if group.invitee is not None:
                            try:
                                grCans = [contact.mid for contact in group.invitee]
                                adhi1.findAndAddContactByMid(msg.to, grCans)
                                adhi1.cancelGroupInvitation(msg.to, grCans)
                                adhi1.inviteIntoGroup(msg.to, grCans)
                            except Exception as error:
                                print error
                        else:
                            if wait["lang"] == "JP":
                                adhi1.sendText(msg.to,"No Invited")
                            else:
                                adhi1.sendText(msg.to,"Error")
                    else:
                        pass
                
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                adhi1.sendText(msg.to,van)
                
            elif msg.text in ["Restart"]:
                if msg.from_ in admin:
                    adhi1.sendText(msg.to, "Bot has been restarted")
                    restart_program()
                    print "@Restart"
                
            elif msg.text in ["time"]:
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bln = bulan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                adhi1.sendText(msg.to, rst)
                
            elif "image " in msg.text:
                if msg.from_ in admin:
                    search = msg.text.replace("image ","")
                    url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    print path
                    try:
                        adhi1.sendImageWithURL(msg.to,path)
                    except:
                        pass
                
            elif 'instagram ' in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        instagram = msg.text.lower().replace("instagram ","")
                        html = requests.get('https://www.instagram.com/' + instagram + '/?')
                        soup = BeautifulSoup(html.text, 'html5lib')
                        data = soup.find_all('meta', attrs={'property':'og:description'})
                        text = data[0].get('content').split()
                        data1 = soup.find_all('meta', attrs={'property':'og:image'})
                        text1 = data1[0].get('content').split()
                        user = "Name: " + text[-2] + "\n"
                        user1 = "Username: " + text[-1] + "\n"
                        followers = "Followers: " + text[0] + "\n"
                        following = "Following: " + text[2] + "\n"
                        post = "Post: " + text[4] + "\n"
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        detail = "**INSTAGRAM INFO USER**\n"
                        details = "\n**INSTAGRAM INFO USER**"
                        adhi1.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                        adhi1.sendImageWithURL(msg.to, text1[0])
                    except Exception as njer:
                    	adhi1.sendText(msg.to, str(njer))    
                	
            elif msg.text in ["Attack"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub4d829c38a9bcc4bf125fbd2a4167119',"}
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                    adhi1.sendMessage(msg)
                
            elif msg.text.lower() == '..':
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub4d829c38a9bcc4bf125fbd2a4167119',"}
                    adhi1.sendMessage(msg)    
#=================================KRIS SCRIPT FINISHED =============================================#
            
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Ban @","")
                        _nametarget = _name.rstrip()
                        gs = adhi1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            adhi1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    adhi1.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                                except:
                                    adhi1.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip()
                        gs = adhi1.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            adhi1.sendText(msg.to,_nametarget + " Not Found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    adhi1.sendText(msg.to,_nametarget + " Delete From Blacklist")
                                except:
                                    adhi1.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Ban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                adhi1.sendText(msg.to,_name + " Succes Add to Blacklist")
                            except:
                                adhi1.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Unban:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = adhi1.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"user does not exist")
                        pass
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                adhi1.sendText(msg.to,_name + " Delete From Blacklist")
                            except:
                                adhi1.sendText(msg.to,_name + " Not In Blacklist")
            elif msg.text in ["Clear"]:
                if msg.from_ in admin:
                    wait["blacklist"] = {}
                    adhi1.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text in ["Ban:on"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    adhi1.sendText(msg.to,"Send Contact")
            elif msg.text in ["Unban:on"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    adhi1.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        adhi1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        adhi1.sendText(msg.to,"Daftar Banlist")
                        num=1
                        msgs="*Blacklist*"
                        for mi_d in wait["blacklist"]:
                            msgs+="\n[%i] %s" % (num, adhi1.getContact(mi_d).displayName)
                            num=(num+1)
                        msgs+="\n*Blacklist*\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                        adhi1.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if msg.from_ in admin:
                    if wait["blacklist"] == {}:
                        adhi1.sendText(msg.to,"Tidak Ada Blacklist")
                    else:
                        adhi1.sendText(msg.to,"Daftar Blacklist")
                        h = ""
                        for i in wait["blacklist"]:
                            h = adhi1.getContact(i)
                            M = Message()
                            M.to = msg.to
                            M.contentType = 13
                            M.contentMetadata = {'mid': i}
                            adhi1.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adhi1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        num=1
                        cocoa = "══════════List Blacklist═════════"
                        for mm in matched_list:
                            cocoa+="\n[%i] %s" % (num, mm)
                            num=(num+1)
                            cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                        adhi1.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = adhi1.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            adhi1.sendText(msg.to,"Tidak ada Daftar Blacklist")
                            return
                        for jj in matched_list:
                            try:
                                adhi1.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass       
#==============================================#
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        adhi1.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        adhi1.sendText(msg.to,"decided not to comment")
#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif "Tb spamtag @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Tb spamtag @","")
                    _nametarget = _name.rstrip(' ')
                    gs = adhi1.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            xname = g.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "
                            msg.contentMetadata ={"MENTION":'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                            adhi1.sendMessage(msg)
                        else:
                            pass
                        
            elif ("Tb cium " in msg.text):
                if msg.from_ in admin:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           adhi1.kickoutFromGroup(msg.to,[target])
                           #adhi1.inviteIntoGroup(msg.to,[target])
                           adhi1.cancelGroupInvitation(msg.to,[target])
                       except:
                           adhi1.sendText(msg.to,"Error")
                           
            elif msg.text in ["list gc"]: #Melihat List Group
                if msg.from_ in admin:
                    gids = adhi1.getGroupIdsJoined()
                    h = ""
                    for i in gids:
                      #####gn = adhi1.getGroup(i).name
                      h += "[•]%s Member\n" % (adhi1.getGroup(i).name   +"👉"+str(len(adhi1.getGroup(i).members)))
                      adhi1.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["list gc2"]: 
                if msg.from_ in admin:
                    gid = adhi1.getGroupIdsJoined()
                    h = ""
                    for i in gid:
                      h += "[%s]:%s\n" % (adhi1.getGroup(i).name,i)
                      adhi1.sendText(msg.to,h)

            elif "Rasita " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Rasita ","")
                    if gid == "":
                        adhi1.sendText(msg.to,"Invalid group id")
                    else:
                        try:
                            adhi1.findAndAddContactsByMid(msg.from_)
                            adhi1.inviteIntoGroup(gid,[msg.from_])
                            adhi1.sendText(msg.to,"succes di invite boss, silahkan masuk...!!")
                        except:
                            adhi1.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")

            elif "Ts bye" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        ginfo = adhi1.getGroup(msg.to)
                        try:
                            adhi1.leaveGroup(msg.to)
                        except:
                            pass
            elif "T sita " in msg.text:
                if msg.from_ in admin:
                    gName = msg.text.replace("T sita ","")
                    ap = adhi1.getGroups([msg.to])
                    semua = [contact.mid for contact in ap[0].members]
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
            elif "#sita " in msg.text:
                if msg.from_ in admin:
                    gName = msg.text.replace("#sita ","")
                    ap = adhi1.getGroups([msg.to])
                    semua = findAndAddContactsByMid(Mi_d)
                    nya = ap[0].members
                    for a in nya:
                        Mi_d = str(a.mid)
                        klis=[adhi]
                        team=random.choice(klis)
                        adhi1.findAndAddContactsByMid(Mi_d)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        adhi1.createGroup(gName, semua)
                        team.findAndAddContactsByMid(Mi_d)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
                        team.createGroup(gName, semua)
            elif "recover" in msg.text:
                if msg.from_ in admin:
                    thisgroup = adhi1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    adhi1.createGroup("recover", mi_d)
                    adhi1.sendText(msg.to,"Success recover")
            elif "T spin" in msg.text:
                if msg.from_ in admin:
                    thisgroup = adhi1.getGroups([msg.to])
                    Mids = [contact.mid for contact in thisgroup[0].members]
                    mi_d = Mids[:33]
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.createGroup("Nah kan", mi_d)
                    adhi1.sendText(msg.to,"Success...!!!!")
            elif msg.text in ["Remove all chat"]:
                if msg.from_ in admin:
                    adhi1.removeAllMessages(op.param2)
                    adhi1.removeAllMessages(op.param2)
                    adhi1.sendText(msg.to,"Removed all chat Finish")
            elif msg.text in ["muach"]:
                if msg.from_ in admin:
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "ub4d829c38a9bcc4bf125fbd2a4167119',"}
                    adhi1.sendMessage(msg)
            elif msg.text in ["T-B-A","Tes"]:
                if msg.from_ in admin:
                    adhi1.sendText(msg.to,"masih aktif Sayang...!!!")
#===============================================
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots or admin:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        adhi1.kickoutFromGroup(op.param1,[op.param2])
                        G = adhi1.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        adhi1.updateGroup(G)
                    except:
                        try:
                            adhi1.kickoutFromGroup(op.param1,[op.param2])
                            G = adhi1.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            adhi1.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots or admin:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    adhi1.kickoutFromGroup(op.param1,[op.param2])
                    adhi1.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots or admin:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    adhi1.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            adhi1.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    adhi1.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots or admin:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = adhi1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    adhi1.updateGroup(G)
                    adhi1.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait['autoAdd'] == True:
                if (wait['message'] in [""," ","\n",None]):
                    pass
                else:
                    adhi1.sendText(op.param1,str(wait['message']))
        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = adhi1.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    adhi1.kickoutFromGroup(op.param1,[op.param3])
                    adhi1.updateGroup(G)
#        if op.type == 17:
#           if wait["Wc"] == True:
#               if op.param2 in Bots:
#                 return
#               ginfo = adhi1.getGroup(op.param1)
#               adhi1.sendText(op.param1, "╔═════════════\n║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n║" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
#               print "MEMBER HAS JOIN THE GROUP"
        if op.type == 17:
            if wait["Wc"] == True:
                if op.param2 in Bots:
                    return
                G = adhi1.getGroup(op.param1)
                h = adhi1.getContact(op.param2)
                adhi1.sendText(op.param1, "╔═════════════║Selamat Datang Di  " + str(ginfo.name) + "\n╠═════════════\n" + "║Founder =>>> " + str(ginfo.name) + " :\n|" + ginfo.creator.displayName + "\n╠═════════════\n" + "║😊Semoga Betah Kak 😘 \n╚═════════════")
                adhi1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
            if wait["Lv"] == True:
                if op.param2 in Bots:
                    return
                adhi1.sendText(op.param1, "╔═════════════\n║Baper Ya :v \n║Semoga Bahagia ya 😊 \n╚═════════════")
                adhi1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + h.pictureStatus)
                print "MEMBER HAS LEFT THE GROUP"
#------------------------------------------------------------------------------#

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        if op.type == 55:
            try:
                if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = adhi1.getContact(op.param2).displayName
                            Np = adhi1.getContact(op.param2).pictureStatus
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        adhi1.sendText(op.param1, "Hallo.. " + "☞ " + nick[0] + " ☜" + "\nNah jangan ngintip mulu 😁. . .\nGabung Chat yux 😉")
                                        adhi1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        adhi1.sendText(op.param1, "Hallo.. " + "☞ " + nick[1] + " ☜" + "\nJangan ngintip mulu napa kak.. 😏. . .\nMasuk ayo sini kak... 😆😂😛")
                                        adhi1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    adhi1.sendText(op.param1, "hallo.. " + "☞ " + Name + " ☜" + "\nJangan ngintip aja\nMasuk gabung chat ya...😋 😝")
                                    adhi1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass

        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in adhi1.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait['likeOn'] == True:
                   adhi1.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          adhi1.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = adhi1.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          adhi1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          adhi1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By BA👈 »»» http://line.me/ti/p/~jkp4678 «««")
          print "Like"
        except:
          pass
      else:
          print "Already Liked Om"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = adhi1.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    adhi1.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    adhi1.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉ąµţ๏ℓɨЌ€ By B-A👈 »»» http://line.me/ti/p/~jkp4678 «««")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Om"


while True:
    try:
        Ops = adhi1.fetchOps(adhi1.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(adhi1.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            adhi1.Poll.rev = max(adhi1.Poll.rev, Op.revision)
            bot(Op)
