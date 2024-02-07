Requirements Specification
Goal

The goal of the project is to design and implement client-
server solution containing:

• details about professional interests of individual
• allowing viewers to provide feedback about the
content
• asking users to fill additional survey to collect
additional data
Use Cases
UC1: User should be able to access the Web page with
content about professional interests of individual
UC2: User should be able to fill feedback form and submit
feedback
UC3: User should be able to see feedbacks of other users
UC4: As part of feedback user selects its current phase of
education (student or bachelor) and, based on it, is
requested to complete additional survey
System requirements
SR1: Web page should be designed according to template
in Appendix 1 in HTML format using CSS for styling and
JavaScript for supporting dynamic functionality
SR2: Backend should be developed using Node.js with
JavaScript or Flask with Python frameworks
SR3: Client-server interaction should be implemented via
REST API defined as
HTTP method & URL Parame
ters

Descrip
tion

GET https://my-json-
server.typicode.com/depth0/survey

1/surveys

NA Returns
collecti
on of
availabl
e
surveys

https://my-json-
server.typicode.com/depth0/survey

1/surveys/[id]

[id]
identifie
d of
specific
survey

Returns
JSON
objects
with
data of

model
of
specific
surveys

https://my-json-
server.typicode.com/depth0/survey

1/questions

NA Returns
collecti
on of
availabl
e
questio
ns

https://my-json-
server.typicode.com/depth0/survey

1/questions/[id]

[id]
identifie
d of
specific
survey

Returns
JSON
objects
with
data of
model
of
specific
questio
ns





How to run the djangpo application.

To run the web application, navigate to the project(base) directory and type: python manage.py runserver
Then use the local url to access the web application. 
The API links are as follows: http://127.0.0.1:8000/api/surveys/  and  http://127.0.0.1:8000/api/surveys/id/
 http://127.0.0.1:8000/api/questions/ and  http://127.0.0.1:8000/api/questions/id/