"""
This file is part of Project Simulator.
Project Simulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Project Simulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from project_iteration import ProjectIteration
from config import *


class Project:
	def __init__(self, team):
		self.team = team
		self.total_time_spent_on_working_with_feature = 0
		self.total_time_spent_on_defect_fixing = 0
		self.total_time_spent_on_technical_depth_fixing = 0
		self.total_time_spent_on_non_profit_activities = 0

		self.total_time_spent_on_meetings = 0
		self.total_salary_spent_on_meetings = 0
		self.total_time_spent_on_troubleshooting = 0
		self.total_salary_spent_on_troubleshooting = 0
		self.total_time_spent_on_release = 0
		self.total_salary_spent_on_release = 0
		self.total_down_time_due_to_troubles = 0
		self.total_down_time_due_to_release = 0

		self.total_cost = 0
		self.troubles_count = {}
		self.salary_spent_on_profit_activities = 0
		self.salary_spent_on_non_profit_activities = 0
		self.total_downtime = 0
		self.total_down_time_cost = 0

	def __append_time_spent_at_iteration(self, project_iteration):
		self.total_time_spent_on_working_with_feature += project_iteration.time_spent_on_working_with_feature()
		self.total_time_spent_on_defect_fixing += project_iteration.time_spent_on_defect_fixing()
		self.total_time_spent_on_technical_depth_fixing += project_iteration.time_spent_on_technical_depth_fixing()
		self.total_time_spent_on_non_profit_activities += project_iteration.time_spent_on_non_profit_activities()

	def __append_troubles(self, project_iteration):
		for trouble in project_iteration.troubles_at_iteration:
			if trouble in self.troubles_count:
				self.troubles_count[trouble] += 1
			else:
				self.troubles_count[trouble] = 1


	def play_year(self):
		for iteration_number in range(round(WORKING_DAYS_IN_SPAIN / ITERATION_IN_WORKING_DAYS)):
			project_iteration = ProjectIteration(self.team, iteration_number)
			project_iteration.play()
			self.total_time_spent_on_meetings += project_iteration.time_spent_on_meetings
			self.total_salary_spent_on_meetings += project_iteration.salary_spent_on_meetings
			self.total_time_spent_on_troubleshooting += project_iteration.time_spent_on_troubleshooting
			self.total_salary_spent_on_troubleshooting += project_iteration.salary_spent_on_troubleshooting
			self.total_time_spent_on_release += project_iteration.time_spent_on_release
			self.total_salary_spent_on_release += project_iteration.salary_spent_on_release
			self.total_down_time_due_to_troubles += project_iteration.down_time_due_to_troubles
			self.total_down_time_due_to_release += project_iteration.down_time_due_to_release

			self.total_cost += project_iteration.total_cost()
			self.salary_spent_on_non_profit_activities += project_iteration.salary_spent_on_non_profit_activities()
			self.salary_spent_on_profit_activities += project_iteration.salary_spent_on_profit_activities()
			self.total_downtime += project_iteration.downtime()
			self.total_down_time_cost += project_iteration.downtime_cost()
			self.__append_time_spent_at_iteration(project_iteration)
			self.__append_troubles(project_iteration)


