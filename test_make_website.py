#import the file being tested
from make_website import *

#import unittest module
import unittest

#define a class of unittest
class Testmakewebsite(unittest.TestCase):

	def test_read_resume(self):
		resume = read_resume('resume.txt')
		self.assertEqual(type(resume),list)
		lines = ''
		with open ('resume.txt') as f:
			for line in f:
				self.assertTrue(line in resume)

	def test_name_detection(self):
		my_name= ['Daizhen Li']
		more_name = ['Dai\n']
		lower_name = ['daizhen li']
		self.assertEqual('Daizhen Li', name_detection(my_name), 'check the normal functionality')
		self.assertEqual('Dai',name_detection(more_name),'Get rid of the new line in the end')
		#test if it catches non-capital letter
		with self.assertRaises(ValueError):
			name_detection(lower_name)

	def test_email_detection(self):
		email = ['dli@seas.upenn.edu']
		email2 = ['dli@seas.upenn']
		email3 = ['dli29@seas.upenn.edu']
		self.assertEqual('dli@seas.upenn.edu',email_detection(email),'Test the functionality')
		#test if it catches non-valid email
		with self.assertRaises(ValueError):
			email_detection(email2)
		self.assertRaises(ValueError,email_detection,email3)
	def test_course_detection(self):
		courses = ['Courses :- Picking Apple, Eating Apple']
		courses2 = ['Courses : This is Fun, Not at All']
		self.assertEqual('Courses  Picking Apple, Eating Apple',course_detection(courses))
		self.assertEqual('Courses  This is Fun, Not at All', course_detection(courses2))

	def test_project_detection(self):
		resume = ['Blahblah', 'Projects', 'A','B','------------------------','Blahblah']
		self.assertEqual(['Projects','A','B','------------------------'],project_detection(resume))
		resume_with_blank_line = ['Projects','A','','B','','------------------------']
		self.assertEqual(['Projects','A','B','------------------------']\
			,project_detection(resume_with_blank_line))

	def test_surround_block(self):
		tag = 'Awesome'
		text = 'Programmer'
		self.assertEqual('<Awesome>Programmer</Awesome>',surround_block(tag,text))

	def test_formating_resume_intro(self):
		name = 'Daizhen Li'
		email = 'dli29@seas.upenn.edu'
		self.assertEqual('<div><h1>Daizhen Li</h1><p>Email: dli29@seas.upenn.edu</p></div>',\
		formating_resume_intro(name,email))

	def test_formating_project(self):
		project = ['Projects','A','B','------------------------']
		self.assertEqual('<div><h2>Projects</h2>\n<ul><li>A</li><li>B</li></ul></div>',formating_project(project))

	def test_formating_courses(self):
		courses = 'Courses  Picking Apple, Eating Apple'
		self.assertEqual('<div><h3>Courses</h3><span>Picking Apple, Eating Apple</span></div>',formating_courses(courses))
	#-------------------------------------------------------------------
	#This is for if you ever want to test the write to file function

	#def test_writing_html(self):
		#better use a different file than the ones used in make_website.py
		#file = 'resume.html'
		#intro = '<div><h1>Daizhen Li</h1><p>Email: dli29@seas.upenn.edu</p></div>'
		#project = '<div><h2>Projects</h2>\n<ul><li>A</li><li>B</li></ul></div>'
		#courses = '<div><h3>Courses</h3><span>Picking Apple, Eating Apple</span></div>'
		#writing_html(intro, project, courses, file)
		#f = open(file,'r+')
		#lines = ''
		#for line in f:
		#	lines += line
		#self.assertTrue(intro in lines)
		#self.assertTrue(project in lines)
		#self.assertTrue(courses in lines)




if __name__ == '__main__':
	unittest.main()