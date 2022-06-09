"""
This file is part of Project Simulator.
Project Simulator is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Project Simulator is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
"""
from config import *

FORMAT = "{:,}"

def total_formula(simulation_results):
    result = ""
    for name,details in simulation_results.items():
        result += f"**{name}**<br/>"
        result += f"$$\n{FORMAT.format(round(details['average data']['total time spent on working with feature'] / (60 * 8), 2))}*R_{{f/d}} " \
               f"+ {FORMAT.format(round(details['average data']['total time spent on defect fixing'] / (60 * 8), 2))}*R_{{df/d}} " \
               f"+ {FORMAT.format(round(details['average data']['total time spent on technical depth fixing'] / (60 * 8), 2))}*P_{{tdf/d}} " \
                f"- {FORMAT.format(round(details['average data']['total cost']), 2)} - C_{{others}}\n$$<br/>"
    return result


def abbreviations_description():
    result = "### Abbreviations\n"
    result += "$R_{{f/d}}$ - Average revenue from a day of new feature development<br/>"
    result += "$R_{{df/d}}$ - Average revenue from a day of fixing defects<br/>"
    result += "$R_{{tdf/d}}$ - Average revenue from a day of improving application by fixing tech depth<br/>"
    result += "C_{{others}} - Other costs<br/><br/>"
    result += "**Revenue from new feature development** inreases sales conversion rate, retention and feasibility of price increase<br/>"
    result += "**Revenue from fixing defects** decreases churn rate and reputational losses<br/>"
    result += "**Revenue from fixing tech depth** increases development speed, probability of occurrence of new defects "
    return result

def total_cost_description(simulation_results):
    result = "\n### Cost Description\n"
    result += "#### Total cost"
    result += "\n| Simulation | Value |\n"
    result += "| --- | --- |\n"
    for name, details in simulation_results.items():
        result += f"| {name} | {FORMAT.format(details['average data']['total cost'])} |\n"

    result += "\n#### Total cost contains:\n"
    result += "| Simulation | Total salary spent on<br/>non profit activities | Down time cost | Total salary spent on<br/>profit activities |\n"
    result += "| --- | --- |--- |--- |\n"
    for name, details in simulation_results.items():
        result += f"| {name} |" \
                  f" {FORMAT.format(details['average data']['total salary spent on non profit activities'])} |" \
                  f" {FORMAT.format(details['average data']['total down time cost'])} |" \
                  f" {details['average data']['total salary spent on profit activities']} |\n"

    result += "\n#### Total salary spent on non profit activities contains:\n"
    result += "| Simulation | Total salary spent on meetings | Total salary spent on troubleshooting | Total salary spent on release |\n"
    result += "| --- | --- |--- |--- |\n"
    for name, details in simulation_results.items():
        result += f"| {name} |" \
                  f" {FORMAT.format(details['average data']['total salary spent on meetings'])} |" \
                  f" {FORMAT.format(details['average data']['total salary spent on troubleshooting'])} |" \
                  f" {details['average data']['total salary spent on release']} |\n"

    result += "\n#### Down time contains:\n"
    result += "| Simulation | Downtime because of release (hours) | Downtime because of troubles (hours) |\n"
    result += "| --- | --- |--- |\n"
    for name, details in simulation_results.items():
        result += f"| {name} |" \
                  f" {FORMAT.format(round(details['average data']['total down time due to release'] / 60, 2))} |" \
                  f" {FORMAT.format(round(details['average data']['total down time due to troubles'] / 60, 2))} |\n"
    return result

def total_balance(simulation_results):
    result = f"{total_formula(simulation_results)}\n"
    result += abbreviations_description()
    result += total_cost_description(simulation_results) + "\n"
    return result


def troubles_report(simulation_results):
    result = "| Simulation |"
    for trouble in TROUBLES.keys():
        result += f" {trouble} |"
    result += "\n| --- |"
    for i in range(len(TROUBLES.keys())):
        result += " --- |"
    result += "\n"
    for name,values in simulation_results.items():
        result += f"| {name} |"
        for trouble in TROUBLES.keys():
            if trouble in values["average troubles"]:
                result += f" {values['average troubles'][trouble]} |"
            else:
                result += " 0 |"
        result += "\n"
    return result

def time_spent(simulation_results):
    result = "| Simuation | " \
             "Spent on<br/>working with feature | " \
             "Spent on<br/>working with feature | " \
             "Spent on<br/>technical depth fixing | " \
             "Spent on meetings | " \
             "Spent on troubleshooting | " \
             "Spent on release |\n"
    result += "| --- | --- | --- | --- | --- | --- | --- |\n"
    for name, details in simulation_results.items():
        result += f"| {name} | "
        result += f"{FORMAT.format(details['average data']['total time spent on working with feature'])} |"
        result += f"{FORMAT.format(details['average data']['total time spent on defect fixing'])} |"
        result += f"{FORMAT.format(details['average data']['total time spent on technical depth fixing'])} |"
        result += f"{FORMAT.format(details['average data']['total time spent on meetings'])} |"
        result += f"{FORMAT.format(details['average data']['total time spent on troubleshooting'])} |"
        result += f"{FORMAT.format(details['average data']['total time spent on release'])} |\n"
    return result

def prepare_report(simulation_results, simulation_count):
    report = f"# Simulation Results\n"
    report += f"Simulation count: **{simulation_count}**\n"
    report += f"## Total Profit for Year:\n{total_balance(simulation_results)}"
    report += f"### Troubles in the year:\n{troubles_report(simulation_results)}\n"
    report += f"### Time Spent for Year:\n{time_spent(simulation_results)}"
    return report
