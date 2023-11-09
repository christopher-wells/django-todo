from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(task_name='Test Task')

    def test_task_creation(self):
        task = Task.objects.get(id=1)
        self.assertEqual(task.task_name, 'Test Task')
        self.assertFalse(task.task_complete)  # task should be initially incomplete

    def test_task_update_completion(self):
        task = Task.objects.get(id=1)
        task.task_complete = True
        task.save()
        updated_task = Task.objects.get(id=1)
        self.assertTrue(updated_task.task_complete)  # task completion status should be updated

    def test_task_ordering(self):
        task1 = Task.objects.create(task_name='Task 1')
        task2 = Task.objects.create(task_name='Task 2')
        tasks = Task.objects.all()
        self.assertEqual(tasks[0], self.task)  # first task should be the one created in setUp()
        self.assertEqual(tasks[1], task1)  # second task should be Task 1
        self.assertEqual(tasks[2], task2)  # third task should be Task 2

    def test_task_absolute_url(self):
        task = Task.objects.get(id=1)
        expected_url = reverse('tasks:index')
        self.assertEqual(task.get_absolute_url(), expected_url)
