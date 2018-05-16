import os
import shutil

for i in range (1, 14):
	shutil.copyfile("isaw-publications.css", "isaw-papers-"+str(i)+"/isaw-publications.css")

