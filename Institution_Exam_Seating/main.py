# Developed by Arijit Bhowmick [sys41x4]
# https://github.com/Arijit-Bhowmick/Give-My-Seat
# https://github.com/sys41x4/Give-My-Seat

# Writing to an excel 
# sheet using Python
#import xlwt
#import xlrd
#from xlutils.copy import copy
#import xlsxwriter
import os
import openpyxl
#import pandas as pd
from pandas import read_excel as pd_read_excel
#import numpy as np
from numpy import array as np_array
import json
import random

class program:
	def print_indv_branch_table(table):
		global row, col
		# print individual branch location in matrix
		

		for branch in list(branch_frequency.keys()):
			table_matrix=[]
			for i in range(row):table_matrix+=[['']*col]
			for i in range(len(table)):
				for j in range(len(table[i])):
					if table[i][j]==branch:
						table_matrix[i][j]=table[i][j]

			program.print_table(table_matrix, f'{branch} Seating:')



	def print_table(table, matrix_header='MATRIX:'):
					
		###
	    longest_cols = [
	    	(max([len(str(row[i])) for row in table]) + 1)
	    	for i in range(len(table[0]))
	    ]

	    row_format = "".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])

	    print(f'[{matrix_header}]\n')
	    for row_num in range(len(table)):
	    	print(row_format.format(*table[row_num]))
	    print()

	def get_rand_branch(table_matrix, prev_value, matrix_row=0, matrix_col=0, upper_value=0):
		global branch_frequency
		global exception_handler

		# Generate modified unique branch values
		# if branch value in branch_frequency==0
		# then it will be excluded in exc_branch list
		exc_branch=[]
		for i in range(len(branch_frequency.values())):
			if list(branch_frequency.values())[i]>0:
				# print(branch_frequency)
				exc_branch+=[list(branch_frequency.keys())[i]]

		
		if exc_branch==[]:
			#print('brooo')
			return '\n'
		###
		else:
			if upper_value!=0:
				try:

					if matrix_row>0 and matrix_col==0:
						if len(exc_branch)==1 and exc_branch[0]==upper_value:
							#return upper_value
							return ''
						exc_branch.remove(upper_value)
					# Except First Entry
					# when .remove() will not give Value Error
					elif matrix_row>0 and matrix_col>0:
						# print("entered")
						# print(f"prev_value=> {prev_value} | upper_value=> {upper_value}")
						if len(exc_branch)==1 and exc_branch[0]==upper_value and exc_branch[0]==prev_value:
							#return upper_value
							#print('hola')
							return ''

						else:
							

							if len(exc_branch)==1 and exc_branch[0]==upper_value:
								#return upper_value
								return ''
							else:
								if upper_value!='':
									exc_branch.remove(upper_value)

							if len(exc_branch)==1 and exc_branch[0]==prev_value:
								#return prev_value
								return ''
							else:
								if prev_value!='':
									exc_branch.remove(prev_value)
				except ValueError:
					# print()
					exception_handler=1

			elif upper_value==0:
				try:
					# Except First Entry
					# when .remove() will not give Value Error
					if len(exc_branch)==1 and exc_branch[0]==prev_value:
							#return prev_value
							return ''
					else:
						if prev_value!='':
							exc_branch.remove(prev_value)
					#random_branch = random.choice(exc_branch)
				except ValueError:
					#print()
					exception_handler=1

			random_branch = random.choice(exc_branch)
			# print("exec_branch not error")

			return random_branch

	def remove_confirmed_rollno(seating_json_data):

		global json_data

		# Roll Number List
		rollnum_list = list(json_data['std_rollnum'].values())
		rollnum_index_list = list(json_data['std_rollnum'].keys())

		for roll in list(seating_json_data.keys()):
			for column_header in list(json_data.keys()):
				del json_data[column_header][rollnum_index_list[rollnum_list.index(roll)]]

		print(json_data)

	def remove_filledup_room():
		global current_room
		global room_data

		room_index_list = list(room_data['room_name'].keys())
		room_list = list(room_data['room_name'].values())

		for column_header in list(room_data.keys()):
			del room_data[column_header][room_index_list[room_list.index(current_room)]]


	def json_data_dump(dump_json_data, excel_data_type):

		if excel_data_type=='student_data':
			with open(f"{excel_data_type}.json", 'w', encoding = 'utf-8') as json_file:json.dump(dump_json_data, json_file)
		elif excel_data_type=='room_data':
			with open(f"{excel_data_type}.json", 'w', encoding = 'utf-8') as json_file:json.dump(dump_json_data, json_file)
		elif excel_data_type=='seating_data':
			with open(f"{excel_data_type}.json", 'w', encoding = 'utf-8') as json_file:json.dump(dump_json_data, json_file)


	def arrange_seating(table, json_data, value_to_show):
		global row, col
		table_matrix=[]
		for i in range(row):table_matrix+=[['']*col]


		branch_list = list(json_data['std_branch'].values())
		# print(branch_list)
		#if value_to_show=='std_name':
		std_name_list = list(json_data['std_name'].values())
		#	seating_type = 'Student Name'
		#if value_to_show=='std_rollnum':
		rollnum_list = list(json_data['std_rollnum'].values())
		#	seating_type='Student Roll Number'
		#elif value_to_show=='std_aadhar':
		aadhar_list = list(json_data['std_aadhar'].values())
		#	seating_type='Student Aadhar'
		
		branch_and_replacer_dict = {}
		for i in range(len(branch_list)):
			branch_and_replacer_dict.__setitem__(rollnum_list[i], branch_list[i])

		global seating_json_data

		seating_json_data={}
		#filled_seat=0
		# for branch in branch_list:
		# 	if filled_seat!=
		for row_num in range(len(table)):
			
			for col_num in range(len(table[row_num])):
				if table[row_num][col_num]=='':
					continue
				else:
					#print(f"table element => {table_matrix} \n dict Value => {branch_and_replacer_dict.values()}")
					#print(table_matrix)
					branch_index = branch_list.index(table[row_num][col_num])

					branch_name = branch_list[branch_index] # branch Name
					roll_num = rollnum_list[branch_index] # Usually Enrollment Number
					aadhar_num = aadhar_list[branch_index] # Aadhar Number
					student_name = std_name_list[branch_index] # Student Name

					table_matrix[row_num][col_num]=roll_num

					# Creating JSON Data for the seating
					# seating_json_data+='{\"std_name\": \"'+student_name+'\", \"branch_name\": \"'+branch_name+'\", \"roll_num\": \"'+roll_num+'\", \"aadhar_num\": \"'+aadhar_num+'\", \"block_num\": \"'+current_block+'\", \"room_num\": \"'+current_room+'\", \"row\": '+str(row_num)+', \"column\": '+str(col_num)+' }, '
					# seating_json_data+='\"'+roll_num+'\": {\"std_name\": \"'+student_name+'\", \"branch_name\": \"'+branch_name+'\", \"roll_num\": \"'+roll_num+'\", \"aadhar_num\": \"'+aadhar_num+'\", \"block_num\": \"'+current_block+'\", \"room_num\": \"'+current_room+'\", \"row\": '+str(row_num)+', \"column\": '+str(col_num)+' }, '
					# seating_json_data+='"'+roll_num+'": {"std_name": "'+student_name+'", "branch_name": "'+branch_name+'", "roll_num": "'+roll_num+'", "aadhar_num": "'+aadhar_num+'", "block_num": "'+current_block+'", "room_num": "'+current_room+'", "row": '+str(row_num)+', "column": '+str(col_num)+' }, '
					seating_json_data.update({roll_num: {"std_name": student_name,"branch_name": branch_name,"roll_num": roll_num,"aadhar_num": aadhar_num,"block_num": current_block,"room_num": current_room,"row": row_num,"column": col_num }})

					#branch_and_replacer_dict.__setitem__(replacer_value, '\n')
					branch_list[branch_index]='\n'

		all_seating_data.update(seating_json_data)
		print()

		# When 1 Room has been successfully booked
		# the students (Based on their Enrollment Number)
		# will be removed from the unassigned list
		# as their seating is confirmed
		program.remove_confirmed_rollno(seating_json_data)

		# Remove the Filleup Room name and its data Row from the json data
		program.remove_filledup_room()

		# Generated Seating data will be dumped in seating_data.json
		program.json_data_dump(all_seating_data, 'seating_data')
		# Generated student data will be dumped in the student_data.json
		program.json_data_dump(json_data, 'student_data')
		# Generated room data will be dumped in the room_data.json
		program.json_data_dump(room_data, 'room_data')


		# On completing 1 room next room would be used
		#
		# global current_room_count
		# current_room_count+=1

		program.print_table(table_matrix, f'Seating Based on {current_block}-{current_room}:')

		# Assign Seating for Remainig Students | Enrollment_No

		program.load_json("from_pre_json", default_json_file_paths)
		# print(total_student_count)
		# total_student_count
		program.generate_seating(json_data, room_data)




	def generate_matrix_samples(json_data, total_branches):

		

		# branch_frequency is the frequency of
		# branch in the excel sheet

		global branch_frequency
		branch_frequency={}
		for i in (list(set(total_branches))):
			branch_frequency.__setitem__(i, total_branches.count(i))


		## Generate table as matrix
		table_matrix = []
		for i in range(row):table_matrix+=[['']*col]

		## without SheetName
		# json_data=json.loads(pd.read_excel(file_path).to_json())
		## With sheetName

		

		#branch = list(set(total_branches))

		
		#print(branch_frequency)

		exc_branch=list(branch_frequency.keys())
		#print(total_branches)
		## if total unique branch are more than column then
		row_finish,matrix_completed=0,0
		matrix_row,matrix_col=0,0
		prev_value=''
		finish=0
		while matrix_completed!=row*col and finish==0:

			if matrix_row==0:
				while row_finish!=col:
					

					table_matrix[matrix_row][matrix_col]=program.get_rand_branch(table_matrix, prev_value)
					prev_value=table_matrix[matrix_row][matrix_col]
					# On adding 1 entry of branch name 
					# in table_matrix, 1 entry/value
					# will be deleted from the branch_frequency dict 
					branch_frequency[prev_value]-=1
					## print(row_finish, col)
					row_finish+=1
					matrix_completed+=1
					matrix_col+=1
					## print(table_matrix)
				matrix_col=0
				matrix_row+=1
				row_finish=0

			elif matrix_row!=0:
				while row_finish!=col:
					ran_branch = program.get_rand_branch(table_matrix, prev_value, matrix_row, matrix_col, table_matrix[matrix_row-1][matrix_col])
					## print(ran_branch.encode())
					if ran_branch=='\n':
						finish=1
						break

					table_matrix[matrix_row][matrix_col]=ran_branch
					
					prev_value=ran_branch

					if prev_value!='':
						branch_frequency[prev_value]-=1

					row_finish+=1
					matrix_completed+=1
					matrix_col+=1
					## print(table_matrix)
				matrix_col=0
				matrix_row+=1
				row_finish=0
		
		#print(table_matrix)
		# print individual branch location in matrix

		return table_matrix


	def generate_matrix(json_data, sample_count=1):
		# Creating 10 sample matrix
		# for maximum throughput

		#np.array(matrix).flatten()
		total_branches = list(json_data['std_branch'].values())

		if len(total_branches)>row*col:
			print(f"Mimimum {len(total_branches)-row*col} students will have to be allocated to another room")

		matrix_samples=[]
		empty_seat_count=[]

		for sample in range(sample_count):
			matrix_samples+=[program.generate_matrix_samples(json_data, total_branches)]


		for sample in matrix_samples:
			empty_seat_count+=[list(np_array(sample).ravel()).count('')]

		max_seating_matrix = matrix_samples[empty_seat_count.index(min(empty_seat_count))]

		program.print_indv_branch_table(max_seating_matrix)

		# Print the formed matrix
		program.print_table(max_seating_matrix, 'Overall Branch Seating:')
		#print(branch_frequency)
		# Print the roll numbers in their provided seating
		program.arrange_seating(max_seating_matrix, json_data, 'std_rollnum')

		# # Print the roll numbers in their provided seating
		# program.arrange_seating(max_seating_matrix, json_data, 'std_aadhar')

	def load_json_from_file(json_data_to_use):
		# {"student_data_path":"", "room_data_path":"", "seating_data_path":""}
		global json_data
		global room_data
		global all_seating_data
		## Read Student Data from JSON File # Variable Name json_data
		# with open(json_data_to_use["student_data_path"], 'r', encoding = 'utf-8') as f:json_data=json.load(f.read())
		json_data=json.load(open(json_data_to_use["student_data_path"]))
		
		## Read Room Data from JSON File # Variable name room_data
		# with open(json_data_to_use["room_data_path"], 'r', encoding = 'utf-8') as f:room_data=json.load(f.read())
		room_data=json.load(open(json_data_to_use["room_data_path"]))


		## Read Seating Data from JSON File # Variable Name all_seating_data
		# with open(json_data_to_use["seating_data_path"], 'r', encoding = 'utf-8') as f:all_seating_data=json.load(f.read())
		
		all_seating_data=json.load(open(json_data_to_use["seating_data_path"]))

		if all_seating_data=='':
			all_seating_data={}


	def load_json(process_to_use, json_data_to_use):
		# {"workbook_file_path":"", "student_data_sheet_name":"", "room_data_sheet_name":""}
		if process_to_use=="from_workbook":
			# Generate JSON data from WorkBook
			# and dump it into JSON Files

			global json_data
			global room_data
			global all_seating_data
			all_seating_data={}

			json_data=json.loads(pd_read_excel(open(json_data_to_use["workbook_file_path"], 'rb'), sheet_name=json_data_to_use["student_data_sheet_name"]).to_json())
			room_data = json.loads(pd_read_excel(open(json_data_to_use["workbook_file_path"], 'rb'), sheet_name=json_data_to_use["room_data_sheet_name"]).to_json())
			
			program.json_data_dump(json_data, "student_data")
			program.json_data_dump(json_data, "room_data")
			program.json_data_dump(all_seating_data, "seating")

		elif process_to_use=="from_pre_json":
			
			program.load_json_from_file(json_data_to_use)


	# def generate_seating(file_path='', sheet_name='', room_detail_sheet='', sample_count=1):
	def generate_seating(student_json_data, room_json_data):
		#file_path = 'data.xlsx'
		################
		## Class Data ##
		################

		


		# if file_path=='':
		# 	return print("File Path Not Provided")
		# if room_detail_sheet=='':
		# 	return print("Room Detail Sheet-Name Not Provided")


		global json_data
		# print(json_data)
		global room_data
		# print(room_data)

		# Total Student Number
		global total_student_count

		total_student_count = len(json_data['std_rollnum'].values())

		if total_student_count==0:
			print("All Students has been assigned to their calculated seating")
			exit()

		program.gather_room_data(room_data)

		#total_seat = row*col
		
		program.generate_matrix(json_data, sample_count)

	def gather_room_data(room_data):
		# Room and its row & Column setup
		global block
		global room_name
		global current_room_count

		global current_block
		global current_room
		global row, col

		# total_block = list(room_data['block_name'].values())
		# total_room = list(room_data['room_name'].values())
		row_list = list(room_data['row'].values())
		column_list = list(room_data['column'].values())


		#current_room_count=0

		# Current Room data
		current_block = list(room_data['block_name'].values())[0]
		current_room = list(room_data['room_name'].values())[0]
		row = list(room_data['row'].values())[0]
		col = list(room_data['column'].values())[0]

		total_seat_provided = 0
		for i in range(len(row_list)):
			total_seat_provided+=row_list[i]*column_list[i]

		if total_seat_provided<total_student_count:
			print(f"""Total Student Count = {total_student_count}\
				Total Seats Provided = {total_seat_provided}\
				Total Student Number is greater than Total Seating\
				Please add additional rooms with additional seating in your excel sheet""")
			# exit()

			
			

		def write_to_excel(file_path, sheet_name, matrix, room_name=''):
			col_name_lst = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
			## For xls File
			# # load the excel file
			# load_excel_file = xlrd.open_workbook(file_path)
			 
			# # copy the contents of excel file
			# copy_excel_content = copy(load_excel_file)
			 
			# # open the first sheet
			# w_sheet = copy_excel_content.get_sheet(0)
			 
			# # row number = 0 , column number = 1
			# w_sheet.write(0,1,'Modified !')
			 
			# # save the file
			# wb.save('UserBook.xls')

			## For .xlsx file
			workbook = openpyxl.load_workbook(file_path)
 
			# The workbook object is then used to add new
			# worksheet via the add_worksheet() method.
			worksheet = workbook.sheetnames[sheet_name]
			 
			# Use the worksheet object to write
			# data via the write() method.
			worksheet.write('A1', 'Hello..')
			worksheet.write('B1', 'Geeks')
			worksheet.write('C1', 'For')
			worksheet.write('D1', 'Geeks')
			 
			# Finally, close the Excel file
			# via the close() method.
			workbook.save('text2.xlsx')

	def main():
		#global row, col
		global sample_count
		global default_json_file_paths

		# Default File Storage Path
		default_json_file_paths={"student_data_path":"student_data.json", "room_data_path":"room_data.json", "seating_data_path":"seating_data.json"}

		sample_count=10
		#row,col=13,4

		#file_path = 'data.xlsx'
		#sheet_name = 'Sheet3'
		#room_detail_sheet = 'allowed_room'
		workbook_data = {"workbook_file_path":"", "student_data_sheet_name":"", "room_data_sheet_name":""}

		#pre_json_data_available='' # Considered as No when entered (Default: NO)
		pre_json_data_available = input("Do You have already any pre json data created using this script ? Y/N ==> ")
		pre_json_paths={"student_data_path":"", "room_data_path":"", "seating_data_path":""}

		if pre_json_data_available.upper()=='Y':
			process_to_use = 'from_pre_json'
			for path_key in list(pre_json_paths.keys())[:-1]:
				ask_path = input(f"Please Enter File_Path of {path_key[:-5]} => ")
				if os.path.exists(ask_path)==True:
					pre_json_paths.update({path_key:ask_path})
				else:
					return print(f"File Path {ask_path} is incorrect for \"{path_key[:-5]}\"\nExiting Program !!!")

			ask_path = input(f"Please Enter File_Path of seating_data => ")

			if ask_path=='':
				pre_json_paths.update({"seating_data_path":''})
			elif os.path.exists(ask_path)==True:
				pre_json_paths.update({"seating_data_path":ask_path})
			else:
				return print(f"File Path {ask_path} is incorrect for \"seating_data\"\nExiting Program !!!")

			json_data_to_use = pre_json_paths
		else:
			process_to_use = 'from_workbook'
			ask = input(f"Please Enter File_Path of {list(workbook_data.keys())[0][:-5]} => ")
			if os.path.exists(ask)==True:
				workbook_data.update({"workbook_file_path":ask})
			else:
				return print(f"File Path {ask} is incorrect\nExiting Program !!!")

			workbook_sheet_list = openpyxl.load_workbook(ask).sheetnames

			for path_key in list(workbook_data.keys())[1:]:
				ask = input(f"Please Enter {path_key} Sheet Name => ")

				if (ask not in workbook_sheet_list):
					return print(f"Sheet Name {ask} is incorrect\nExiting Program !!!")
				workbook_data.update({path_key:ask})

			json_data_to_use = workbook_data

		# program.gather_room_data(file_path, room_detail_sheet)
		#program.generate_seating(file_path, sheet_name, room_detail_sheet, sample_count)
		program.load_json(process_to_use, json_data_to_use)
		program.generate_seating(json_data, room_data)

program.main()