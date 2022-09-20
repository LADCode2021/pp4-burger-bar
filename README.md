# PP4 - Burger Bar (Booking app)

Booking is an app designed to make booking a table, changing a book and cancelling a booking at a burger bar easier and more intuitive. The inspiration is taken from a local burger restaurant who on their website asks guests to message them on Whatsapp to book a table. They then manually reply to confirm if they have a table at that time and date. If the guest needs to change their booking, add more people to their booking, add special requests or cancel their booking, then again they have to get in contact via WhatsApp and wait for a manual reply.

Booking achieves the project goal by providing booking page based on principles of design thinking. I empathised with the user by putting myself in their position and anticipated what I think could improve the booking process. I asked myself what would could the site do that would improve the booking process and encourage users to return to the site and therefore the burger bar. I then examined what I would want to see to make me book and return to book again. This process formed my problem statement: "How do I develop a booking application that provides this functionality to the user?"


In terms of functionality users can make a booking (create element of CRUD), see their booking (read element of CRUD), edit their booking (update element of CRUD) or cancel a booking (delete element of CRUD). They must create/login into an account as initial authorisation step for defensive programming reasons and for GDPR reasons so only that person can access their bookings. The app is deployed on Heroku and uses postgresql as its backend database. Other frameworks and packages were used to deliver this app and are detailed towards the end.

[The live project can be viewed here.](https://pp4-burger-bar.herokuapp.com/)

![](docs/images/ismysiteresponsive_screenshot.png)

# Planning

Following my empathise, questions and examine initial step I started mapping out what I felt was the minimum viable product in agile methodology out the requirements I'd identified in a flow diagram using [Lucid Charts](https://www.lucidchart.com/pages/). This allowed me to fully scope what I needed the tool to do and was useful to refer back to, to ensure I was staying on track with the intended minimum outputs for the project.

Please see my original plan below:

![](docs/images/lucid-planning-diagram.jpeg)

I then created a GitHub repository for my app and created a project. Once I'd created the project I setup user stories using automation which automatically added via a template user stories I created to my todo list in the project. I did this so I could track the progress of the functionality I had identified was required for this app.

Please see my initial user stories:

![](docs/images/github-projects-todo-list.png)


I largely stuck to the plan except I decided to update the worksheet all in one API call as the final task, rather than on two separate calls to updated sales first and then the pay calculations later. I read that it is best served to have as few API calls as possible in an application to keep loading/run-time as quick as possible.

Upon failing the initial submission of this project I then added new functionality. The assessor felt that if the user cannot access data in the Googlesheet and if they have to access the Googlesheet to obtain dealer id's then it renders the calculator less useful than just using the Googlesheet. To address this feedback I added functionality to allow the user to access previous sales data. I have changed the the programme so it displays a list of dealer id's in the programme before the user has to choose which dealer. The user should now not need to access the Googlesheet directly for any data input or retrieval.

# How to use Booking app


# Features

## Existing Features

## Future Features

# Technologies used

* Google Chrome
* GitHub
* GitPod
* Heroku

# Custom Models

# Testing

## Bugs

## Remaining Bugs

## Validator Testing

I validated the code in PEP8 and no errors were returned:

# Deployment

# Technologies Used

I used the following technologies:

* Hardware: MacBook Pro
* GitHub
* GitPod
* Google Chrome, Firefox and Safari web browsers
* Django
* Heroku

# Credits

* Code Institute lesson content adapted in some areas - inline comments in code show where.










