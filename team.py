"""
This file is part of Project Simulator.
Project Simulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Project Simulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from config import *


class Team():

    def __init__(self):
        self.team_salaries_per_minute = {}
        self.working_with_feature_team_salary = 0
        self.defect_fixing_team_salary = 0
        self.technical_depth_fixing_team_salary = 0
        self.release_team_salary = 0
        self.trouble_shooting_team_salary = {}
        self.regular_meetings_involvement_team_salary = {}
        self.__calculate_team_costs_per_minute()
        self.__init_working_with_feature_team_cost()
        self.__init_defect_fixing_team_cost()
        self.__init_technical_depth_fixing_team_cost()
        self.__init_regular_meetings_involvement_team_cost()
        self.__init_release_team_cost()
        self.__init_trouble_shooting_team_cost()

    def __calculate_team_costs_per_minute(self):
        for team_member, count in TEAM.items():
            self.team_salaries_per_minute[team_member] = round(
                ((((SALARY_PER_MONTH[team_member] * 12) / TEAM_WORKING_DAYS[team_member]) / 8) / 60) * count, 2)

    def __init_working_with_feature_team_cost(self):
        self.working_with_feature_team_salary = sum([self.team_salaries_per_minute[role]
                                                     for role
                                                     in PROFIT_ACTIVITIES["Feature"]["roles"]])

    def __init_defect_fixing_team_cost(self):
        self.defect_fixing_team_salary = sum([self.team_salaries_per_minute[role]
                                              for role
                                              in PROFIT_ACTIVITIES["Defect Fixing"]["roles"]])

    def __init_technical_depth_fixing_team_cost(self):
        self.technical_depth_fixing_team_salary = sum([self.team_salaries_per_minute[role]
                                                       for role
                                                       in PROFIT_ACTIVITIES["Technical Depth Fixing"]["roles"]])

    def __init_regular_meetings_involvement_team_cost(self):
        for name, details in REGULAR_MEETINGS.items():
            self.regular_meetings_involvement_team_salary[name] = 0
            for role in details["roles"]:
                self.regular_meetings_involvement_team_salary[name] += self.team_salaries_per_minute[role] \
                                                                       * details["time"] \
                                                                       * details['count per iteration']

    def __init_release_team_cost(self):
        self.release_team_salary = sum([self.team_salaries_per_minute[role]
                                        for role
                                        in RELEASE_INVOLMENT_ROLES])

    def __init_trouble_shooting_team_cost(self):
        for trouble, descr in TROUBLES.items():
            for role in descr["time to find out root cause"]["roles"]:
                self.trouble_shooting_team_salary[trouble] = self.team_salaries_per_minute[role]\
                                                             * int(descr["time to find out root cause"]["time"])
            for role in descr["time to recover"]["roles"]:
                self.trouble_shooting_team_salary[trouble] += self.team_salaries_per_minute[role] \
                                                             * int(descr["time to recover"]["time"])
