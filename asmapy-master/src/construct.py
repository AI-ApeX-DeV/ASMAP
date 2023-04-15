import urllib.request
import os
import os.path
from datetime import datetime


FILES = {
    "routeviews.bz2": "http://archive.routeviews.org/bgpdata/%Y.%m/RIBS/rib.%Y%m%d.0000.bz2",
    "ripe-00.gz": "https://data.ris.ripe.net/rrc00/%Y.%m/bview.%Y%m%d.0000.gz",
}

def download_dump(src, dst, callback, file_size):
    downloaded_mib = 0
    block_size = max(4096, file_size // 1000)
    download_size_mib = file_size / 1024 / 1024

    while True:
        buf = src.read(block_size)
        if not buf:
            break
        dst.write(buf)
        downloaded_mib += len(buf) / 1024 / 1024
        callback(downloaded_mib, download_size_mib)

def display_progress(downloaded_mib, download_size_mib):
    print('\r    {:.2f} / {:.2f} MiB --- {:.1f}%'.format(
        downloaded_mib, download_size_mib,
        (downloaded_mib / download_size_mib) * 100), end='')

def construct(date):
    DIRNAME = "data-%s/" % date
    if not os.path.exists(DIRNAME):
        os.mkdir(DIRNAME)
    for filename, url in FILES.items():
        fullpath = DIRNAME + filename
        datetime_obj = datetime.strptime(date, '%Y%m%d')
        eurl = datetime_obj.strftime(url)
        if not os.path.exists(fullpath):
            print("Downloading %s from %s" % (filename, eurl))
            if os.path.exists(fullpath + ".part"):
                os.remove(fullpath + ".part")
            try:
                with urllib.request.urlopen(eurl) as response, open(fullpath + ".part", "wb") as out_file:
                    file_size = int(response.getheader('content-length'))
                    download_dump(response, out_file, display_progress, file_size);
                    print()
                os.rename(fullpath + ".part", fullpath)
            except OSError as err:
                print("Failed to download %s: %s" % (filename, err))
