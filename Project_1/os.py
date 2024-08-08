import os
import activity1
import activity2
if not os.path.exists("Project_1"):
    os.mkdir("Project_1")
os.chdir("Project_1")
a1_free_time()
a1_busy_time()
a2_free_time()
a2_busy_time()
