#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Knight:
    """
    Die Klasse Knight repräsentiert einen Ritter mit spezifischen Eigenschaften, Fähigkeiten und Lebenspunkten.

    """

    armor = True

    def __init__(self, full_name: str, special_ability: str,
                 skill: float, round_table: bool = True):
        """
        Initialisiert einen neuen Ritter mit den folgenden Attributen:

        :param full_name:
        :param special_ability:
        :param skill:
        :param round_table:
        """
        self.full_name = full_name
        self._special_ability = special_ability
        self.skill = skill
        self.round_table = round_table
        self.__health = 100

    @property
    def health(self):
        """

        :param self:
        :return: __health
        """
        return self.__health

    @health.setter
    def health(self, value):
        """

        :param self:
        :param value:
        :return:
        """
        if value > 0:
            self.__health = value
        else:
            raise ValueError("Death is not an option.")

    def __repr__(self):
        """

        :param self:
        :return:
        """
        return f"{self.full_name} is at {self.health}% health"

    def duel(self, other):
        """

        :param self:
        :param other:
        :return:
        """
        if self.round_table and other.round_table:
            print("Knights of the Round Table don't fight each other.")
        else:
            if self.skill > other.skill:
                other.health -= 20
                print(f"{self.full_name} wins, {other.full_name} loses.")
            else:
                self.health -= 20
                print(f"{other.full_name} wins, {self.full_name} loses.")


class King(Knight):
    """
    Die Klasse King erbt von Knight und repräsentiert einen König mit besonderen Eigenschaften.
    Ein König hat standardmäßig maximale Fähigkeiten und eine besondere Fähigkeit namens "aristocracy".
    """
    """

    def __init__(self, full_name: str, special_ability: str = 'aristocracy',
                 skill: float = float('inf'), round_table: bool = True):
        """

        :param full_name:
        :param special_ability:
        :param skill:
        :param round_table:
        """
        super().__init__(full_name, special_ability, skill, round_table)
        # self.special_ability = special_ability
        # self.skill = skill
        # self.round_table = round_table

    def __repr__(self):
        return f"The health of {self.full_name} is none of you business."

bedevere = Knight('Sir Bedevere the Wise', 'wisdom', 55)
lancelot = Knight('Sir Lancelot the Brave', 'bravery', 60)
black_knight = Knight('Black Knight', 'confidence', 100, False)
knight_of_ni = Knight('Knight Who Says Ni', 'ni', 55, False)

bedevere.duel(lancelot)
print(bedevere)
bedevere.duel(black_knight)
print(bedevere)
bedevere.duel(knight_of_ni)
print(bedevere)

arthur = King('King Arthur')
print(arthur)
