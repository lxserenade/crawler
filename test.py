#!/use/bin/env python
#-*- coding:utf8 -*-

import urllib
import re
import json
import time,datetime
import numpy as np
from my_leastsq import *


data=[1064715, 1040697, 738304, 456399, 400885, 394643, 392089, 388057, 366430, 321151, 305288, 264096, 261089, 242011, 241813, 235756, 234706, 230304, 217794, 216982, 212611, 208852, 198573, 196750, 195984, 194630, 194466, 193478, 192490, 184660, 179922, 172080, 171723, 169728, 159053, 159014, 159012, 155851, 153971, 150996, 145132, 145015, 142509, 141499, 137893, 136652, 133072, 133068, 126571, 126410, 124805, 124803, 124559, 121409, 120947, 119975, 116739, 116354, 114356, 114354, 113875, 113870, 110828, 109651, 109315, 107678, 105844, 104318, 95724, 92988, 92986, 92381, 92159]
leastsq_plot(np.array([float(i)/100000 for i in data]),"test")