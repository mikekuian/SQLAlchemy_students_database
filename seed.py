import faker
from random import randint, choice
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Group, Student, Teacher, Subject, Grade

# Налаштування підключення до бази даних
engine = create_engine("postgresql://postgres:mysecretpassword@localhost:5432/postgres")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

NUMBER_OF_STUDENTS = 50
NUMBER_OF_GROUPS = 3
NUMBER_OF_SUBJECTS = 10
NUMBER_OF_TEACHERS = 5
NUMBER_OF_GRADES = NUMBER_OF_STUDENTS * 20

# Генератор фейкових даних
fake = faker.Faker()

def generate_fake_data():
    # Створення груп
    groups = [Group(name=f'Group {i + 1}') for i in range(NUMBER_OF_GROUPS)]
    session.add_all(groups)

    # Створення вчителів
    teachers = [Teacher(name=fake.name()) for _ in range(NUMBER_OF_TEACHERS)]
    session.add_all(teachers)

    # Створення предметів
    subjects = [Subject(name=fake.job(), teacher=choice(teachers)) for _ in range(NUMBER_OF_SUBJECTS)]
    session.add_all(subjects)

    # Створення студентів і оцінок
    for _ in range(NUMBER_OF_STUDENTS):
        group = choice(groups)
        student = Student(name=fake.name(), group=group)
        session.add(student)
        # Для кожного студента генеруються випадкові оцінки з кожного предмету
        for subject in subjects:
            for _ in range(5):  # Кожен студент отримує 5 оцінок з кожного предмету
                grade = Grade(student=student, subject=subject, grade=randint(1, 100), timestamp=fake.past_date())
                session.add(grade)

    session.commit()

if __name__ == "__main__":
    generate_fake_data()
    print("Data generated successfully!")
    session.close()
