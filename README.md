# Deezer Downloader

Download music directly from deezer.

You will need a file `settings.ini` file in your `~/.config/deezer-dl`.

Only works for linux. Don't hesitate to open an issue for any feature request.

```ini
;;; base config

[deezer]
; valid arl cookie value
; login manually using your web browser and take the arl ookie
cookie_arl = <deezer-cookie>

; download flac files (if False mp3 is used)
flac_quality = True

; user id for favorite song to be downloaded
user_id = "00000000"

; music diriectory
music_dir = /tmp/deezer-dl
```

## Install

```
$ pip install --user https://github.com/rllola/deezer-dl.git
```

## Feature

```
usage: deezer-dl [-h] {check,download} ...

optional arguments:
  -h, --help        show this help message and exit

command:
  
      check      Verify Deezer login.
      download   Download favorites.    
      

  {check,download}
```

## Acknowledgement

Thanks to kmile hardwork see : https://github.com/kmille/deezer-downloader