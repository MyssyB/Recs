RECS
Patient Records Portal

Team
Meet our dynamic team of skilled software engineers, each specializing in their respective domains:
Praisegod Adesanmi Praisegod - Backend Developer: Praisegod is a Backend Developer and will be handling the database management, data storage and maintaining the server. His experience in developing, designing and maintaining database, servers and deployment makes his role important in completing this project.

Agiande Beulah - Front-End Developer: Beulah’s role will be that of a researcher and creating/maintaining the UI/UX designs and front end requirements. Her experience in graphics designs makes her a fundamental contributor to the project.
Technologies 
Languages: Python, HTML, CSS, Javascript.
Framework: JQuery
Libraries: Flask, Python, 
Hardware: Laptops.
Platform: Container (Docker).
Books: Documentations (as reflected on the References)

JQuery in place of React as a Framework:
JQuery is straightforward, simple to understand and implement. It provides a wide range of functions for DOM manipulation, event handling and animation.  JQuery is lightweight and can be included via CDN by just one line of code. React has a steep learning curve compared to JQuery and it requires learning other concepts like JSX, state management, hooks and component lifecycle alongside it. React also requires mode boilerplate code, especially when setting up a project with additional tools like Webpack, Babel, or Redux. 

Challenge:
This portfolio project is intended to give patients easy access to their health information (medical records and test results), facilitate communication with their healthcare providers, and process payment. 
However, it will not give the patient access to book any form for invasive medical procedure (surgery) or access to view results of scans (x-rays, MRIs, PET or CAT scan).
This project will help patients across all geographical regions and is independent of any specific locale.
Risks:
One of the major risks will be server downtime from the host platform. The alternative is to deploy it on multiple platform and use a load balancer to distribute the network traffic.

The non-technical risk will be securing patient’s confidential and credit card information and the some of the strategy that will be employed to prevent this is the use of payment gateways (e.g. Paystack, flutterwave etc) and using micro services to handle database integration.
Infrastructure
The process for branching will be what we are already used to in team projects where one member of the team will create the github repository, add others as contributors. The contributors will then clone the repo into their local machine, create a branch to work on, then push the branch to origin. 
The deployment strategy that will be used in this project is to containerize using Docker. This is to separate different parts of the projects into micro services: frontend, backend, database and proxy server will be independent of each other.
The data will be gotten from the frontend via user interface. The user will submit their data and it will be sent via https request to the backend which will handle the storage to the database.
Unittest will be used for testing the backend code.

Existing Solutions
CarePlus is health record software used in clinics to book patients appointments with specialists, maintain patients medical information, test results, process medication and bill payment but it is being used by the health professionals and patients have no access to it.
The decision to reimplement this solution is to give patients access to their health information outside of the health facility, access to the results of investigations done and a secure payment platform to settle their medical bills.

