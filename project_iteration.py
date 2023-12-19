"""
This file is part of Project Simulator.
Project Simulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Project Simulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from config import *
import random

class ProjectIteration():
	def __init__(self, team, iteration_number):
		self.iteration_number = iteration_number
		self.team = team
		self.time_spent_on_meetings = 0
		self.meetings_at_iteretion = []
		self.salary_spent_on_meetings = 0
		self.time_spent_on_troubleshooting = 0
		self.down_time_due_to_troubles = 0
		self.troubles_at_iteration = []
		self.salary_spent_on_troubleshooting = 0
		self.time_spent_on_release = 0
		self.down_time_due_to_release = 0
		self.salary_spent_on_release = 0

	def __play_meetings(self):
		for name, details in REGULAR_MEETINGS.items():
			if self.iteration_number > 0 and self.iteration_number % details["cadence"] == 0:
				print(name)
				self.salary_spent_on_meetings += self.team.regular_meetings_involvement_team_salary[name]
				self.meetings_at_iteretion.append(name)
				self.time_spent_on_meetings += details["time"]
				
	def __play_troubles(self):
		for trouble,descr in TROUBLES.items():
			if float(descr["probability"]) > random.uniform(0, 1):
				self.troubles_at_iteration.append(trouble)
				self.time_spent_on_troubleshooting += int(descr["time to find out root cause"]["time"])
				self.time_spent_on_troubleshooting += int(descr["time to recover"]["time"])
				self.down_time_due_to_troubles += int(descr["time to find out root cause"]["time"])
				self.down_time_due_to_troubles += int(descr["time to recover"]["time"])
				self.salary_spent_on_troubleshooting += self.team.trouble_shooting_team_salary[trouble]

	def __play_release(self):
		if self.iteration_number > 0 and self.iteration_number % RELEASE_CADENCE_IN_ITERATIONS == 0:
			self.time_spent_on_release = RELEASE_TIME_IN_MINUTES
			self.down_time_due_to_release = RELEASE_DOWN_TIME_IN_MINUTES
			self.salary_spent_on_release = self.team.release_team_salary * RELEASE_TIME_IN_MINUTES

	def downtime(self):
		return self.down_time_due_to_release + self.down_time_due_to_troubles

	def downtime_cost(self):
		return self.downtime() * DOWN_TIME_COST_IN_MINUTES

	def time_spent_on_non_profit_activities(self):
		return self.time_spent_on_meetings + self.time_spent_on_troubleshooting + self.time_spent_on_release

	def time_spent_on_profit_activities(self):
		return ITERATION_IN_MINUTES - self.time_spent_on_non_profit_activities()

	def time_spent_on_working_with_feature(self):
		return self.time_spent_on_profit_activities() * PROFIT_ACTIVITIES['Feature']['quota']

	def time_spent_on_defect_fixing(self):
		return self.time_spent_on_profit_activities() * PROFIT_ACTIVITIES['Defect Fixing']['quota']

	def time_spent_on_technical_depth_fixing(self):
		return self.time_spent_on_profit_activities() * PROFIT_ACTIVITIES['Technical Depth Fixing']['quota']

	def salary_spent_on_non_profit_activities(self):
		return self.salary_spent_on_meetings + self.salary_spent_on_troubleshooting + self.salary_spent_on_release

	def salary_spent_on_working_with_feature(self):
		return self.team.working_with_feature_team_salary * self.time_spent_on_working_with_feature()

	def salary_spent_on_defect_fixing(self):
		return self.team.defect_fixing_team_salary * self.time_spent_on_defect_fixing()

	def salary_spent_on_technical_depth_fixing(self):
		return self.team.technical_depth_fixing_team_salary * self.time_spent_on_technical_depth_fixing()

	def salary_spent_on_profit_activities(self):
		return self.salary_spent_on_working_with_feature() + self.salary_spent_on_defect_fixing() + self.salary_spent_on_technical_depth_fixing()

	def total_cost(self):
		return self.salary_spent_on_profit_activities() + self.salary_spent_on_non_profit_activities() + self.downtime_cost()

	def play(self):
		self.__play_meetings()
		self.__play_troubles()
		self.__play_release()