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
![Coffee](https://img.shields.io/badge/Coffee%20Consumed-%E2%98%95%20%2034%20Cups%20%20%E2%98%95-yellow?style=flat-square)

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
  - [Known Issues](#known-issues)
  - [Future Optimisation](#future-optimisation)
- [Authors](#authors)

## Project Brief

Workforce shortages in mental health are affecting the ability for staff to provide good quality of care.

The client is a mental health charity, who want a simple and streamlined way to monitor the progress of individuals at risk of relapse.

Unfortunately, the patient to psychiatrist number is exceedingly high, and the client needs an easy way for the referees to keep track of mood, and automatically select the best course of treatment for individuals.

A previously commissioned app was incredibly bulky, and as a result, patients often fall off and lose interest in updating their mood.

> Individuals log into the app, and every day, mark their mood from a selection of values.

> This COULD be done through pressing a button on screen to mark their mood, using emojis, with text underneath for autistic individuals.

> They must also be able to provide a short ‘twitter message’ style update.

> They could be also be able to select how many minutes of mindfulness practice they have achieved on a sliding scale.

> A client is then given a semi-personalised task for helping to improve or maintain their mood.

---

> A referee can log into the app, and see the progress of their patients.

> The referee should be able to leave a short, personalised reply.

> If a patient is ‘at risk’, the referee is notified immediately, and provided with the offending comment, as well as personal contact details.

---

> Referees should be able to log on and add new mindfulness tasks to an existing database.

> Both Patients and referees should be able to edit the response, if something bad happens in the day and needs immediate attention.

---

> There could be push or email notifications sent to the patient if they have forgotten to provide feedback that day.

> Perhaps a patient can track their mood over time with a graphical interface.

> The app could provide different motivating messages each day, so that the user won’t get bored.


### Resources

- View my full risk assessment document [here.][1]
- View my project presentation [here.][2]
- View my JIRA Project [here.][3]

## Project Approach

 I tackled this project from a 'top down' perspective. First envisioning a working application, and designing an application 'skeleton' around this. 
 The main tool I used to achieve this was through the use of templating and blueprints within Flask. This approach was inspired by Todd Birchard of Hackers&Slackers.
 
My project in it's current state (10th August 2020) satisfies _some_ QA assessment criteria. Areas marked with a ~~strikethrough~~ indicate tasks in which I must still complete.

- Create both psychiatrist and patient account accounts, which hold a relationship. (C).
- Patients are automatically assigned to psychiatrists on registration.
- If there are no psychiatrists in the system, a patient cannot register.
- There cannot be two accounts with the same email in the **database** (not just one table.)

- Our users can read data on, update, and delete their accounts. (RUD).

- Create a patient 'mood tracking' page, which allows users to enter an update a unique mood every day. (C)
- ~~Our patient can view, track, update, and delete their previous moods.~~

- The web app automatically flags a patient as 'requires assistance' if a low mood has been entered today.
- Our psychiatrists can view the information of patients who require assistance.
- ~~On a separate page, psychiatrists can see a list of posts that they haven't currently reviewed.~~
- ~~Psychiatrists can comment on user moods.~~ (Framework is in place, however functionality was a lot more difficult than first envisioned.)

Although full CRUD functionality has not yet been implemented, I really have been working hard at this project:

- User authentication.
- Favicons change depending on which user is currently logged in.
- Custom error handling.
- Meticulous attention to detail in bug fixes.
- A custom test server layout for Flask apps running on an application factory model.
- The start of a Page Oriented Model approach to functional testing.
- Nginx acting as reverse-proxy so that our app can be accessed by a domain name: www.miwellness.co.uk
- An automated risk assessment spreadsheet that adheres to industry standard automated tolerance levels. _With dynamic colours._ 

## Project Management

Spoilers: I've never built an application before. 

###### _"...They'll probably mention that again in this readme."_

When I first found out the project specification from QA, I knew that I would have to structure the creation of my app around the learning of said new technologies.
My JIRA project roadmap was created in a manner which replicates and corresponds with my first 6 weeks of study at QA.

In my JIRA settings, I configured additional support for bug tracking, issue tracking, and user stories. In a production environment, new features are normally implemented through user stories.
I made some attempts to work with user stories, but I found this way of thinking rather alien to me without a functioning app, and without actual clients to test.

Every time I've shown my web app to F&F, the first thing they mention is that it looks like something out of 1990. 
Of course in reality, the very first thing I would do is strap a bootstrap template on my project - A true user story.
However in the context of this QA assessment with set project parameters and a strict mark scheme, I mostly chose to structure my backlog around _issues_.

As a developer who favours theory and ideas, before I can truly justify implementing a new feature into my project, I have to truly understand it first.
Not really knowing that much at all about app development however, meant that my story point estimates have been _rather diabolical_.

To aid myself in this process, one incredibly useful implementation to my project management workflow was the introduction of MoSCoW analysis. 
Although perhaps not a great indicator of **time spent,** from a more abstract view of planning poker T-shirt sizes in order to gauge the complexity of a project.

I wanted to keep both _security_ and _file structure_ in high focus. Particularly as I knew that I would be deploying my app to a live production environment.

I made sure that all of my admin passwords were strong, and stored in a password manager. I used linux environment variables, and eventually a .env file to store secret information required for my app to function.

After just a few days of coding the registration functionality, my app was already turning into spaghetti code. If I hadn't organised my code into snippets and blueprints, it would have became a monolithic beast.

## Project Architecture

One of the things I have enjoyed most about my time at QA so far has been learning about databases and database structure. I am already confident in the use of DDL to model database schema.
When I was first introduced to SQL, I couldn't quite grasp the concept of ORM. Now, I'm living my best life, creating complicated SQLAlchemy queries, and enjoy the process of database modelling, updates, and queries.

### Database Structure







#### Dynamically assigning patients with a new psychiatrist. 

After learning about SQLAlchemy's db.relationship() module and tearing up my original database design, my next task was to _dynamically assign_ a psychiatrist to any new patients upon registration.

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

Alas, now is the time I put my hands up and admit, on 10th August 2020, I currently have **0% CODE COVERAGE.**


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


## Project Review

### Known Issues

### Future Optimisation

There are many, many more  of 

CSS styling.

## Authors

**Josh Higginson** - _Junior DevOps Consultant for QA Consulting._

