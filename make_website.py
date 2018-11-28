def read_resume(file_name):
	'''read in resume.txt and 
	store it in program's memory as 
	variable f
	'''

	#decare an empty list resume to store file into memory
	resume = []
	#open input file and append each line to resume
	with open(file_name,'r') as f:
		for line in f:
			resume.append(line)
	#return resume as output
	return resume

def name_detection(resume):
	'''Detect the name in resume and 
	raise an error if the first character in 
	the name string is not 'A' through 'Z'
	'''

	#get the first line in resume, store as name
	for line in resume:
		name = line.strip('\n')
		break
	#get the list of upper letters by listing all the uppercase letters
	Upper_Letter = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N'\
	'O','P','Q','R','S','T','U','V','W','X','Y','Z']
	#if the first letter of name is not an upper letter, raise an error
	if name[0] not in Upper_Letter:
		raise ValueError('The first line of resume must be name with proper capitalization')
	#return name, which is a string
	return name

def email_detection(resume):
	'''detect the email address in resume 
	'''

	#declare a list of numbers
	numbers = ['1','2','3','4','5','6','7','8','9','0']
	#iterate though list resume
	for line in resume:
		#find the line with '@'
		if '@' in line:
			#check if there is number in that line
			for num in numbers:
				#if numbers in line, raise value error
				if num in line:
					raise ValueError('This is not a valid email address')
			#equate the line with email w/o the \n at the end
			email = line.strip('\n')
			#break outof the for loop once email is found
			break
	#check if the email ends with .com or .edu, or if there is number
	if email[-4:] != '.com' and email[-4:] != '.edu':
		#if not, raise value error and print error message
		raise ValueError('This is not a valid email address')
	#otherwise, return the email
	else:
		return email 

def course_detection(resume):
	'''looks for the word Courses in resume
	and extract the line that contains that word
	'''

	#iterate through list resume
	for line in resume:
		#fine the line with Courses
		if 'Courses' in line:
			#store that line into courses w/o the end \n
			courses = line.strip('\n')
			#break out of the for loop once found courses 
			break
	#remove any random punctuation in courses
	courses = courses.replace(' : ','  ')
	courses = courses.replace(' :- ','  ')
	#return a list of courses
	return courses

def project_detection(resume):
	'''looks for the word Project in the resume
	'''

	#declare an empty list project
	project = []
	#iterate through the resume to find the line with project
	for i in range(len(resume)):
		if 'Project' in resume[0]:
			#break after that line is found
			break
		#remove all the provious lines in resume
		resume.remove(resume[0])

	#iterate again through the remaining of resume
	for line in resume:
		#append the elements into the project
		project.append(line.strip('\n'))
		#if that line is an empty line remove that line
		if '' in project:
			project.remove('')
		#if at least 10 minus signs are met, stop appending to line
		if '----------' in line:
			break
	#return the list of projects
	return project

def surround_block(tag, text):
	'''This function surrounds the given text with
	the given html tag and returns the string
	'''

	#add the tag to text with correct format
	text = '<'+tag+'>'+text+'</'+tag+'>'
	#return '<tag>text</tag>'
	return text

def formating_resume_intro(name,email):
	'''formate the intro section of resume
	for writing to a file in the correct format
	'''

	#format the name with tag
	name = surround_block('h1',name)
	#format email with tag
	email = surround_block('p','Email: '+email)
	#join them together with tag to get intro
	intro = surround_block('div',name+email)
	#return the formated intro
	return intro

def formating_project(project):
	'''format the projects in resume for writing to a file
	'''
	#declare empty string content
	content = ''
	#format title with tag
	title = surround_block('h2',project[0])
	#format each project with tag and add them together in content
	for i in range(1,len(project)-1):
		content += surround_block('li',project[i])
	#format content with tag
	content = surround_block('ul',content)
	#join title and content together line seperated
	project = title + '\n' + content
	#format the project with tag s
	project = surround_block('div',project)
	#return the formatted project
	return project

def formating_courses(courses):
	'''format the courses section of resume for 
	writing to a file
	'''

	#seperate title and content in courses
	courses = courses.split('  ')
	#format title and contents with tags
	title = surround_block('h3',courses[0])
	content = surround_block('span',courses[1])
	#format courses by join title and content together and add the tag
	courses = surround_block('div',title+content)
	#return the formatted courses
	return courses

def writing_html(intro, project, courses, file):
	#open output file
	f = open(file, 'r+')
	#read the contents into lines
	lines = f.readlines()
	#delete every thing from file
	f.seek(0)
	f.truncate()
	#delete the last two lines in lines
	del lines[-1]
	del lines[-1]
	#write the lines to output file s
	f.writelines(lines)
	#write out desired contents into output file s
	f.write('<div id="page-wrap">')
	f.write(intro+'\n')
	f.write(project+'\n')
	f.write(courses+'\n')
	f.write('</div>\n')
	f.write('</body>\n')
	f.write('</html>\n')
	#close the file to save
	f.close()
	


def main():
	#specify the input file 
	input_file = 'resume.txt'
	#read and store the input file into list resume
	resume = read_resume(input_file)
	#get name from resume
	name = name_detection(resume)
	#get email from resume
	email = email_detection(resume)
	#get courses from resume
	courses = course_detection(resume)
	#get projects from resume
	project = project_detection(resume)
	#specify the output file
	output_file = 'resume.html'
	#format the intro
	intro = formating_resume_intro(name,email)
	#format the projects
	project = formating_project(project)
	#format the courses 
	courses = formating_courses(courses)
	#write to output file
	writing_html(intro,project,courses,output_file)


if __name__  == '__main__':
	main()