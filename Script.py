class script(object):
    START_TXT = """๐แดสสแด {},

 ๐ ส ๐กแดแดแด ษช๐ Heast

๐จ'๐ ๐บ ๐ฅ๐๐๐พ๐๐ฝ๐๐ ๐๐๐๐๐ ๐ฌ๐บ๐๐บ๐๐พ๐ Bot
โข Build Version : V2.1.0 (BETA)
โข Speciality : Movie Provider
๐ข๐๐๐ผ๐ /help OR Help Button ๐๐ ๐๐ ๐ฅ๐๐๐ผ๐๐๐๐๐."""
    HELP_TXT = """๐แดสสแด {} Here is your Functions"""
    ABOUT_TXT = """<b>โฅ My name: {}
โฅ Creator: <a href='https://t.me/sangeeth006'>S-DEVIL</a>
โฅ Library: Pyrogram
โฅ Language: Python ๐น
โฅ Data Base: MongoDB
โฅ Bot Server: Heroku
โฅ Build Status: v2.1.0 [ Beta ]"""
    DONATION_TXT = """<b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง & ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b> 

โบโบ <b>๐๐จ๐ง๐๐ญ๐ข๐จ๐ง</b>

โชผ <b>๐๐จ๐ฎ ๐๐๐ง ๐๐จ๐ง๐๐ญ๐ ๐๐ง๐ฒ ๐๐ฆ๐จ๐ฎ๐ง๐ญ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐ณ. 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
- ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
- ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐จ๐ซ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/The_user_death><b>แดฉสแด๊ฐแด๊ฑแดส</b></a> แโโโโโโโโโโโโ

โบโบ <b>๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง</b>

โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
- ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
- ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/The_user_death><b>แดฉสแด๊ฐแด๊ฑแดส</b></a> แโโโโโโโโโโโโ"""
    PROMOTION_TXT = """<b>ใ ๐๐๐ข๐ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ข๐จ๐ง ใ</b>

โชผ <b>๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ก๐ข๐๐ก ๐๐จ๐ฎ ๐๐๐ง๐ญ ๐๐จ ๐๐ซ๐จ๐ฆ๐จ๐ญ๐ . 
<b>โโโโโโโโโแ Payment Methods แโโโโโโโโโ
- ๐๐ผ๐ผ๐ด๐น๐ฒ๐ฃ๐ฎ๐
- ๐ฃ๐ต๐ผ๐ป๐ฒ๐ฃ๐ฒ
_๐๐จ๐ง๐ญ๐๐๐ญ ๐๐ ๐๐ข๐ญ๐ก ๐๐จ๐ฎ๐ซ ๐๐จ๐ง๐ญ๐๐ง๐ญ ๐๐ง๐ ๐๐ง๐จ๐ฐ ๐๐๐จ๐ฎ๐ญ ๐๐ก๐ ๐๐๐ฒ๐ฆ๐๐ง๐ญ ๐๐ง๐๐จ_
โโโโโโโโโโโโแ <a href=https://t.me/The_user_death><b>แดฉสแด๊ฐแด๊ฑแดส</b></a> แโโโโโโโโโโโโ""" 
    FILE_TXT = """The Batch Module../

<b>.By Using This MODUL you Can Store Files In My DataBase AND I Will Give You A Permanent Link To Access The Saved Files. ๐ธ๐ต ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ ๐ฟ๐๐ฑ๐ป๐ธ๐ฒ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐ด๐ฝ๐ณ ๐๐ท๐ด ๐ต๐ธ๐ป๐ ๐ป๐ธ๐ฝ๐บ ๐พ๐ฝ๐ป๐  ๐พ๐ ๐๐พ๐ ๐๐ฐ๐ฝ๐ ๐๐พ ๐ฐ๐ณ๐ณ ๐ต๐ธ๐ป๐ด๐ ๐ต๐๐พ๐ผ ๐ฐ  ๐ฟ๐๐ธ๐๐ฐ๐๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ๐ ๐ผ๐๐๐ ๐ผ๐ฐ๐บ๐ด ๐ผ๐ด ๐ฐ๐ณ๐ผ๐ธ๐ฝ ๐พ๐ฝ ๐๐ท๐ด ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ฐ๐ฒ๐ฒ๐ด๐๐ ๐ต๐ธ๐ป๐ด๐.</b>
โชผ Commands

โช /plink โบโบ <b>Reply To Any Media To Get The Link .</b>
โช /pbatch โบโบ <b>Use Your Media Link With This Command .</b>
โช /batch โบโบ <b>To Create Link For Multy Files</b>

โชผ ๐๐ฑ๐๐ฆ๐ฉ๐ฅ๐ โบ

<code>/batch https://t.me/FPHDMOVE/3 https://t.me/FPHDMOVE/8</code>
"""

    
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
โข/whois :-give a user full details"""
    CLONE_TXT ="""<b>CLONE MODULE</b>
