#!/usr/bin/python3
#
#CreateSettings.py
#
#Copyright (C) 2011-2012 Nicholas Polach <npolach@hotmail.com>
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


class CreateSettings:

	mintemp = 0
	maxtemp = 0

	def __init__(self):

		# Begins creation of settings file
		CreateSettings.MinTemp()	
	
	def MinTemp():

		SettingsFile = open('settings.txt', 'w')

		# Automatically sets 0 as lowest temperature and lets user choose 
		# max temperature and fan speed for first temperature range
		CreateSettings.mintemp = int(input('Maximum temperature for first temperature range: '))
		minspeed = int(input('Fan speed for temperature range "0*C <= *C <= {0}*C": '.format(CreateSettings.mintemp)))
		save = '0' + ' ' + str(CreateSettings.mintemp) + ' ' + str(minspeed)
		SettingsFile.write(save)
		SettingsFile.write('\n')
		print('~~~~~~')
		
		CreateSettings.AvgTemp(SettingsFile) 
		
	def AvgTemp(SettingsFile): 

		loop = 'yes' 
		while loop == 'yes':

			# Lets users create more temperature ranges and set fan speeds 
			# until they specify "no"
			CreateSettings.mintemp = CreateSettings.mintemp+1
			CreateSettings.maxtemp = int(input('Maximum temperature for next temperature range: '))
			speed = int(input('Fan speed for temperature range "{0}*C <= *C <= {1}*C": '.format(CreateSettings.mintemp, CreateSettings.maxtemp)))
			save = str(CreateSettings.mintemp) + ' ' + str(CreateSettings.maxtemp) + ' ' + str(speed)
			SettingsFile.write(save)
			SettingsFile.write('\n')
			CreateSettings.mintemp = CreateSettings.maxtemp
			loop = str(input('Add another temperature range? (yes/no): '))
			while loop != 'yes' and loop != 'no':
				loop = str(input('Add another temperature range? (yes/no): '))
			print('~~~~~')

		CreateSettings.MaxTemp(SettingsFile) 
	
	def MaxTemp(SettingsFile):

		# Takes last max temperature and automatically creates last temperature range 
		# and sets fan speed to 100%
		CreateSettings.maxtemp = CreateSettings.maxtemp+1
		save = str(CreateSettings.maxtemp) + ' ' + '1000' + ' ' + '100'
		SettingsFile.write(save)
		SettingsFile.close()
		print('Final temperature range is "{0}*C+" at 100% fan speed.'.format(CreateSettings.maxtemp))

CreateSettings()
