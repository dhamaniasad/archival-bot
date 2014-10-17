archival-bot
============

Python script to submit a URL to multiple archival services
____

#### Usage:
Put a file named urls.txt in the directory the script is being run from. The file should contain all the URLs that you want to archive, and have only 1 URL per line. 
Next, run the script using `python archivalbot.py`.
You will get a file out.txt as the output, which will contain a list of all the archived versions of the URLs.

Sample urls.txt
```
http://www.wikipedia.org
https://github.com/dhamaniasad/archival-bot
```

Sample out.txt
```
http://www.wikipedia.org:
http://www.peeep.us/c57a737e
http://web.archive.org/web/20141017193743/http://www.wikipedia.org
http://archive.today/r9uus
https://github.com/dhamaniasad/archival-bot:
http://www.peeep.us/8c8093ae
http://web.archive.org/web/20141017193745/https://github.com/dhamaniasad/archival-bot
http://archive.today/3yO5N
```