Note:- This Function Help To Clone BOt Like This And Also Develope Bot As Your Wish
โข/clone - Help To Clone This Bot"""
    FUN_TXT ="""<b>Gแดแดแดs</b> 
    
<b>Some dank for fun or whatever!</b>
 
๐ฃ. /dice - Role The Dice
๐ค. /Throw ๐๐ /Dart - To Make Dart
3. /Runs - Some Random Dialogues
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /ikka - Fun with ikka
6. /luck or /cownd - Spin And Try Your Luck
7. /aunty - Chat or Fun with anty"""
    DEPLOY_TXT = """ ๐ Sorry bro """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and The Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
โข /filter - <code>add a filter in chat</code>
โข /filters - <code>list all the filters of a chat</code>
โข /del - <code>delete a specific filter in chat</code>
โข /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>SONG DOWNLOAD MODULE</b>

<b>๊ฑแดษดษข แดแดแดกษดสแดแดแด ๊ฐแดแดแดแดสแด, For This Feature You Can Download Any Music. Work Only On Group../</b>

<b>COMMANDS</b>

โบ /song SONG NAME 

แดกแดสแด แดษดสy แดษด ษขสแดแดแดฉ"""
    
    TOR_TXT = """Help: <b>Torrent Search</b>
<b>Commands and Usage</b>:
โข /torrent or /tor : Get Your Torrent Link From Various Resource.
<b>NOTE:</b>
โข Heast should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    
    IMG_TXT = """If You Want To Make A image Of Text send
/hand <anything> to Get the Photo"""

    FONTS_TXT = """ Want Some Stylish fonts send /font <anything>"""

    
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin A Message../</b>

=><b>ALL The Pin Releated Module Will See Here</b>

โ /pin :- To Pin The Message In Your Chat
โ /unpin :- To UNPIN The Current Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

โข /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS ๐ค module:</b>

Translate text to speech

<b>Commands and Usage:</b>

โข /tts <text> : convert text to speech

<b>NOTE:</b>

โข IMDb should have admin privillage.
โข These commands works on both pm and group.
โข IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>๐ Ping:</b>

- /pings - To know your pings

โข This commands can be used in pms and groups
โข This commands can be used buy everyone in the groups and bots pm
โข Share us for more features"""
    TELE_TXT = """<b>โซ๏ธHELP: Telegraphโช๏ธ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

๐คง /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

โข This Command Is Available in goups and pms
โข This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>PRIVATE BOT FOR YOU</b>
<b>โบ Do You Want A Bot Like This </b>
<b>โบ With All Your Creadets</b>
<b>โบ With Your Ownership</b>"""

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

<b>๐ฐ๐๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ ๐๐ท๐ด ๐ต๐ด๐ฐ๐๐๐๐ด ๐๐พ ๐ต๐ธ๐ป๐๐ด๐ ๐ฐ๐ฝ๐ณ ๐๐ฐ๐๐ด ๐๐ท๐ด ๐ต๐ธ๐ป๐ด๐ ๐ฐ๐๐๐พ๐ผ๐ฐ๐๐ธ๐ฒ๐ฐ๐ป๐ป๐ ๐ต๐๐พ๐ผ ๐ฒ๐ท๐ฐ๐ฝ๐ฝ๐ด๐ป ๐๐พ ๐ถ๐๐พ๐๐ฟ. ๐๐พ๐ ๐ฒ๐ฐ๐ฝ ๐๐๐ด ๐๐ท๐ด ๐ต๐พ๐ป๐ป๐พ๐๐ธ๐ฝ๐ถ ๐ฒ๐พ๐ผ๐ผ๐ฐ๐ฝ๐ณ๐ ๐๐พ ๐พ๐ฝ ๐ฐ๐ฝ๐ณ ๐พ๐ต๐ต ๐๐ท๐ด ๐ฐ๐๐๐พ๐ต๐ธ๐ป๐๐ด๐ ๐ธ๐ฝ ๐๐พ๐๐ ๐ถ๐๐พ๐๐ฟ.../</b>

