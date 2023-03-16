"""Defines a registration system with access code for a home alarm system.
"""

import json
from random import randint


class Register():
    """A class that represents a registration system.
    """

    def add(self, chat: str, name: str, username: str):
        """Adds a new habitant to the system, if he is not already registered.

        Args:
            chat (str): Telegram ID associated to private chat
            name (str): User's Telegram name
            username (str): User's Telegram username

        Returns:
            bool: Success adding the habitant
        """
        no_file = False
        habitant_at_home = True

        try:
            with open("home.txt", mode="r", encoding="utf-8") as file:
                habitants = json.load(file)
                # Remove username from habitants
                users = habitants.get('users')
                habitant_at_home = [
                    user for user in users if user.get('username') == username
                ]
        except OSError:
            no_file = True

        if no_file or not habitant_at_home:
            habitant = {
                'chat': chat,
                'name': name,
                'username': username,
                'access_code': self.generate_access_code(),
            }

            if no_file:
                habitants = {'users': [habitant]}
            else:
                users.append(habitant)
                habitants = {'users': users}
            # Create a new file and save it
            with open("home.txt", mode="w", encoding="utf-8") as file:
                file.write(json.dumps(habitants))
                file.close()
            return True
        return False

    def remove(self, username: str):
        """Removes an habitant if he is already registered.

        Args:
            username (str): User's Telegram username

        Returns:
            bool: Success removing the habitant
        """
        with open("home.txt", mode="r", encoding="utf-8") as file:
            habitants = json.load(file)
            users = habitants.get('users')
            num_prev_habitants = len(users)
            # Remove username from habitants
            users = [
                user for user in users if user.get('username') != username
            ]
            habitants['users'] = users

        with open("home.txt", mode="w", encoding="utf-8") as file:
            file.write(json.dumps(habitants))
            file.close()
        if len(users) == num_prev_habitants:
            return False
        return True

    def get(self):
        """Gets all the users chat IDs and names.

        Returns:
            tuple(str, str): Tuple with chat and user's name
        """
        with open("home.txt", mode="r", encoding="utf-8") as file:
            habitants = json.load(file)
            users = habitants.get('users')

            notifications = []
            for user in users:
                notifications.append((user.get('chat'), user.get('name')))

            return notifications

    def generate_access_code(self):
        """Generates a random number of 4 digits that is not already in use.

        Returns:
            int: 4 digit access code
        """
        with open("home.txt", mode="r", encoding="utf-8") as file:
            habitants = json.load(file)
            users = habitants.get('users')
            codes = [user.get('access_code') for user in users]

        new_code = randint(1000, 9999)
        # Ensure code is unique
        while new_code in codes:
            new_code = randint(1000, 9999)
        return new_code

    def login(self, access_code: int):
        """Checks whether the given access_code is from a registered habitant or not.

        Args:
            access_code (int): 4 digit access code

        Returns:
            str/bool: Logged user's name or False if not found
        """
        with open("home.txt", mode="r", encoding="utf-8") as file:
            habitants = json.load(file)
        users = habitants.get('users')
        user_logged = [
            user for user in users if user.get('access_code') == access_code
        ]

        if user_logged:
            return user_logged[0].get('name')
        return False

    def get_code(self, username: str):
        """Gets the code of the user with a certain username, if he is already registered.

        Args:
            username (str): User's Telegram username

        Returns:
            int/bool: User's access code or False if not found
        """
        with open("home.txt", mode="r", encoding="utf-8") as file:
            habitants = json.load(file)
        users = habitants.get('users')
        user_code = [
            user for user in users if user.get('username') == username
        ]

        if user_code:
            return user_code[0].get('access_code')
        return False
