import csv
import requests
import time

access_token = "YOUR_ACCESS_TOKEN"
course_id="COURSE_ID"
project_id="ASSIGNMENT_ID"
grades_file="GRADE_FILE.csv"

url = "https://gatech.instructure.com/api/v1/courses/"+course_id+"/assignments/"+project_id+"/submissions/"
headers = {'Content-Type':'application/json', 'Authorization': 'Bearer {}'.format(access_token)}

with open(grades_file, "r") as f:
	reader = csv.reader(f, delimiter=',', quotechar='"')
	for row in reader:
		# add student id in url
		student_url = url+row[1]

		# add score in request body
		params = {"submission[posted_grade]": row[2]}
		r = requests.put(student_url, headers=headers, params=params)

		# print the student name
		print row[0]

		# print response
		print r

		# wait a while
		time.sleep(1)

f.close()

