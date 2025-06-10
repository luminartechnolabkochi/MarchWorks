students = [
    {
        "id": 1,
        "name": "Anjali Menon",
        "course": "Computer Science",
        "gpa": 8.6,
        "passoutyear": 2023,
        "skills": ["Python", "Django", "HTML", "CSS"]
    },
    {
        "id": 2,
        "name": "Rahul Nair",
        "course": "Mechanical Engineering",
        "gpa": 7.8,
        "passoutyear": 2022,
        "skills": ["AutoCAD", "SolidWorks", "MATLAB"]
    },
    {
        "id": 3,
        "name": "Sneha Ramesh",
        "course": "Information Technology",
        "gpa": 9.1,
        "passoutyear": 2024,
        "skills": ["JavaScript", "React", "Node.js"]
    },
    {
        "id": 4,
        "name": "Vivek Kumar",
        "course": "Electronics and Communication",
        "gpa": 8.3,
        "passoutyear": 2023,
        "skills": ["VLSI", "Embedded Systems", "C"]
    },
    {
        "id": 5,
        "name": "Meera Raj",
        "course": "Civil Engineering",
        "gpa": 7.5,
        "passoutyear": 2021,
        "skills": ["STAAD Pro", "AutoCAD", "Site Management"]
    },
    {
        "id": 6,
        "name": "Amit Shankar",
        "course": "Computer Applications",
        "gpa": 8.9,
        "passoutyear": 2024,
        "skills": ["Java", "Spring Boot", "SQL"]
    },
    {
        "id": 7,
        "name": "Divya Joseph",
        "course": "Data Science",
        "gpa": 9.2,
        "passoutyear": 2023,
        "skills": ["Python", "Pandas", "Machine Learning"]
    },
    {
        "id": 8,
        "name": "Nikhil Thomas",
        "course": "Computer Science",
        "gpa": 7.7,
        "passoutyear": 2022,
        "skills": ["PHP", "MySQL", "Laravel"]
    },
    {
        "id": 9,
        "name": "Arjun Das",
        "course": "Electronics",
        "gpa": 8.1,
        "passoutyear": 2023,
        "skills": ["Microcontrollers", "PCB Design", "C++"]
    },
    {
        "id": 10,
        "name": "Sandra Philip",
        "course": "Artificial Intelligence",
        "gpa": 9.5,
        "passoutyear": 2025,
        "skills": ["Deep Learning", "NLP", "TensorFlow"]
    },
    {
        "id": 11,
        "name": "Ravi Menon",
        "course": "Electrical Engineering",
        "gpa": 8.0,
        "passoutyear": 2022,
        "skills": ["Power Systems", "MATLAB", "SCADA"]
    },
    {
        "id": 12,
        "name": "Krishna Mohan",
        "course": "Computer Science",
        "gpa": 8.8,
        "passoutyear": 2023,
        "skills": ["Flask", "JavaScript", "MongoDB"]
    },
    {
        "id": 13,
        "name": "Lakshmi B",
        "course": "Information Systems",
        "gpa": 8.2,
        "passoutyear": 2022,
        "skills": ["Excel", "SQL", "Data Visualization"]
    },
    {
        "id": 14,
        "name": "Akhil Raj",
        "course": "Cybersecurity",
        "gpa": 9.0,
        "passoutyear": 2024,
        "skills": ["Network Security", "Linux", "Ethical Hacking"]
    },
    {
        "id": 15,
        "name": "Neha Santhosh",
        "course": "Software Engineering",
        "gpa": 8.7,
        "passoutyear": 2023,
        "skills": ["Agile", "Scrum", "JIRA"]
    }
]

student_name_filter=[st.get("name") for st in students if st.get("name")[0]=="A"]

print(student_name_filter)
