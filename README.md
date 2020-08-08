[//]: # (Implicit Links Within Project)

[1]: https://docs.google.com/spreadsheets/d/1C1NilfOavO-xX1UOnmB7djAXTZ_X5EZ-cNiQfMzb8rI/edit?usp=sharing   "Risk Assessment"
[2]: https://docs.google.com/presentation/d/1BL5r35I7me4MSkJispzxlc57zhBZT7YtfSIj4wbV7tA/edit?usp=sharing   "Presentation"
[3]: https://team-1579095236068.atlassian.net/jira/your-work   "JIRA Project"
[4]: https://www.bma.org.uk/advice-and-support/nhs-delivery-and-workforce/workforce/mental-health-workforce-report   "mental health workforce report"


# MiWell

😀 🙂 😶 😕 😔 😢 😡

**A _smarter_ tool for tracking patient mental health.**

_Created for QA Consulting by Joshua Higginson_


![GitHub](https://img.shields.io/github/license/joshuahigginson1/DevOps_Assessment_1?style=flat-square)
![Coffee](https://img.shields.io/badge/Coffee%20Consumed-%E2%98%95%20%2029%20Cups%20%20%E2%98%95-yellow?style=flat-square)

Add more badges here.


## Contents

- [Project Brief](#project-brief)
  - [Resources](#resources)
  - [Requirements](#requirements)
- [Project Approach](#project-approach)
- [Project Architecture](#project-architecture)
  - [Database Structure](#database-structure)
  - [CI Pipeline](#ci-pipeline)
  - [Front End Development](#front-end-development)
- [Testing](#testing)
 - [Unit Testing](#unit-testing)
 - [Functional Testing](#functional-testing)
- [Project Management](#project-management)
- [Project Review](#project-review)
  - [Risk Assessment](#risk-assessment)
  - [Known Issues](#known-issues)
  - [Future Optimisation](#future-optimisation)
- [Authors](#authors)




## Project Brief

Workforce shortages in mental health are affecting the ability for staff to provide good quality of care.

### Resources

- View my full risk assessment document [here.][1]
- View my project presentation [here.][2]
- View my JIRA Project [here.][3]

### Requirements

## Project Approach

## Project Architecture

### Database Structure







#### Dynamically assigning patients with a new psychiatrist. 

After updating the relationships within my tables, my next task was to dynamically assign a psychiatrist to our patients upon registration.
I thought that the best way of doing this would be to perform an outer join on the psychiatrist and patient tables.

In theory, I could then use the aggregate function COUNT() in order to calculate each psychiatrist's workload.

**Note: In _theory_. The following code did not make it's way into the final project.**

We assign the patient with the psychiatrist with the _least number of other patients_ assigned to them.

` SELECT psy.bacp_number, COUNT(pat.username) `  
` FROM psychiatrist psy `  
` LEFT OUTER JOIN patient pat `  
` ON psy.bacp_number=pat.psychiatrist_id `  
` GROUP_BY psy.bacp_number; `

**Unfortunately for us,** when we convert this code into SQLAlchemy syntax, we omit all 'null entries' within our join table.

`psych_on_patients_join = db.session.query(Psychiatrist.bacp_number, func.count(Patient.username)).outerjoin(Psychiatrist, Psychiatrist.bacp_number == Patient.psychiatrist_id).group_by(Psychiatrist.bacp_number).first()`

`(chosen_psychiatrist, patient_count) = psych_on_patients_join`

This code would not include any of the psychiatrists with no previously assigned patients, aka, a ‘_null_ result’.

##### The Fix

My chosen fix for this issue was to ‘unpack’ a larger subset of our SQLAlchemy table into a _Python dictionary_.

Once I had the data within python itself, it became far easier for me to manipulate the code with functions in Python.







### CI Pipeline

### Front End Development

## Testing




### Unit Testing







### Functional Testing





#### My approach to functional testing.
After an afternoon of research into functional testing, I finally decided to settle on the use of a **Page-Object Model** approach to unit testing.

>> The Page-Object model is one of many approaches to structuring test code.
>> Each page of our web application is associated with it's own **'page class'.**
>> 'Page classes' contain a reference to every _functional_ element of code as a **'elements'.**
>> Our tests can then utilise the methods of this page object class whenever they need to simulate interaction with the UI.

I chose this approach for a few specific reasons:
1. My application code is already organised into blueprints. It makes sense that my test elements are organised in a similar way.

2. If I were to add a UI to my app later down the line, I wouldn't have to rewrite every test. Only change the way in which the 'page class' references the UI.

3. I hate having to repeat code.


### Issues with Flask-Testing.

_This section of the documentation covers my experience with the Flask-Testing module, why I ultimately chose to scrap the LiveServerTestCase class, and how I designed my own multi-threaded test framework._

Test_client() is a _lightweight browser emulation_ that comes prebuilt into flask. This makes it easier for developers to test their programs without having to write their own.
However, this client cannot _fully_ emulate the environment of an application running within a browser.

There are a number of things that it will **not** do. The test_client() browser cannot execute JavaScript code, which makes it impossible to fully test an interactive UI. 
Any code that is included within a http response will be returned without having been executed.

For this project, I wanted to ensure that my functional tests were running in a ‘true-to-life' production environment.

This is why I chose to run my functional tests on a use a real web browser, hat is connected to our application, running on a real web server. 

### UI Testing with Selenium.

Selenium is a web browser automation tool that supports the most popular web browsers, across Windows, MacOS and Linux.

>> Permission to name this testing framework the “Mi-Guel” test framework.
>> I found my solution after reading Miguel Grinberg’s Flask Web Development (2nd edition). 

Selenium requires a 'web driver' to run tests within a web browser.

>> Additional credit goes to the ‘GOAT’: TDD with Python (2nd edition), written by Harry J.W. Percival.









## Project Management

## Project Review


## Risk Assessment

### Known Issues

### Future Optimisation

CSS styling.

## Authors

**Josh Higginson** - _Junior DevOps Consultant for QA Consulting._

