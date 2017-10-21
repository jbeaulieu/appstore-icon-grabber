# appstore-icon-grabber
A Python script to download icons from the Apple App Store

Requirements
------------
The following modules need to be installed via ``pip`` before the script can run:

- Pillow
- python-slugify (installing slugify via pip will result in a unicode error on some versions of Windows)
- requests

Usage
-----

After locating the ID of the app you wish to download the icon for, simply add it as an arguement the script:
For example,
```bash
$ python appicon.py 284815942
```
Will download the icon for the Google app on the iTunes app store.

### Downloading multiple icons
Multiple ID arguments in succession are supported, for example
```bash
$ python appicon.py 535886823 422689480 544007664
```
will download the icons for Google Chrome, Gmail, and Youtube.

Disclaimer
----------

__In a nutshell:__ it's not my fault if Apple or the app developer call for your head on a platter because you failed to correctly attribute an icon to its proper owner!

I do not own the icons downloaded using this tool, and chances are neither do you, the user. This tool merely provides easier access to material that is already openly available on the web. It is your job to see to it that anything gained through use of this tool is properly attributed to its original source. I take no responsibility for the use or misuse of any graphics or other information gathered through this script.
