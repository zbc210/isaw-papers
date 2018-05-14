from  bs4  import BeautifulSoup
import re
import os
import shutil

for i in range (1, 14):
	shutil.copyfile("isaw-publications.css", "isaw-papers-"+str(i)+"/isaw-publications.css")

	#with open('isaw-papers-'+str(i)+'/isaw-papers-'+str(i)+'.xhtml') as paper:
		#soup = BeautifulSoup(paper)


	#css = soup.find("link", {"rel" : re.compile("stylesheet*")})
	#css['href']= 'isaw-publications.css'

	#with open("isaw-papers-"+str(i)+'/isaw-papers-'+str(i)+'.xhtml', 'w') as paper:
		#paper.write(str(soup)) 
