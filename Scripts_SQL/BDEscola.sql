CREATE TABLE Professores (
	id_professor SERIAL PRIMARY KEY,
	nome_prof VARCHAR(255) NOT NULL,
	cpf_prof VARCHAR (50) UNIQUE NOT NULL,
	data_nasc_prof DATE NOT NULL,
	telefone VARCHAR (11) NOT NULL,
	formacao VARCHAR (50) NOT NULL

);

CREATE TABLE Alunos (
	id_aluno SERIAL PRIMARY KEY,
	nome_aluno VARCHAR(255) NOT NULL,
	cpf_aluno VARCHAR (50) UNIQUE NOT NULL,
	data_nasc_aluno DATE NOT NULL,
	telefone_aluno VARCHAR (11) NOT NULL
);

CREATE TABLE Cursos (
		id_curso SERIAL PRIMARY KEY,
		nome_curso VARCHAR(50) NOT NULL,
		periodo VARCHAR(50) NOT NULL,
		carga_horaria VARCHAR (20) NOT NULL, 
		vagas VARCHAR (10) NOT NULL
);


CREATE TABLE Matriculas (
	id_matricula SERIAL PRIMARY KEY,
	
	id_aluno INT NOT NULL,
	id_curso INT NOT NULL,
	
	FOREIGN KEY (id_aluno)
		REFERENCES Alunos(id_aluno),
	FOREIGN KEY (id_curso)
		REFERENCES Cursos (id_curso)
);


CREATE TABLE Professores_Cursos(
	id_professor INT NOT NULL,
	id_curso INT NOT NULL,
	PRIMARY KEY (id_professor, id_curso),
	FOREIGN KEY (id_professor) REFERENCES Professores (id_professor),
	FOREIGN KEY (id_curso) REFERENCES Cursos (id_curso)
	
	
);

CREATE TABLE Alunos_Matriculas(
	id_aluno INT NOT NULL,
	id_matricula INT NOT NULL,
	
	primary key(id_aluno, id_matricula),
	FOREIGN KEY (id_aluno) REFERENCES Alunos (id_aluno),
	FOREIGN KEY (id_matricula) REFERENCES Matriculas (id_matricula)
);

CREATE TABLE Cursos_Matriculas(
	id_curso INT NOT NULL,
	id_matricula INT NOT NULL,
	
	PRIMARY KEY (id_curso, id_matricula),
	FOREIGN KEY (id_curso) REFERENCES Cursos (id_curso),
	FOREIGN KEY (id_matricula) REFERENCES Matriculas (id_matricula)
	
);