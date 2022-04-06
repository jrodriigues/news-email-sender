## Email sender script

The objective of this script is to retrieve data from an API (News API), format that data and send it on an email, using the Gmail API.


### ** Step by step to execute the program **

- Create an account with the [News API](https://newsapi.org/) and create an API key
- Create a new project in GCD (Google Cloud Platform) and install the Gmail API from the library
- In the GCD, create a OAuth 2.0 credential, download the .json file and paste it in your directory (change the name to client_secret_file.json)
- Create and run a virtual environment, and install the packages directly from the 'requirements.txt'
- Replace the variables that have comment "Flag" - this are user specific variables, like API key
- run 'email_sender.py'


### ** References **

- [Jie Jenn youtube video](https://www.youtube.com/watch?v=44ERDGa9Dr4) for 'support.py' and 'email_sender.py'
