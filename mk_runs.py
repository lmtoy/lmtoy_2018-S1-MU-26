#! /usr/bin/env python3

# Using /home/teuben/LMT/lmtoy/data_lmt/unity/data_lmt.log
# 2018-S1-MU-26 - Science
#   script generated by source_obsnum.sh
import os
import sys

from lmtoy import runs

project="2018-S1-MU-26"

# Dictionary of sources, each with a list of obsnum's in this project
# negative obsnums are ignored in the combinations. See also comments.txt
# for obsnum specific comments and parameters!
on = {}

on["Az_G12_26"] = \
 [ 76585, 76586, 76587, 76589, 76590, 76591, 76593, 76594, 76595, 76600, 76601, 76602, 76604, 76605, 76606, 76610, 76611, 76612, 76735, 76736, 76737, 76739, 76740, 76741, 76743, 76744, 76745, 77017, 77018, 77019, 77021, 77022, 77023, 77025, 77026, 77027, 77143, 77144, 77145, 77147, 77148, 77149, 77151, 77152, 77153,]

on["Az_G12_79"] = \
 [ 76717, 76718, 76719, 76721, 76722, 76723, 76725, 76726, 76727, 76730, 76731, 76732, 76834, 76835, 76836, 76838, 76839, 76840, 76842, 76843, 76844, 76847, 76848, 76849, 76851, 76852, 76853, 76855, 76856, 76857, 76859, 76860, 76861, 77122, 77123, 77124, 77126, 77127, 77128, 77130, 77131, 77132, 77134, 77135, 77136, 77138, 77139, 77140,]

on["Az_NGP_28"] = \
 [ 76774, 76775, 76776, 76778, 76779, 76780, 76782, 76883, 76884, 76885, 76887, 76888, 76889, 76891, 76892, 76893, 77031, 77032, 77033, 77035, 77036, 77037, 77039, 77040, 77041, 77044, 77045, 77046, 77048, 77049, 77050, 77156, 77157, 77158, 77160, 77161, 77162, 77164, 77165, 77166, 77169, 77170, 77171,]

# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)
pars1 = {}

pars1["Az_G12_26"] = ""
pars1["Az_G12_79"] = ""
pars1["Az_NGP_28"] = ""

# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}

pars2["Az_G12_26"] = ""
pars2["Az_G12_79"] = ""
pars2["Az_NGP_28"] = ""

# parameters for the (optional) third pass of the pipeline (usually for bank=1)
pars3 = {}

pars3["Az_G12_26"] = ""
pars3["Az_G12_79"] = ""
pars3["Az_NGP_28"] = ""

# Found 3 source(s) for 2018-S1-MU-26

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
