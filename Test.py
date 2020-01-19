# -*- coding: utf-8 -*-
#!/usr/bin/python

#**
#* Created by jfwang on 2017-02-28.
#* pickupFile - 提取一类型文件
#**

import sys,getopt
import os
from os.path import join, getsize  
import platform

class pickupFile(object):
	def __init__(self):
		super(pickupFile, self).__init__()
		
		# 源路径
		self.fromFilePath = ""

		# 输出路径
		self.toFilePath = ""


	def setFromFilePath(self,path):
		self.fromFilePath = path

	def setToFilePath(self,path):
		self.toFilePath = path

	def initDir(self):
		sysstr = platform.system()
		if(sysstr =="Windows"):
			cmd = "rd /s/q %s" % self.toFilePath
			os.system(cmd)
		else:
			cmd = "rm -r -f %s" % self.toFilePath
			os.system(cmd)

		cmd = "mkdir %s" % self.toFilePath
		os.system(cmd)


	def run(self,fileType):
		self.initDir()
		for root, dirs, files in os.walk(self.fromFilePath):
			for name in files:
				fileName, fileSuffix = os.path.splitext(name)
				if fileSuffix == fileType:
					fromFileName = self.fromFilePath + root[len(self.fromFilePath):] + '/' + name

					toFullPath = self.toFilePath + root[len(self.fromFilePath):]
					toFullName = toFullPath + '/' + name

					if os.path.isdir(toFullPath):
						pass
					else:
						os.makedirs(toFullPath)

					cmd = "cp %s %s" % (fromFileName,toFullName)
					print cmd
					
					sysstr = platform.system()
  					if(sysstr =="Windows"):
  						cmd = "xcopy %s %s" % (fromFileName,toFullName)
					os.popen(cmd)

def usage():
	print '-h, --help:		Please see help information.'
	print '-i, --input:		Input resource path.'
	print '-o, --output:	Output resource path.'
	print '-t, --type:		pickup file type.'


def main(argv):
	pickup = pickupFile()

	try:
		opts, args = getopt.getopt(argv[1:], 'h:i:o:t:', ['help=', 'input=', 'output=','type='])
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit(1)

	print 'Incoming parameters: %s' % opts

	#是否运行
	iscanrun = 1
	filetype = ".png" 
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
			sys.exit(0)
		elif opt in ('-i', '--input'):
			pickup.setFromFilePath(arg)
			print 'setFromFilePath: %s' % arg
		elif opt in ('-o', '--output'):
			pickup.setToFilePath(arg)
			print 'setToFilePath: %s' % arg
		elif opt in ('-t', '--type'):
			filetype = arg
			print 'filetype: %s' % arg
		else:
			iscanrun = 0
			print '-h Please see help information.'

	if iscanrun==1:
		pickup.run(filetype)

if __name__ == '__main__':
	main(sys.argv)

