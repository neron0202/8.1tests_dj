import pytest
from _pytest import python
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@python.mark.django_db
def test_create_course(client, course_factory):
    #Arrange
    courses = course_factory(_quantity=1)

    #Act
    response = client.get('/api/v1/courses/')

    #Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)







def test_example():
    assert False, "Just test example"
