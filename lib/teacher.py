#!/usr/bin/env python

import random
from lib.user import User  # Correct import

class Teacher(User):  # Inherits from User
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)  # Correct `super()` call

    def teach(self):
        return random.choice(self.knowledge)
