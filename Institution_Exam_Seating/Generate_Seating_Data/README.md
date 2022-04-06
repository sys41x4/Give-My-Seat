# Give-My-Seat
## [Institution Exam Seating] [Generate Seating Data]

---

### Process to use
[1] Using `Excel WorkBook` having extension `.xlsx`

**Test Excel WorkBook Data**

**[Student Data Sheet Example]**

| std_name | std_rollnum | std_branch | std_aadhar |
| - | - | - | - |
| student1 | rollnum1 | branch2 | aadhar1 |
| student2 | rollnum2 | branch1 | aadhar2 |
| student3 | rollnum3 | branch1 | aadhar3 |
| student4 | rollnum4 | branch3 | aadhar4 |
| student5 | rollnum5 | branch3 | aadhar5 |
| student6 | rollnum6 | branch1 | aadhar6 |
| student7 | rollnum7 | branch1 | aadhar7 |
| student8 | rollnum8 | branch3 | aadhar8 |
| student9 | rollnum9 | branch3 | aadhar9 |
| student10 | rollnum10 | branch3 | aadhar10 |
| student11 | rollnum11 | branch1 | aadhar11 |
| student12 | rollnum12 | branch3 | aadhar12 |
| student13 | rollnum13 | branch2 | aadhar13 |
| student14 | rollnum14 | branch3 | aadhar14 |
| student15 | rollnum15 | branch3 | aadhar15 |
| student16 | rollnum16 | branch3 | aadhar16 |

**[Room Data Sheet Example]**

| block_name | room_name | row | column |
| - | - | - | - |
| F | A1 | 12 | 4 |
| F | A2 | 11 | 5 |
| F | A3 | 11 | 4 |
| G | S1 | 12 | 5 |
| G | S2 | 12 | 4 |
| G | S3 | 12 | 4 |
| G | S4 | 12 | 5 |
| K | J9 | 11 | 4 |

a. Enter `Excel WorkBook path`
	Example : `data.xlsx`

b. Enter `Student Data Sheet Name`
	Example : `student_data`

c. Enter `Room Data Sheet Name`
	Example : `room_data`

d. Enter `Time Period of Seat Booking`
	Example : `20.03.2022-20.04.2022`

e. Enter `Do you want to dump generated data to excel ?`
	Example : `Y` or `N`

f. Enter `Sample Count (Used during Matrix Formation)`
	The More the sample count,
	the more will the script use the system resource,
	and the more perfect will be the seating data
	(Default: 1)
	Example : `10`

g. Enter `Want to get the output in terminal ?`
	Example : `Y` or `N`


[2] Using Previous JSON Files created using this script

a. Enter `student_data` `JSON` File Location
		Example : `student_data.json`

b. Enter `room_data` `JSON` File Location
		Example : `room_data.json`

c. Enter `seating_data` `JSON` File Location
		Example : `seating_data.json`
		We can also leave it empty without entring any data, if there is no previous `seating_data` JSON file available

d. Enter `Time Period of Seat Booking`
	Example : `20.03.2022-20.04.2022`

e. Enter `Do you want to dump generated data to excel ?`
	Example : `Y` or `N`

f. Enter `Sample Count (Used during Matrix Formation)`
	The More the sample count,
	the more will the script use the system resource,
	and the more perfect will be the seating data
	(Default: 1)
	Example : `10`

g. Enter `Want to get the output in terminal ?`
	Example : `Y` or `N`

#### Speific Instructions during data fetching

1. Use the `column name` of `student data sheet`, as follows:
	a. Student Name Column Name -> `std_name`
	b. Student Roll Number Column Name -> `std_rollnum`
	c. Student Branch Name Column Name -> `std_branch`
	d. Student Aadhar Column Name -> `std_aadhar`

2. Use the `column name` of `Room Data Sheet`, as follows:
	a. Block Name Column Name -> `block_name`
	b. Room Name Column Name -> `room_name`
	c. Total Row Count in the specified room -> `row`
	d. Total Column Count in the specified room -> `column`

---

Data generated will be created under `<Starting_Date>-<Ending Date>-<Current Date>` Directory.

* After providing data the `assigned_seating_data.json` file will be created where all students with their **Seating Details** will be available. Further more if you want to get the data in excel sheet, then you can specify `Y/N` when the program start to run, and it will create `assigned_seating_data.xlsx`, having single sheet named as `Seating Data <Current Date>`

* `unassigned_room_data.json` will be created which show the leftover/unallocated Rooms

* `unassigned_student_data.json` will be created in each step, while at the end there would be an empty data dictionary, with only some keys