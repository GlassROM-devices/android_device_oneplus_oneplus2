import common
import struct

def FullOTA_InstallEnd(info):
    print "no bootloader.img in target_files; skipping install"
    print "no radio.img in target_files; skipping install"

def IncrementalOTA_InstallEnd(info):
    source_bootloader_img = None
    print "no bootloader.img in target target_files; skipping install"
