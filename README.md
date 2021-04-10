# Deezer Downloader

Download music directly from deezer.

You will need a file `settings.ini` file.

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
$ make install
```