class script(object):
    START_TXT = """𝗛ᴇʟʟᴏ {},

 𝗠ʏ 𝗡ᴀᴍᴇ ɪ𝘀 vadivelu

𝖨'𝗆 𝖺 𝖥𝗋𝗂𝖾𝗇𝖽𝗅𝗒 𝗀𝗋𝗈𝗎𝗉 𝖬𝖺𝗇𝖺𝗀𝖾𝗋 Bot
• Build Version : V2.1.0 (BETA)
• Speciality : Movie Provider
𝖢𝗅𝗂𝖼𝗄 /help 𝗍𝗈 𝗆𝗒 𝖥𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝗌."""
    HELP_TXT = """𝗛ᴇʟʟᴏ {} Here is your Functions"""
    ABOUT_TXT = """<b>➥ My name: {}
➥ Creator: <a href='https://t.me/sangeeth006'>S-DEVIL</a>
➥ Library: Pyrogram
➥ Language: Python 𝟹
➥ Data Base: MongoDB
➥ Bot Server: Heroku
➥ Build Status: v2.0.1 [ Beta ]"""
    DONATION_TXT = """<b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧 & 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b> 

›› <b>𝐃𝐨𝐧𝐚𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
- 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
- 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/The_user_death><b>ᴩʀᴏꜰᴇꜱᴇʀ</b></a> ᚛━━━━━━━━━━━━

›› <b>𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
- 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
- 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/The_user_death><b>ᴩʀᴏꜰᴇꜱᴇʀ</b></a> ᚛━━━━━━━━━━━━"""
    PROMOTION_TXT = """<b>〄 𝐏𝐚𝐢𝐝 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 〄</b>

⪼ <b>𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐖𝐡𝐢𝐜𝐡 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐓𝐨 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 . 
<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━
- 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
- 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐂𝐨𝐧𝐭𝐞𝐧𝐭 𝐀𝐧𝐝 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/The_user_death><b>ᴩʀᴏꜰᴇꜱᴇʀ</b></a> ᚛━━━━━━━━━━━━""" 
    FILE_TXT = """The Batch Module../

<b>.By Using This MODUL you Can Store Files In My DataBase AND I Will Give You A Permanent Link To Access The Saved Files. 𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝚆 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈  𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰  𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙽 𝚃𝙷𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝙵𝙸𝙻𝙴𝚂.</b>
⪼ Commands

➪ /plink ›› <b>Reply To Any Media To Get The Link .</b>
➪ /pbatch ›› <b>Use Your Media Link With This Command .</b>
➪ /batch ›› <b>To Create Link For Multy Files</b>

⪼ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

<code>/batch https://t.me/FPHDMOVE/3 https://t.me/FPHDMOVE/8</code>
"""

    LYRICS_TXT ="""LYRICS Module"""
    
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    FUN_TXT ="""<b>Gᴀᴍᴇs</b> 
    
<b>Some dank for fun or whatever!</b>
 
𝟣. /dice - Role The Dice
𝟤. /Throw 𝗈𝗋 /Dart - To Make Dart
3. /Runs - Some Random Dialogues
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin And Try Your Luck"""
    DEPLOY_TXT = """ 😏 Sorry bro """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and The Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>SONG DOWNLOAD MODULE</b>

<b>ꜱᴏɴɢ ᴅᴏᴡɴʟᴏᴀᴅ ꜰᴇᴀᴛᴜʀᴇ, For This Feature You Can Download Any Music. Work Only On Group../</b>

<b>COMMANDS</b>

› /song SONG NAME 

ᴡᴏʀᴋ ᴏɴʟy ᴏɴ ɢʀᴏᴜᴩ"""
    
    TOR_TXT = """Help: <b>Torrent Search</b>
<b>Commands and Usage</b>:
• /torrent or /tor : Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
• IMDb should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    
    IMG_TXT = """If You Want To Make A image Of Text send
/hand <anything> to Get the Photo"""

    FONTS_TXT = """ Want Some Stylish fonts send /font <anything>"""

    BOTSTATUS_TXT = """Send /status for getting bot and heroku status"""

    MAMMOKA_TXT = """𝐂𝐀𝐔𝐓𝐈𝐎𝐍 : <b>Iᴋᴋᴀ Fᴀɴs Aʀᴇ Pʀᴏʜɪʙɪᴛᴇᴅ Nᴇᴀʀ Tʜɪs ᴀʀᴇᴀ</b> 
    
    <b> 𝙍𝙀𝘼𝙎𝙊𝙉: </b>
    Tʜɪs ғɪʟᴛᴇʀ ᴄᴏɴᴛᴀɪɴs ᴛᴏxɪᴄ ғᴜɴɴʏ sᴛɪᴄᴋᴇʀs 😂😂😂
    
    <b> 𝘾𝙊𝙈𝙈𝘼𝙉𝘿: </b> /ikka ☺☺
    
    """

    AUNTY_TXT ="""<b>THE GREAT MALLU AUNTY</b>
   
 Sᴇɴᴅ /aunty, 
 
 Tʜᴇɴ Mᴀʟʟᴜ Aᴜɴᴛʏ Wɪʟʟ Tᴇxᴛ Yᴏᴜ Sᴏᴍᴇ Jᴏᴋᴇs 😂😂 """
    
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin A Message../</b>

