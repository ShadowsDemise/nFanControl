#!/usr/bin/python3
#

#Copyright 2011-2012 Nicholas Polach
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os, subprocess, time

class FanControl:

	def __init__(self):

		try:
			SettingsFile = open('settings.txt', 'r')
		except IOError:
			import CreateSettings
		else:
			FanControl.EnableFanSettings(SettingsFile)
			

	def EnableFanSettings(SettingsFile):

		os.system('nvidia-settings -a [gpu:0]/GPUFanControlState=1')
		os.system('nvidia-settings -a [gpu:1]/GPUFanControlState=1')
		os.system('nvidia-settings -a [gpu:2]/GPUFanControlState=1')
		os.system('nvidia-settings -a [gpu:3]/GPUFanControlState=1')

		FanControl.ReadFile(SettingsFile)

	def ReadFile(SettingsFile):

		loop = 'yes'

		while loop == 'yes':
			
			try:
				temp0 = int(subprocess.getoutput('nvidia-settings -q "[gpu:0]/GPUCoreTemp" -t'))
			except:
				pass			
			try:
				temp1 = int(subprocess.getoutput('nvidia-settings -q "[gpu:1]/GPUCoreTemp" -t'))
			except:
				pass
			try:
				temp2 = int(subprocess.getoutput('nvidia-settings -q "[gpu:2]/GPUCoreTemp" -t'))
			except: 
				pass			
			try:
				temp3 = int(subprocess.getoutput('nvidia-settings -q "[gpu:3]/GPUCoreTemp" -t'))
			except: 
				pass
			TempFile = open('settings.txt', 'r') 
			
			
			for line in TempFile.readlines():
				line = tuple(line.split())
				if int(line[0]) <= temp0 <= int(line[1]):			
					os.system('nvidia-settings -a [fan:0]/GPUCurrentFanSpeed={0}'.format(int(line[2])))	

			try:
				for line in TempFile.readlines():
					line = tuple(line.split())
					if int(line[0]) <= temp1 <= int(line[1]):			
						os.system('nvidia-settings -a [fan:1]/GPUCurrentFanSpeed={0}'.format(int(line[2])))
			except:
				pass	

			try:
				for line in TempFile.readlines():
					line = tuple(line.split())
					if int(line[0]) <= temp2 <= int(line[1]):			
						os.system('nvidia-settings -a [fan:2]/GPUCurrentFanSpeed={0}'.format(int(line[2])))
			except:
				pass	

			try:
				for line in TempFile.readlines():
					line = tuple(line.split())
					if int(line[0]) <= temp3 <= int(line[1]):			
						os.system('nvidia-settings -a [fan:3]/GPUCurrentFanSpeed={0}'.format(int(line[2])))
			except:
				pass				
			
			TempFile.close() 

			time.sleep(30)			



FanControl()