<b>COMMANDS :-
<b>โบ /autofilter on - ENABLE AUTOFILTER IN GROUP.</b>
<b>โบ /autofilter off - DISABLE AUTOFILTER IN GROUP.</b>
<b>โบ /set_template - Set IMDB Template For AUTO FILTER BOT.</b>
<b>โบ /get_template - Get Current IMDB Template Of AUTO FILTER BOT.</b>

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
โข /connect  - <code>connect a particular chat to your PM</code>
โข /disconnect  - <code>disconnect from a chat</code>
โข /connections - <code>list all your connections</code>"""
    SEARCH_TXT = """Help: <b>IMDb</b>
Search many things without leaving telegram!
<b>Commands and Usage:</b>
โข /imdb  - get the film information from IMDb source.
โข /search  - get the film information from various sources.
<b>NOTE:</b>
โข BOT should have admin privillage.
โข More search tools can be found on inline.
โข Those commands works on both pm and group."""
    INFO_TXT = """Help: <b>Information</b>
Get information about something!
<b>Commands and Usage:</b>
โข /id - get id of a specified user.
โข /info  - get information about a user.
โข /json - get the json details of a message.
<b>NOTE:</b>
โข Bot should have admin privillage.
โข These commands works on both pm and group.
โข These commands can be used by any group member."""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
โข /logs - <code>to get the rescent errors</code>
โข /stats - <code>to get status of files in db.</code>
โข /status - For getting bot and heroku status
โข /delete - <code>to delete a specific file from db.</code>
โข /users - <code>to get list of my users and ids.</code>
โข /chats - <code>to get list of the my chats and ids </code>
โข /leave  - <code>to leave from a chat.</code>
โข /disable  -  <code>do disable a chat.</code>
โข /ban_user  - <code>to ban a user.</code>
โข /unban_user  - <code>to unban a user.</code>
โข /channel - <code>to get list of total connected channels</code>
โข /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>โบ T-FILES: <code>{}</code></b>
<b>โบ T-USER: <code>{}</code></b>
<b>โบ T-CHATS: <code>{}</code></b>
<b>โบ USED-S: <code>{}</code> </b>
<b>โบ F-STORAGE: <code>{}</code> </b>"""
    LOG_TEXT_G = """#๐๐๐ฐ๐๐ซ๐จ๐ฎ๐ฉ
    
<b> ๐๐ซ๐จ๐ฎ๐ฉ โชผ {}(<code>{}</code>)</b>
<b> ๐๐จ๐ญ๐๐ฅ ๐๐๐ฆ๐๐๐ซ๐ฌ โชผ <code>{}</code></b>
<b> ๐๐๐๐๐ ๐๐ฒ โชผ {}</b>
"""
    LOG_TEXT_P = """#๐๐๐ฐ๐๐ฌ๐๐ซ
    
<b> ๐๐ - <code>{}</code></b>
<b> ๐๐๐ฆ๐ - {}</b>
"""
    REPORT_TXT = """โค ๐๐๐ฅ๐ฉ: Rแดแดแดสแด โ ๏ธ

This Is The Command To Help To Report A Message Or A User TO The Admin Of The Respective Group.Don't Misuse This Command.../ 

๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/report ๐๐ @admins - ๐ณ๐ ๐๐พ๐๐๐๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐บ๐ฝ๐๐๐๐ (๐๐พ๐๐๐ ๐๐ ๐บ ๐๐พ๐๐๐บ๐๐พ)."""

    CORONA_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ข๐๐๐๐ฝ