=><b>ALL The Pin Releated Module Will See Here</b>

◉ /pin :- To Pin The Message In Your Chat
◉ /unpin :- To UNPIN The Current Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>🌟 Ping:</b>

- /pings - To know your pings

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    TELE_TXT = """<b>▫️HELP: Telegraph▪️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>PRIVATE BOT FOR YOU</b>
<b>› Do You Want A Bot Like This </b>
<b>› With All Your Creadets</b>
<b>› With Your Ownership</b>
<b>› CONTACT ME <a href=https://t.me/The_user_death>ᴩʀᴏꜰᴇꜱᴇʀ</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """Here is the help for the <b>Purges</b> module:
<b>Admin only</b>:
- /purge: deletes all messages between this and the replied to message.
- /del: deletes the message you replied to.
<b>Examples</b>:
- Delete all messages from the replied to message, until now.
-> /purge"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-This Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. The Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/FilmPirateGroup)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>AUTOFILTER MODULE..</b>

<b>𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙰𝙽𝙳 𝚂𝙰𝚅𝙴 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲𝙰𝙻𝙻𝚈 𝙵𝚁𝙾𝙼 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙶𝚁𝙾𝚄𝙿. 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙴 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚃𝙾 𝙾𝙽 𝙰𝙽𝙳 𝙾𝙵𝙵 𝚃𝙷𝙴 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿.../</b>

<b>COMMANDS :-
<b>› /autofilter on - ENABLE AUTOFILTER IN GROUP.</b>
<b>› /autofilter off - DISABLE AUTOFILTER IN GROUP.</b>
<b>› /set_template - Set IMDB Template For AUTO FILTER BOT.</b>
<b>› /get_template - Get Current IMDB Template Of AUTO FILTER BOT.</b>

Channel Filter

<b> If you need to change into Channel Filter mode use /settings in your group
"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    SEARCH_TXT = """Help: <b>IMDb</b>
Search many things without leaving telegram!
<b>Commands and Usage:</b>
• /imdb  - get the film information from IMDb source.
• /search  - get the film information from various sources.
<b>NOTE:</b>
• BOT should have admin privillage.
• More search tools can be found on inline.
• Those commands works on both pm and group."""
    INFO_TXT = """Help: <b>Information</b>
Get information about something!
<b>Commands and Usage:</b>
• /id - get id of a specified user.
• /info  - get information about a user.
• /json - get the json details of a message.
<b>NOTE:</b>
• Bot should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member."""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>› T-FILES: <code>{}</code></b>
<b>› T-USER: <code>{}</code></b>
<b>› T-CHATS: <code>{}</code></b>
<b>› USED-S: <code>{}</code> </b>
<b>› F-STORAGE: <code>{}</code> </b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b> 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b> 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b> 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b> 𝐈𝐃 - <code>{}</code></b>
<b> 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """➤ 𝐇𝐞𝐥𝐩: Rᴇᴘᴏʀᴛ ⚠️

This Is The Command To Help To Report A Message Or A User TO The Admin Of The Respective Group.Don't Misuse This Command.../ 

𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/report 𝗈𝗋 @admins - 𝖳𝗈 𝗋𝖾𝗉𝗈𝗋𝗍 𝖺 𝗎𝗌𝖾𝗋 𝗍𝗈 𝗍𝗁𝖾 𝖺𝖽𝗆𝗂𝗇𝗌 (𝗋𝖾𝗉𝗅𝗒 𝗍𝗈 𝖺 𝗆𝖾𝗌𝗌𝖺𝗀𝖾)."""

    CORONA_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖢𝗈𝗏𝗂𝖽

This Command Help You To Know Daily Information About Covid../

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /covid - 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾 𝗍𝗈 𝗀𝖾𝗍 𝖼𝗈𝗏𝗂𝖽𝖾 𝗂𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖴𝗋𝗅 𝗌𝗁𝗈𝗋𝗍𝗇𝖾𝗋

This Command Help To Short A Command../ 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /short: 𝗎𝗌𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗐𝗂𝗍𝗁 𝗒𝗈𝗎𝗋 𝗅𝗂𝗇𝗄 𝗍𝗈 𝗀𝖾𝗍 𝗌𝗁𝗈𝗋𝗍𝖾𝖽 𝗅𝗂𝗇𝗄𝗌

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾:
<code>/short https://youtu.be/AB9CdEfG8ch0</code>"""

    VIDEO_TXT ="""Help To Download A Video From Youtube

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/AB9CdEfG8ch0)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
<code>/mp4 https://youtu.be/AB9CdEfG8ch0</code>
<code>/video https://youtu.be/AB9CdEfG8ch0</code>"""

    ZOMBIES_TXT = """Help You To Kick A user../

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """➤ 𝐇𝐞𝐥𝐩: Iᴍᴀɢᴇ

This Command Help A Edit A Image Easly../ 

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ 𝖩𝗎𝗌𝗍 𝗌𝖾𝗇𝖽 𝗆𝖾 𝖺 𝗂𝗆𝖺𝗀𝖾 𝗍𝗈 𝖾𝖽𝗂𝗍 ✨
"""

    STICKER_TXT = """You Can Use This Moudel To Find A sticker.
• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """Help To Download Any You Tube Thumnail
    
𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/AB9CdEfG8hi0</code>"""

    ABOOK_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖠𝗎𝖽𝗂𝗈𝖻𝗈𝗈𝗄

YOU CAN CONVERT A PDF FILE TO A AUDIO FILE WITH THIS COMMAND✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪ /audiobook: 𝖱𝖾𝗉𝗅𝗒 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝖺𝗇𝖽 𝗍𝗈 𝖺𝗇𝗒 𝖯𝖣𝖥 𝗍𝗈 𝗀𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝗍𝗁𝖾 𝖺𝗎𝖽𝗂𝗈"""

    GTRANS_TXT = """➤ 𝐇𝐞𝐥𝐩: 𝖦𝗈𝗈𝗀𝗅𝖾 𝖳𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋

THIS COMMAND HELP YOU TO TRANSLATE A TEXT TO ANY LANGUAGE YOU WANT.THIS COMMAND WORK ON BOTH GROUP AND PM ✯

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    ALIVE_TXT = """ALIVE MOD
• /alive - check me alive or dead🤧
Just for a rasam😂"""

    GROUP_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    CHANNEL_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    MAIN_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    FILTER_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    NE_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    IQ_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    CARBON_TXT = """ <b>Carbon Moudel</b>
    
<b>YOU CAN BEAUTIFY YOUR CODES BY USING THIS FEATURE...</b>

<b>COMMAND.!</b>

<b>/carbon ›› Replay To Any Message</b>
<b>Work ON Both Group AND PM</b>"""

    NEX_TXT = """𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    EXTRA_TXT = """Extra Modulbot
NOTE:
these are the extra features of this bot
"""

    MOD_TXT = """
𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:
"""

    ANYFILECAPTION_TXT = """<b>📽 File Name:</b> <code> {file_name}</code>     
   
<b>🗯 Size:</b> <code>{file_size}</code>

<code>⏳ Error?</code> <a href='😭'>CLICK HERE TO JOIN & TRY AGAIN!</a>'>CLICK HERE TO JOIN & TRY AGAIN!</a>"""

    NXE_TXT = """
𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:
"""

    MAX_TXT = """ 𝖧𝖾𝗋𝖾 𝗂𝗌 𝗍𝗁𝖾 𝖴𝗌𝗎𝖺𝗅 𝖼𝗈𝗆𝗆𝖺𝗇𝖽𝗌:"""

    COR_TXT = """Creators ❤
- Thanks To Dan For His Awesome Library
- Thanks To Mahesh For His Awesome Media-Search-bot
- Thanks To <a href='https://github.com/trojanzhex'>Trojanz</a> for Their Awesome Unlimited Filter Bot And AutoFilterBoT
- Thanks To <a href='https://t.me/TeamEvamaria'>Eva Mari Team</a> A amazing combination of this repo 
- Thanks To <a href='https://t.me/sangeeth006'>s-devil</a> To create me 
- Thanks To All Everyone In This Journey"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

THESE ARE THE COMMANDS A GROUP ADMIN CAN USE TO MANAGE THEIR GROUP MORE EFFICIENTLY.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
