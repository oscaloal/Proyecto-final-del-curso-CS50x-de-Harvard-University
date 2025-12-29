# Las Gabias - App Participativa
#### Video Demo:  <https://youtu.be/TsMWIxWBGOQ?si=FPGFz6OSyTwL_UYM>
#### Description:
To explain my project, I need to describe the two reasons that led me to this decision:

	1.	I am a student at the University of Granada, a southern city in Spain. As in any other Western country, Spain is a democracy where we elect our politicians and where we can participate in public life. In recent years, as in many other countries around the world, Spain has experienced a rise in far-right and far-left movements, which polarize people and make the system more difficult to manage.

	2.	During this course, I came to understand the amount of time and knowledge needed to do anything in computer science. Overly ambitious ideas like creating my own game or developing an app were out of the scope for this project, both because of the limited time — it must be done before December 31st — and because of my limited and newly acquired knowledge. For this reason, I decided to spend my time developing a Flask application that could have real impact in the world, and that I could progressively remake as time passes and as my knowledge grows.

These two reasons made me choose this project. The name of the project has two parts: Las Gabias, which is the name of my town; and App Participativa, which means in Spanish “participative app.” The idea of this app is to promote public participation, guidance, and oversight for all the citizens of this town. Through this app, we can support and promote the local economy with the “Eventos” section; we can also communicate to the town’s politicians with changes we believe are most urgent through the “Propuestas” section. We can also stay informed about what is happening with the “Noticias” section. To make this a functional website, we allow people to log in, log out, and register storing the data with SQL. Once registered, anyone can create an event or a proposal, and immediately after being created, it will appear in the “Noticias” or “Eventos” section so everyone can vote and read other people’s ideas.

This project aims to strengthen democratic participation among all citizens of the town — from bakers to teachers and everyone else — so that we can overcome division and integrate into a more cohesive society.

Initially, i thought to write the menu access in the top of the website, but when reading Bootstrap documentation I found out a navbar could be a nice way to approach it, and this was my decision.

I just created a table where I kept the user, ID... but I didn't keep the news created by each user or the dates, for that reason I had to creat several new tables and linked them together through common elements. I really liked the world of databases.

The last thing was the initial image, I used a image of my town, but I didn't really like the desing and the static it was. So, I looked on the internet how to write dinamically changing images.
