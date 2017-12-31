from numpy import *
from datetime import datetime, timedelta
import myfunc.IO.MERGIR as MERGIR


DTime = datetime(2014,4,1,15,30)
ir = MERGIR.MERGIR()
dat1 = ir.load_1hr(DTime)
dat2 = ir.load_30min(DTime)
print dat1
print dat1.shape




