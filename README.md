# redump-dat-url-get
Gets DAT download URLs from redump.info. It works by parsing the HTML to get all the links in the `main` element with the link text "Dat".

Usage: `redump-dat-url-get DOWNLOAD_PAGE_URL`  
e.g. `redump-dat-url-get 'https://redump.info/downloads'`

Then you can pipe that to a file or directly to another program:  
e.g. `redump-dat-url-get 'https://redump.info/downloads' | wget --content-disposition -i -` to download all the DATs to the current folder.
