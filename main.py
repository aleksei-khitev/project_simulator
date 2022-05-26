from team import Team
from project import Project
from report import prepare_report
from config import *

def launch_simulations(simulation_count):
    team = Team()
    accumulated_data = {
        "total time spent on working with feature": [],
        "total time spent on defect fixing": [],
        "total time spent on technical depth fixing": [],
        "total time spent on non profit activities": [],
        "total salary spent on non profit activities": [],
        "total salary spent on profit activities": [],
        "total time spent on meetings": [],
        "total salary spent on meetings": [],
        "total time spent on troubleshooting": [],
        "total salary spent on troubleshooting": [],
        "total time spent on release": [],
        "total salary spent on release": [],
        "total down time due to troubles": [],
        "total down time due to release": [],
        "total down time": [],
        "total down time cost": [],
        "total cost": []
    }

    accumulated_troubles = {}
    for trouble in TROUBLES.keys():
        accumulated_troubles[trouble] = []


    for i in range(simulation_count):
        project = Project(team)
        project.play_year()
        accumulated_data["total time spent on working with feature"].append(project.total_time_spent_on_working_with_feature)
        accumulated_data["total time spent on defect fixing"].append(project.total_time_spent_on_defect_fixing)
        accumulated_data["total time spent on technical depth fixing"].append(project.total_time_spent_on_technical_depth_fixing)

        accumulated_data["total time spent on non profit activities"].append(project.total_time_spent_on_non_profit_activities)
        accumulated_data["total salary spent on non profit activities"].append(project.salary_spent_on_non_profit_activities)
        accumulated_data["total salary spent on profit activities"].append(project.salary_spent_on_profit_activities)
        accumulated_data["total time spent on meetings"].append(project.total_time_spent_on_meetings)
        accumulated_data["total salary spent on meetings"].append(project.total_salary_spent_on_meetings)

        accumulated_data["total time spent on troubleshooting"].append(project.total_time_spent_on_troubleshooting)
        accumulated_data["total salary spent on troubleshooting"].append(project.total_salary_spent_on_troubleshooting)

        accumulated_data["total time spent on release"].append(project.total_time_spent_on_release)
        accumulated_data["total salary spent on release"].append(project.total_salary_spent_on_release)

        accumulated_data["total down time due to troubles"].append(project.total_down_time_due_to_troubles)
        accumulated_data["total down time due to release"].append(project.total_down_time_due_to_release)
        accumulated_data["total down time"].append(project.total_downtime)
        accumulated_data["total down time cost"].append(project.total_down_time_cost)

        accumulated_data["total cost"].append(project.total_cost)

        for trouble, count in project.troubles_count.items():
            accumulated_troubles[trouble].append(count)

    average_data = {}
    for key, value in accumulated_data.items():
        average_data[key] = round(sum(value) / len(value), 2)

    average_troubles = {}
    for key, value in accumulated_troubles.items():
        if (value is not None and len(value) > 0):
            average_troubles[key] = round(sum(value) / len(value), 2)
    return average_data, average_troubles

simulation_count = 100
simulation_results = {}

# Init
average_data, average_troubles = launch_simulations(simulation_count)
simulation_results['Base Example'] = {
    "average data": average_data,
    "average troubles": average_troubles
}

# With IT Org
REGULAR_MEETINGS["daily"]["time"] = 15
PROFIT_ACTIVITIES_AT_ITERATION_QUOTAS['Feature'] = 0.6
PROFIT_ACTIVITIES_AT_ITERATION_QUOTAS['Defect Fixing'] = 0.3
average_data, average_troubles = launch_simulations(simulation_count)
simulation_results['With IT Org'] = {
    "average data": average_data,
    "average troubles": average_troubles
}

# With Monitoring
REGULAR_MEETINGS["daily"]["time"] = 25
PROFIT_ACTIVITIES_AT_ITERATION_QUOTAS['Feature'] = 0.4
PROFIT_ACTIVITIES_AT_ITERATION_QUOTAS['Defect Fixing'] = 0.5
TROUBLES["Service errors because of lack of server's disk space"]["probability"] = -1
TROUBLES["Error because of some service down in the chain of invocations"]["time to find out root cause"]["time"] = 0
TROUBLES["Error because of some service down in the chain of invocations"]["time to recover"]["roles"] = [SYSTEM_ENGINEER, QA_ENGINEER]
average_data, average_troubles = launch_simulations(simulation_count)
simulation_results['With Monitoring'] = {
    "average data": average_data,
    "average troubles": average_troubles
}

# All Improvements
REGULAR_MEETINGS["daily"]["time"] = 15
PROFIT_ACTIVITIES_AT_ITERATION_QUOTAS['Feature'] = 0.6
PROFIT_ACTIVITIES_AT_ITERATION_QUOTAS['Defect Fixing'] = 0.3
TROUBLES["Service errors because of lack of server's disk space"]["probability"] = -1
TROUBLES["Error because of some service down in the chain of invocations"]["time to find out root cause"]["time"] = 0
TROUBLES["Error because of some service down in the chain of invocations"]["time to recover"]["roles"] = [SYSTEM_ENGINEER, QA_ENGINEER]
average_data, average_troubles = launch_simulations(simulation_count)
simulation_results['All Improvements'] = {
    "average data": average_data,
    "average troubles": average_troubles
}

report = prepare_report(simulation_results, simulation_count)
f = open("report.md", "w")
f.write(report)
f.close()