This Command Help You To Know Daily Information About Covid../

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /covid - ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐๐๐ ๐๐บ๐๐พ ๐๐ ๐๐พ๐ ๐ผ๐๐๐๐ฝ๐พ ๐๐๐ฟ๐๐๐๐บ๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
<code>/covid ๐จ๐๐ฝ๐๐บ</code>"""

    URLSHORT_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ด๐๐ ๐๐๐๐๐๐๐พ๐

This Command Help To Short A Command../ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /short: ๐๐๐พ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐๐๐ ๐๐๐๐ ๐๐๐๐ ๐๐ ๐๐พ๐ ๐๐๐๐๐๐พ๐ฝ ๐๐๐๐๐

โ๐ค๐๐บ๐๐๐๐พ:
<code>/short https://youtu.be/AB9CdEfG8ch0</code>"""

    VIDEO_TXT ="""Help To Download A Video From Youtube

โข ๐๐ด๐ข๐จ๐ฆ
๐ ๐ฐ๐ถ ๐๐ข๐ฏ ๐๐ฐ๐ธ๐ฏ๐ญ๐ฐ๐ข๐ฅ ๐๐ฏ๐บ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ณ๐ฐ๐ฎ ๐ ๐ฐ๐ถ๐ต๐ถ๐ฃ๐ฆ

๐๐ค๐ฌ ๐๐ค ๐๐จ๐
โข ๐๐บ๐ฑ๐ฆ /video or /mp4 ๐๐ฏ๐ฅ (https://youtu.be/AB9CdEfG8ch0)
โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ:
<code>/mp4 https://youtu.be/AB9CdEfG8ch0</code>
<code>/video https://youtu.be/AB9CdEfG8ch0</code>"""

    ZOMBIES_TXT = """Help You To Kick A user../

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
โข /inkick - command with required arguments and i will kick members from group.
โข /instatus - to check current status of chat member from group.
โข /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
โข /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
โข /dkick - to kick deleted accounts."""

    IMAGE_TXT = """โค ๐๐๐ฅ๐ฉ: Iแดแดษขแด

This Command Help A Edit A Image Easly../ 

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช ๐ฉ๐๐๐ ๐๐พ๐๐ฝ ๐๐พ ๐บ ๐๐๐บ๐๐พ ๐๐ ๐พ๐ฝ๐๐ โจ
"""

    STICKER_TXT = """You Can Use This Moudel To Find A sticker.
โข ๐๐๐๐๐
To Get Sticker ID
 
๐๐ค๐ฌ ๐๐ค ๐๐จ๐
 
โ Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """Help To Download Any You Tube Thumnail
    
๐๐ค๐ฌ ๐๐ค ๐๐จ๐
๐๐บ๐ฑ๐ฆ /ytthumb ๐๐ฏ๐ฅ ๐๐ช๐ฅ๐ฆ๐ฐ ๐๐ช๐ฏ๐ฌ

โข ๐๐น๐ข๐ฎ๐ฑ๐ญ๐ฆ
<code>/ytthumb https://youtu.be/AB9CdEfG8hi0</code>"""

    ABOOK_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ ๐๐ฝ๐๐๐ป๐๐๐

YOU CAN CONVERT A PDF FILE TO A AUDIO FILE WITH THIS COMMANDโฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช /audiobook: ๐ฑ๐พ๐๐๐ ๐๐๐๐ ๐ผ๐๐๐๐บ๐๐ฝ ๐๐ ๐บ๐๐ ๐ฏ๐ฃ๐ฅ ๐๐ ๐๐พ๐๐พ๐๐บ๐๐พ ๐๐๐พ ๐บ๐๐ฝ๐๐"""

    GTRANS_TXT = """โค ๐๐๐ฅ๐ฉ: ๐ฆ๐๐๐๐๐พ ๐ณ๐๐บ๐๐๐๐บ๐๐พ๐

THIS COMMAND HELP YOU TO TRANSLATE A TEXT TO ANY LANGUAGE YOU WANT.THIS COMMAND WORK ON BOTH GROUP AND PM โฏ

โค ๐๐จ๐ฆ๐ฆ๐๐ง๐๐ฌ ๐๐ง๐ ๐๐ฌ๐๐ ๐:

โช/tr - ๐ณ๐ ๐๐๐บ๐๐๐๐บ๐๐พ๐ ๐๐พ๐๐๐ ๐๐ ๐บ ๐๐๐พ๐ผ๐๐ฟ๐ผ ๐๐บ๐๐๐๐บ๐๐พ

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tr ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐บ๐๐๐๐บ๐๐พ ๐ผ๐๐ฝ๐พ

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ ๐๐
โข ๐พ๐ = ๐ค๐๐๐๐๐๐
โข ๐๐ = ๐ฌ๐บ๐๐บ๐๐บ๐๐บ๐
โข ๐๐ = ๐ง๐๐๐ฝ๐"""

    ALIVE_TXT = """ALIVE MOD
