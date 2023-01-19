use lesson;

CREATE TABLE Subject(
	id INT AUTO_INCREMENT,
    title varchar(100) not null,
    lessons_number int,
    
    primary key(id)
);

CREATE TABLE IT_Group(
	id INT auto_increment,
    title varchar(100) not null,
    primary key(id)
);

CREATE TABLE Lesson(
	id int auto_increment,
    topic varchar(100),
    lesson_date date,
    start_time 	timestamp,
    lesson_type enum("Основна", "Заміна", "Відпрацювання", "Відробка", "Пробне", "Індивідуальне"),
    group_id int,
    subject_id int,
    topic_num int,
    
    primary key(id),
    foreign key(group_id) references IT_Group(id),
    foreign key(subject_id) references Subject(id)
);

ALTER TABLE Lesson DROP COLUMN start_time;
ALTER TABLE Lesson ADD COLUMN needs_working_out BOOL;
