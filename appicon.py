import io
import requests
from PIL import Image
from slugify import slugify


def download_icon(icon_url, title, mask):

    print("Downloading: " + title)

    # Download icon, apply mask.
    icon_data = requests.get(icon_url)
    icon = Image.open(io.BytesIO(icon_data.content))
    icon.putalpha(mask)

    # Specify the desired size of icons here. You may list multiple values
    # Note that this app pulls 512x512 icons from the app store, so any
    #  larger-resolution output will be upscaled
    size_list = [512]

    # Compute and save thumbnails.
    for size in size_list:
        icon_resized = icon.resize((size, size), Image.ANTIALIAS)
        icon_resized.save("icon_{0}_{1}x{1}.png".format(title, size))


def download_app_metadata(app_id, mask):

    url = "http://itunes.apple.com/us/lookup?id={}".format(app_id)
    r = requests.get(url)
    if r.status_code != 200:
        print('Error downloading {} {}'.format(url, r.status_code))
        return

    results = r.json()

    meta = results["results"][0]
    icon_url = meta["artworkUrl512"]
    title = slugify(meta["trackCensoredName"])

    download_icon(icon_url, title, mask)


def download_icon_mask():

    # Download the mask from Github, this way we don't
    # have to provide mask.png and the script is self contained.
    mask_url = ""
    mask_data = requests.get(mask_url)
    mask = Image.open(io.BytesIO(mask_data.content))
    mask = mask.convert('L')
    return mask


def download_apps():

    app_ids = [
        "284815942"
    ]

    #mask = download_icon_mask()
    mask_import = Image.open('mask512.png')
    mask = mask_import.convert('L');
    [download_app_metadata(app_id, mask) for app_id in app_ids]


if __name__ == '__main__':

    download_apps()
    print("Finished")
