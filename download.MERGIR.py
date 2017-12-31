from datetime import datetime, timedelta
import myfunc.util as util
import calendar
import os, sys, socket
import subprocess

#https://disc2.gesdisc.eosdis.nasa.gov/data/MERGED_IR/GPM_MERGIR.1/2014/091/merg_2014040100_4km-pixel.nc4

iYM  = [2008,2]
eYM  = [2008,2]
lYM  = util.ret_lYM(iYM, eYM)

hostname = "https://disc2.gesdisc.eosdis.nasa.gov"
cookiesPath ="/home/utsumi/bin/MERGIR/.urs_cookies"

myhost= socket.gethostname()
if myhost == "mizu":
  obaseDir = "/home/utsumi/mnt/wellshare/data"
elif myhost == "well":
  obaseDir = "/media/disk2/share/data"




for YM in lYM:
    Year,Mon = YM
    iDay = 1
    eDay = calendar.monthrange(Year,Mon)[1]
    iDTime   = datetime(Year,Mon,iDay,0)
    eDTime   = datetime(Year,Mon,eDay,23)
    dDTime   = timedelta(days=1)
    lDTime   = util.ret_lDTime(iDTime, eDTime, dDTime)

    DTime0   = datetime(Year,1,1,0)

    for DTime in lDTime:
        Day      = DTime.day
        DOY      = (DTime - DTime0).days +1

        rootDir  = hostname + "/data/MERGED_IR/GPM_MERGIR.1"
        srcDir   = rootDir + "/%04d/%03d"%(Year,DOY)
        for Hour in range(0,24):

            ##-- single ----
            #if not (Day==2)&(Hour==15): continue  # test
            ##--------------

            fileName = "merg_%04d%02d%02d%02d_4km-pixel.nc4"%(Year,Mon,Day,Hour)
            srcPath  = srcDir + "/" + fileName

            oDir     = obaseDir + "/MERGIR/%04d/%02d%02d"%(Year,Mon,Day)
            outPath  = oDir + "/%s"%(fileName)
            util.mk_dir(oDir)


            scmd = "wget --load-cookies %s --save-cookies %s --auth-no-challenge=on --keep-session-cookies --content-disposition %s -O %s"%(cookiesPath, cookiesPath, srcPath, outPath)

            print scmd

            subprocess.call(scmd, shell=True)

