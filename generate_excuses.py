#!#! /usr/bin/env python3
#-*- coding: utf-8 -*-
##
# Generate excuses from a predetermined list of excuses for        
# finance departments everywhere on why they should not
# pay their vendors.
#
##
import os, random, time, shutil

class generateExcuses():
	def __init__(self):
		self.file_name = "excuses.txt"
		self.cwd = os.getcwd()
		self.prettylines = range(100)
		self.columns = shutil.get_terminal_size().columns

	def print_header(self):
		print("Welcome to the Random Excuse Generator".center(self.columns))
		self.print_pretty_lines()
		print("The date today is {}".format(time.strftime("%d/%m/%Y")).center(self.columns))
		print("As usual, you are a member of your finance team in charge of the payroll".center(self.columns))
		print("Based on your experience, you have a number of excuses on hand to delay the payment of salary.".center(self.columns))
		print("Now, you are going to generate an excuse to delay some poor fucker's salary...".center(self.columns))
		self.print_pretty_lines()
		print("Your excuse for the month is...\n".center(self.columns))
		self.open_excuses()

	def open_excuses(self):
		with open (self.file_name,"r") as f:
			list_of_excuses = f.readlines()
			random_no = self.get_random_number(len(list_of_excuses))
			selected_excuse = [(str)(random_no-1),": ",list_of_excuses[random_no]]
			print("".join(selected_excuse).center(self.columns))

	def get_random_number(self,length):
		random_index = random.randint(0,length-1)
		return random_index

	def print_pretty_lines(self):
		divider = []
		[divider.append("=") for x in self.prettylines]
		print("".join(divider).center(self.columns))

if __name__ == "__main__":
	generateExcuses().print_header()
