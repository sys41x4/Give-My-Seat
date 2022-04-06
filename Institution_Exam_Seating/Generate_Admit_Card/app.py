from flask import Flask, make_response, jsonify, render_template, request
from waitress import serve
import pdfkit
import os

import qrcode
from PIL import Image
from io import BytesIO
from datetime import datetime

import json
import base64

import sys

# run the script with the arguments
# python app.py <confirmed_seating_path> <Institute_Name>


print(f"""
{'*'*50}			
# Developed by Arijit Bhowmick [sys41x4]
# Lisence Type : GNU AGPLv3 [GNU Affero General Public License v3.0]
# https://choosealicense.com/licenses/agpl-3.0/

# Project Available at :
# https://github.com/Arijit-Bhowmick/Give-My-Seat
# https://github.com/sys41x4/Give-My-Seat
{'*'*50}

Give My Seat [Institution Exam Seating](Generate Admit Card)

GMS_IES_GAD

     ==-.                     
   -@@@@@.                    
   :@@@@@=                    
    :@@@@                     
  -=@@@@#.          .         
 %@@@@@@@@@#.     .*-         
-@@@@@@@@@@@@.   =+           
 @@@@@@@@@@@@# .*:  .         
 :%@@@@@@@@@@@%%:=#%.         
   *%@@@@@@@@@@@@@@#+..       
   #@@@@@@@@@@@@@@@@@@@@%#*+: 
   .#@@@@@@@@@@@@@@@@@@@@@@@@.
     .=*@@@@@@@@@@@@@@#=@@@@= 
        *%@@@@@@@@@@@%-@@@@*  
         :+-=*%#%@@@@=@@@@#   
              *-*@@@@@@@@#    
              %#%@@@@@# :     
      .***#@@@@@@@@@@@%=      
       +++%#+-*@@@%:+@@@+     
       .@*     %@@@@..==      
        :.     =@@@#


\n\n
""")

def help_msg():
	print("""
Run The Script with the following Arguments\n
python app.py <host> <port> <Number_of_process_to_use> <Institute_Name> <confirmed_seating_path> <wkhtmltopdf_path> <qr_embed_img_path> <pdf_logo_webaddress>
""")

try:
	host = sys.argv[1]
	port = sys.argv[2]
	process = int(sys.argv[3])
	institute_name = sys.argv[4]
	if (os.path.exists(sys.argv[5])==False) or (os.path.exists(sys.argv[6])==False) or (os.path.exists(sys.argv[7])==False):raise IndexError
	confirmed_seating_data_path = sys.argv[5]
	# wkhtmltopdf_path = 'wkhtmltox\\bin\\wkhtmltopdf.exe'
	wkhtmltopdf_path = sys.argv[6]
	## embed logo in qr
	# logo_link = 'sample_images/icon.jpg'
	logo_link = sys.argv[7]

	## PDF logo on PDF
	# pdf_logo = 'https://avatars.githubusercontent.com/u/66935336?v=4'
	pdf_logo = sys.argv[8]
except IndexError:
	help_msg()
	sys.exit()



json_data=json.load(open(confirmed_seating_data_path))



## Flask Configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Hello_I_am_Arijit_Bhowmick_sys41x4'


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_admitcard',methods= ['POST'])
def home():
	data = request.get_json()
	roll_num = data['roll']
	aadhar_num =  data['aadhar']

	return jsonify({"roll_num":roll_num})

@app.route("/<aadhar_num>")
def roll_not_provided(aadhar_num):

	std_seating_info={"std_name": "","branch_name": "","roll_num": "Enrollment Number Not Provided","aadhar_num": aadhar_num,"block_num": "","room_num": "","row": "","column": ""}
	return generate_pdf(std_seating_info)

def generate_pdf(std_seating_info):
	std_seating_info.update({'base64_qr_str':gen_verifiable_qr_code(std_seating_info), 'institute_name':institute_name, 'pdf_logo':pdf_logo})
	rendered = render_template("pdf_templete.html", std_name = std_seating_info['std_name'], branch_name = std_seating_info['branch_name'], roll_num = std_seating_info['roll_num'], aadhar_num = std_seating_info['aadhar_num'], block_num = std_seating_info['block_num'], room_num = std_seating_info['room_num'], row = std_seating_info['row'], column = std_seating_info['column'], pdf_logo=std_seating_info['pdf_logo'], base64_qr_str=std_seating_info['base64_qr_str'], institute_name=std_seating_info['institute_name'])

	pdf = pdfkit.from_string(rendered, False, configuration=pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path))

	response = make_response(pdf)

	response.headers['Content-Type'] = 'application/pdf'
	
	response.headers['Content-Disposition'] = "inline;filename="+std_seating_info['roll_num']+"_"+str(datetime.date(datetime.now()))+".pdf"

	return response

@app.route("/<aadhar_num>/<roll_num>")
def admitcard(aadhar_num, roll_num):
	global confirmed_seating_data_path

	std_seating_info = fetch_json_data(confirmed_seating_data_path, roll_num.upper(), aadhar_num.upper())
	

	return generate_pdf(std_seating_info)

def fetch_json_data(confirmed_seating_data_path, roll_num, aadhar_num):

	global json_data

	try:
		std_seating_info = json_data[roll_num]
		if aadhar_num != std_seating_info["aadhar_num"]:
			return {"std_name": "","branch_name": "","roll_num": roll_num,"aadhar_num": "Aadhar Number is Not Valid","block_num": "","room_num": "","row": "","column": "" }
	
	except KeyError:
		return {"std_name": "","branch_name": "","roll_num": "Enrollment Number is Not Valid","aadhar_num": "","block_num": "","room_num": "","row": "","column": "" }

	return std_seating_info

def gen_verifiable_qr_code(student_seating_data):
	global logo_link
	logo = Image.open(logo_link)

 	# taking base width
	basewidth = 65

 	# adjust image size
	wpercent = (basewidth/float(logo.size[0]))
	hsize = int((float(logo.size[1])*float(wpercent)))
	logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)

	qr_color = '#212529'

	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_H,
		box_size=3,
		border=3,
	)

	student_seating_data = json.dumps(student_seating_data, indent = 1)

	qr.add_data(student_seating_data)

	qr.make(fit=True)

	# adding color to QR code
	qr_img = qr.make_image(
		fill_color=qr_color, back_color="white").convert('RGB')

	# set size of QR code
	pos = ((qr_img.size[0] - logo.size[0]) // 2,
	       (qr_img.size[1] - logo.size[1]) // 2)
	qr_img.paste(logo, pos)

	buffered = BytesIO()
	qr_img.save(buffered, format="JPEG")

	base64_qr_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

	return base64_qr_str 

if __name__ == "__main__":
	# app.run(host=host, debug=False, port=port)
	print(f"Starting Production Server at {host}:{port}")
	serve(app, host=host, port=port)