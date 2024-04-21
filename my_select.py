from connect_db import session
from models import Group, Student, Teacher, Subject, Grade
from sqlalchemy import func, desc


def select_1():
    return session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()


def select_2():
    return session.query(Student.name, Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade).join(Student).join(Subject).where(Subject.name == 'Lobbyist') \
        .group_by(Student.name, Subject.name).order_by(desc('avg_grade')).limit(1).all()


def select_3():
    return session.query(Group.name, Subject.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Student).join(Grade).join(Subject).join(Group).where(Subject.name == 'Lobbyist') \
        .group_by(Group.name, Subject.name).all()


def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).all()


def select_5():
    return session.query(Teacher.name, Subject.name).select_from(Teacher).join(Subject) \
            .where(Teacher.name == 'Benjamin Bauer MD').all()


def select_6():
    return session.query(Group.name, Student.name).select_from(Group).join(Student) \
            .where(Group.name == '8843').all()


def select_7():
    return session.query(Group.name, Subject.name, Grade.grade).select_from(Group).join(Student).join(Grade) \
            .join(Subject).where(Group.name == '8843', Subject.name == 'Lobbyist').all()


def select_8():
    return session.query(Teacher.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Teacher) \
        .join(Subject).join(Grade).where(Teacher.name == 'Benjamin Bauer MD').group_by(Teacher.name).all()


def select_9():
    return session.query(Student.name, Subject.name).select_from(Student).join(Grade).join(Subject) \
            .where(Student.name == 'John Smith').group_by(Student.name, Subject.name).all()


def select_10():
    return session.query(Student.name, Teacher.name, Subject.name).select_from(Student).join(Grade).join(Subject) \
        .join(Teacher).where(Student.name == 'John Smith', Teacher.name == 'Benjamin Bauer MD') \
        .group_by(Student.name, Teacher.name, Subject.name).all()


print(select_1())
