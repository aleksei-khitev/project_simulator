"""
This file is part of Project Simulator.
Project Simulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Project Simulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
PROJECT_MANAGER = "Project Manager"
BUSINESS_ANALYST = "Business Analyst"
QA_ENGINEER = "QA Engineer"
SOFTWARE_ENGINEER = "Software Engineers"
SYSTEM_ENGINEER = "System Engineer"

RUBLE_PER_EUR = 74.12
WORKING_DAYS_IN_SPAIN = 250
WORKING_DAYS_IN_RUSSIAN = 247

SALARY_PER_MONTH = {
	PROJECT_MANAGER: 3240,
	BUSINESS_ANALYST: 2640,
	QA_ENGINEER: 2320,
	SOFTWARE_ENGINEER: 107_000 / RUBLE_PER_EUR,
	SYSTEM_ENGINEER: 2280
}

TEAM = {
	PROJECT_MANAGER: 1,
	BUSINESS_ANALYST: 1,
	QA_ENGINEER: 1,
	SOFTWARE_ENGINEER: 4,
	SYSTEM_ENGINEER: 1	
}

TEAM_WORKING_DAYS = {
	PROJECT_MANAGER: WORKING_DAYS_IN_SPAIN,
	BUSINESS_ANALYST: WORKING_DAYS_IN_SPAIN,
	QA_ENGINEER: WORKING_DAYS_IN_SPAIN,
	SOFTWARE_ENGINEER: WORKING_DAYS_IN_RUSSIAN,
	SYSTEM_ENGINEER: WORKING_DAYS_IN_SPAIN
}

ITERATION_IN_WORKING_DAYS = 10
ITERATION_IN_MINUTES = ITERATION_IN_WORKING_DAYS * 8 * 60

REGULAR_MEETINGS = {
	"retro": {
		"cadence": 1,
		"time": 60,
		"count per iteration": 1,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, SYSTEM_ENGINEER, PROJECT_MANAGER]
	},
	"estimation": {
		"cadence": 1,
		"time": 60,
		"count per iteration": 1,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, PROJECT_MANAGER]
	},
	"prioritisation": {
		"cadence": 1,
		"time": 60,
		"count per iteration": 1,
		"roles": [BUSINESS_ANALYST, PROJECT_MANAGER]
	},
	"planning": {
		"cadence": 1,
		"time": 60,
		"count per iteration": 1,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, SYSTEM_ENGINEER, PROJECT_MANAGER]
	},
	"daily": {
		"cadence": WORKING_DAYS_IN_SPAIN,
		"count per iteration": ITERATION_IN_WORKING_DAYS,
		"time": 25,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, SYSTEM_ENGINEER, PROJECT_MANAGER]
	},
	"demo": {
		"cadence": 1,
		"count per iteration": 1,
		"time": 60,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, SYSTEM_ENGINEER, PROJECT_MANAGER]
	},
}

PROFIT_ACTIVITIES = {
	"Feature": {
		"quota": 0.4,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, PROJECT_MANAGER]
	},
	"Defect Fixing": {
		"quota": 0.5,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, BUSINESS_ANALYST, PROJECT_MANAGER]
	},
	"Technical Depth Fixing": {
		"quota": 0.1,
		"roles": [SOFTWARE_ENGINEER, QA_ENGINEER, PROJECT_MANAGER]
	},
}

RELEASE_INVOLMENT_ROLES = [SOFTWARE_ENGINEER, QA_ENGINEER, SYSTEM_ENGINEER, PROJECT_MANAGER]
RELEASE_CADENCE_IN_ITERATIONS = round(WORKING_DAYS_IN_SPAIN / (4 * ITERATION_IN_WORKING_DAYS), 0)
RELEASE_TIME_IN_MINUTES = 16 * 60
RELEASE_DOWN_TIME_IN_MINUTES = 8 * 60

TROUBLES = {
	"Service errors because of lack of server's disk space": {
		"time to find out root cause": {
			"time": 60,
			"roles": [SOFTWARE_ENGINEER, SYSTEM_ENGINEER, QA_ENGINEER, PROJECT_MANAGER]
		},
		"time to recover": {
			"time": 15,
			"roles": [SOFTWARE_ENGINEER, SYSTEM_ENGINEER]
		},
		"probability": 8 / WORKING_DAYS_IN_SPAIN
	},
	"Error because of some service down in the chain of invocations": {
		"time to find out root cause": {
			"time": 15,
			"roles": [SOFTWARE_ENGINEER, SYSTEM_ENGINEER, QA_ENGINEER, PROJECT_MANAGER]
		},
		"time to recover": {
			"time": 10,
			"roles": [SOFTWARE_ENGINEER, SYSTEM_ENGINEER, QA_ENGINEER]
		},
		"probability": 20 / WORKING_DAYS_IN_SPAIN
	}
}
DOWN_TIME_COST_IN_MINUTES = 3.6