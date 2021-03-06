![alt text](https://github.com/jbeaulieu/appstore-icon-grabber/blob/master/banner.jpg "Project BASIL: App Store Icon Grabber")

# Project BASIL
A Python script to download icons from the Apple App Store

Prerequisites
------------
The following modules must be installed before the script can run:

- [Pillow](https://github.com/python-pillow/Pillow)
- [python-slugify](https://github.com/un33k/python-slugify)
- [requests](http://docs.python-requests.org/en/master/)

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

You may change this behavior to specify one or more resolutions of your choice. Currently, this feature requires editing a hardcoded value in the code.

To add your custom resolutions, simply edit the line
```python
size_list = [512]
```
to include your comma-separated resolutions.

__Note__ that while this script will output icons at any resolution you'd like via the above method, sizes above 512x512px will be upscaled, due to the json issue mentioned at the beginning of this section.

Disclaimer
----------

I do not own the icons downloaded using this tool, and chances are neither do you. This tool merely provides easier access to material that is already openly available on the web. It is your job to ensure that anything gained through use of this tool is properly attributed to its original source. I take no responsibility for the misuse of any graphics or other information gathered through this script.
