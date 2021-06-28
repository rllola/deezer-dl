#!/usr/bin/env python3

import sys
import os
import argparse

if not sys.platform.startswith('linux'):
    print('Only linux is supported.')
    sys.exit(1)

def main():
    description = """
    check      Verify Deezer login.
    download   Download favorites.    
    """

    parser = argparse.ArgumentParser(prog='deezer-dl',formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = parser.add_subparsers(title='command',description=description, dest='command')
    check = sp.add_parser('check')
    download = sp.add_parser('download')

    args = parser.parse_args()

    if args.command:
        from deezer import config, test_deezer_login, get_song_infos_from_deezer_website, download_song, get_deezer_favorites, TYPE_TRACK
        from utils import format_song_filename

        if args.command == 'check':
            test_deezer_login()
        elif args.command == 'download':
            favorite_playlist = get_deezer_favorites(config['deezer']['user_id'])
            print(config['deezer']['music_dir'])
            
            os.makedirs(config['deezer']['music_dir'], exist_ok=True)

            for song_id in favorite_playlist:
                try:
                    song_info = get_song_infos_from_deezer_website(TYPE_TRACK, song_id)
                    song_filename = format_song_filename(song_info['ART_NAME'],song_info['SNG_TITLE'])
                    song_path = os.path.join(config['deezer']['music_dir'], song_filename)
                    if os.path.exists(song_path):
                        continue
                    download_song(song_info, song_path)            
                except Exception as e:
                    print(e)
                    pass

if __name__ == "__main__":
    main()