โข /alive - check me alive or dead๐คง
Just for a rasam๐"""

    GROUP_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    CHANNEL_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    MAIN_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    FILTER_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    NE_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    IQ_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    CARBON_TXT = """ <b>Carbon Moudel</b>
    
<b>YOU CAN BEAUTIFY YOUR CODES BY USING THIS FEATURE...</b>

<b>COMMAND.!</b>

<b>/carbon โบโบ Replay To Any Message</b>
<b>Work ON Both Group AND PM</b>"""

    NEX_TXT = """๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    EXTRA_TXT = """Extra Modulbot
NOTE:
these are the extra features of this bot
"""

    MOD_TXT = """
๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:
"""

    ANYFILECAPTION_TXT = """<b>๐ฝ File Name:</b> <code> {file_name}</code>     
   
<b>๐ฏ Size:</b> <code>{file_size}</code>

<code>โณ Error?</code> <a href='๐ญ'>CLICK HERE TO JOIN & TRY AGAIN!</a>'>CLICK HERE TO JOIN & TRY AGAIN!</a>"""

    NXE_TXT = """
๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:
"""

    MAX_TXT = """ ๐ง๐พ๐๐พ ๐๐ ๐๐๐พ ๐ด๐๐๐บ๐ ๐ผ๐๐๐๐บ๐๐ฝ๐:"""

    COR_TXT = """Creators โค
- Thanks To Dan For His Awesome Library
- Thanks To Mahesh For His Awesome Media-Search-bot
- Thanks To <a href='https://github.com/trojanzhex'>Trojanz</a> for Their Awesome Unlimited Filter Bot And AutoFilterBoT
- Thanks To <a href='https://t.me/TeamEvamaria'>Eva Mari Team</a> A amazing combination of this repo 
- Thanks To <a href='https://t.me/sangeeth006'>s-devil</a> To create me 
- Thanks To All Everyone In This Journey"""

    RESTRIC_TXT = """โค ๐๐๐ฅ๐ฉ: Mแดแดแด ๐ซ

THESE ARE THE COMMANDS A GROUP ADMIN CAN USE TO MANAGE THEIR GROUP MORE EFFICIENTLY.

โช/ban: ๐ณ๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐ฟ๐๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unban: ๐ณ๐ ๐๐๐ป๐บ๐ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tban: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐ป๐บ๐ ๐บ ๐๐๐พ๐.
โช/mute: ๐ณ๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/unmute: ๐ณ๐ ๐๐๐๐๐๐พ ๐บ ๐๐๐พ๐ ๐๐ ๐๐๐พ ๐๐๐๐๐.
โช/tmute: ๐ณ๐ ๐๐พ๐๐๐๐๐บ๐๐๐๐ ๐๐๐๐พ ๐บ ๐๐๐พ๐.

โค ๐ญ๐๐๐พ:
๐ถ๐๐๐๐พ ๐๐๐๐๐ /tmute ๐๐ /tban ๐๐๐ ๐๐๐๐๐๐ฝ ๐๐๐พ๐ผ๐๐ฟ๐ ๐๐๐พ ๐๐๐๐พ ๐๐๐๐๐.

โ๐ค๐๐บ๐๐๐๐พ: /๐๐ป๐บ๐ 2๐ฝ ๐๐ /๐๐๐๐๐พ 2๐ฝ.
๐ธ๐๐ ๐ผ๐บ๐ ๐๐๐พ ๐๐บ๐๐๐พ๐: ๐/๐/๐ฝ. 
 โข ๐ = ๐๐๐๐๐๐พ๐
 โข ๐ = ๐๐๐๐๐
 โข ๐ฝ = ๐ฝ๐บ๐๐"""
    CREATOR_REQUIRED = """โ<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "โ **Arguments Required**"
      
    KICKED = """โ๏ธ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """๐ฎ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """โ<b>เดเดจเตเดจเต Admin เดเดเตเดเดคเตเดค เดธเตเดฅเดฒเดคเตเดคเต เดเดพเตป เดจเดฟเดเตเดเดฟเดฒเตเดฒ เดชเตเดเตเดตเดพ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """โ๏ธ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>เดเดชเตเดชเต เดเดฒเตเดฒเดพเด เดเดเดฟเดเตเดเตเดฎเดพเดฑเตเดฑเดฟ เดคเดฐเดพเด...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
