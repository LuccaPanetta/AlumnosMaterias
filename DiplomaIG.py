# Lista de alumnos 

subject_dict = {'0400' : 'ART AND DESIGN', 
'0450' : 'BUSINESS STUDIES', 
'0470' : 'HISTORY', 
'0475' : 'LITERATURE IN ENGLISH', 
'0478' : 'COMPUTER SCIENCE', 
'0500' : 'FIRST LANGUAGE ENGLISH (ORAL ENDORSEMENT)', 
'0502' : 'FIRST LANGUAGE SPANISH', 
'0580' : 'MATHEMATICS (WITHOUT COURSEWORK)', 
'0610' : 'BIOLOGY', 
'0099' : 'CHEMISTRY', 
'0077' : 'PHYSICS', 
'0088' : 'GERMAN LANGUAGE', 
'0044' : 'ENVIRONMENT'}


class Alumno():
	def __init__ (self, nombre, colegio, candidato):
		self.name = nombre
		self.school = colegio
		self.candidate = candidato
		self.subject_ok = []
	
	def exam_result(self, subject, grade):
		if grade != 'U':
			self.subject_ok.append(subject)
			
	def diploma (self):
		if len(self.subject_ok) > 6:
			return True

	def get_candidate(self):
		return(self.candidate)

	def get_name(self):
		return(self.name)

	def verify_subject(self, subject):
		if subject in self.subject_ok:
			return True
		else:
			return False

	def return_subjects(self):
		return self.subject_ok





Lista_Alumnos=[]

# Proceso el archivo de alumnos
alu_file=open("Alumnos.txt", "r")
alu=alu_file.readline()
while len(alu) > 0:
	a,b,c = alu.split(',',2)
	Lista_Alumnos.append(Alumno(a,b,c.strip()))
	alu=alu_file.readline()
alu_file.close()

# Función para encontrar un alumno (devuelve posición)
def find_student(candidate_code):
	position=-1
	for i in range (len (Lista_Alumnos)):
		if Lista_Alumnos[i].get_candidate() == candidate_code:
			position = i
			break
	return position

# Procesar archivo notas
results_file=open('results.txt', 'r')
r_candidate=results_file.readline()

while len(r_candidate)>0:
	student_index = find_student(r_candidate.strip())
	r_subject= results_file.readline()
	r_result=results_file.readline()
	Lista_Alumnos[student_index].exam_result(r_subject.strip(), r_result.strip())
	r_candidate=results_file.readline()
results_file.close()	
	
# ver qué alumnos consiguieron diploma
print("Detalle de alumnos que consiguieron el diploma")
for i in range (len (Lista_Alumnos)):
	if Lista_Alumnos[i].diploma() == True:
		print( Lista_Alumnos[i].get_candidate() + "   " + Lista_Alumnos[i].get_name() )
print("\n")


# Lista de alumnos que aprobaron una materia
materia= '0400' #input("Ingrese materia a listar")
print("            " + subject_dict[materia])
for i in range (len (Lista_Alumnos)):
	if Lista_Alumnos[i].verify_subject(materia) == True:
		print(Lista_Alumnos[i].get_candidate().rjust(10), Lista_Alumnos[i].get_name().ljust(40))
print("\n")


# Lista de materias que aprobó un alumno
alumno= 'AR310' #input("Ingrese candidate code del alumno a listar")
student_index = find_student(alumno)
print(Lista_Alumnos[student_index].get_candidate() + "   " +  Lista_Alumnos[student_index].get_name())
lista_materias= Lista_Alumnos[student_index].return_subjects()
for i in range (len(lista_materias)):
	print(lista_materias[i].center(10) + subject_dict[lista_materias[i]].ljust(20))




