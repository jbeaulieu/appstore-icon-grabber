# appstore-icon-grabber
A Python script to download icons from the Apple App Store

Requirements
------------
The following modules need to be installed via ``pip`` before the script can run:

- Pillow
- python-slugify (installing slugify via pip will result in a Unicode error on some versions of Windows)
- requests

Usage
-----

After locating the ID of the app you wish to download the icon for, simply add it as an argument the script.
For example, the Google app on the iTunes app store can be found at <https://itunes.apple.com/us/app/google/id284815942>.

Executing
```bash
$ python appicon.py 284815942
```
Will download the icon for the Google app on the iTunes app store.

### Downloading multiple icons
Multiple ID arguments in succession are supported, for example
```bash
$ python appicon.py 535886823 422689480 544007664
```
will download the icons for Google Chrome, Gmail, and YouTube.

### Image Resolution
By default, the script will process icons at a resolution of 512x512. This appears to be the highest resolution that is guaranteed to be linked to in the json file the script obtains from the app store for each icon. If there is a reliable way to obtain higher native resolutions from the app store, I will strive to include it here so that resolutions above 512px square will not require upscaling.

You may change this behavior to specify one or more resolutions of your choice. Currently, this feature requires editing a hardcoded value in the code, but it will be added as an optional command-line argument soon.

To add your custom resolutions, simply edit the line
```python
size_list = [512]
```
to include your comma-separated resolutions.

__Note__ that while this script will output icons at any resolution you'd like via the above method, sizes above 512x512px will be upscaled, due to the json issue mentioned at the beginning of this section.

Disclaimer
----------

__In a nutshell:__ it's not my fault if Apple or the app developer call for your head on a platter because you failed to correctly attribute an icon to its proper owner!

I do not own the icons downloaded using this tool, and chances are neither do you, the user. This tool merely provides easier access to material that is already openly available on the web. It is your job to see to it that anything gained through use of this tool is properly attributed to its original source. I take no responsibility for the use or misuse of any graphics or other information gathered through this script.
