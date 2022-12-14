# Flask Twitter
## A minimal flask Twitter tweet display app built using chatGPT.

This entire app was written using [chatGPT by OpenAI](https://openai.com/blog/chatgpt/) with minimal interference.
The LLM generated the code for the python, css, and html files that enabled a functional flask app within minutes. 

Here's how that journey happened:

### Step 1: Creating flask python app file.
![chatGPT creating the python code](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/create-py.PNG)\
A simple prompt was enough to create a functional app in terms of the backend. Now we have the code for our app file, but what should the file be called?

![chatGPT naming my python file](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/filename-question.PNG)\
This may be a basic question, but it is interesting that it gave me semantically meaningful file names in relation to my project too. In the end, I named it app.py just because that is a flask convention and makes it easy to test in a development environment, but that was my own choice.

The backend logic is great. However, the user needs a frontend in order to interact with it.
Interestingly, it mentions in the code an 'index.html' file. I wondered if it could follow my logic flow and create that.

### Step 2: Creating the html file.
![chatGPT creating the html code](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/create-html.PNG)\
Amazingly, chatGPT understood that the html file I wanted was in reference to the flask app above. It even correctly used the Jinja2 code that flask requires, and explained its own logic back to me which is a great learning tool. I added some minor elements to redirect back to the github page to learn more.

### Step 3: Give it some style.
```
body {
    font-family: 'Helvetica Neue', sans-serif;
    background-color: #1DA1F2;
    color: #ffffff;
}

h1, h2 {
    text-align: center;
    color: #ffffff;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 10px;
}

label, input[type="text"], input[type="submit"] {
    display: block;
    width: 100%;
    margin-bottom: 10px;
    /* This needed to be manually added so the text could be visible. */
    color:black;
}

input[type="text"] {
    padding: 10px;
    font-size: 16px;
    border: none;
    border-bottom: 2px solid #1DA1F2;
}

input[type="submit"] {
    padding: 10px;
    font-size: 16px;
    background-color: #1DA1F2;
    color: #ffffff;
    border: none;
    cursor: pointer;
}

ul {
    margin: 0;
    padding: 0;
}

li {
    list-style: none;
    margin-bottom: 10px;
    padding: 10px;
    background-color: #ffffff;
    border-radius: 10px;
    /* This needed to be manually added so the text could be visible. */
    color:black;
}
```

chatGPT was able to create css code that correctly referenced our html code, and styled it based on my request for a twitter-like theme. It correctly used the right colors, although it is a bit bright for my eyes. I could probably ask for a dark mode alteration, but I felt it was fine for a simple prototype. The only minor edits I needed to make were some text colors to make it visible against the white background.

*Note: chatGPT started having network errors around this time. I was able to copy the code before it gave the error. It seems to error out at the end of the output which is strange. Considering this is a research prototype and is free, it is understandable.*

### Getting our credentials.
![chatGPT telling me how to get Twitter developer credentials](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/find-twitter-credentials.PNG)\
In the python code, it mentioned api keys. I wondered if chatGPT knew what those were. It did, and told me how to get them.

### Hiding our api keys.
![chatGPT telling me how to hide my api keys using an env file](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/env-api.PNG)\
You shouldn't directly share your api keys, so it is good practice to hide them in hidden environment variables. I already knew what to ask for, but it is still impressive that chatGPT provided me relevant instructions on how to create an .env file and then import those variables into the python file.

*Note: I have hidden that .env file from git so it isn't uploaded. Feel free to create your own .env file with your own credentials to try it out.*

### How do we run this thing?
![chatGPT telling me how to run a flask file](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/how-to-run-flask.PNG)\
I am a bit rusty on using flask, so I asked chatGPT how to run my program. It helped me install flask and then run my app. 

*Note: I ended up naming my file app.py, and the above code actually gives an error on Windows by default due to PATH issues. Interestingly, chatGPT was able to troubleshoot that as well, but you may not have that issue. I ended up running simply python -m run*

### We have an app!
![chatGPT telling me how to run a flask file](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/tweet-display-app.PNG)\
We have a fully functional app in less than 30 minutes. Granted, the app is very simple and could possibly be coded manually even faster, but I still believe it is an incredible tool to help developers create prototypes quickly. In the end, this is a tool that is not even fully designed as a coding tool, yet I feel the chatbot nature is almost more helpful than tools like copilot. I believe the friendly dialogue nature of chatGPT combined with the incredible LLM behind it to be the true innovation here, and I have high hopes for the future.

### Network Errors
![chatGPT telling me how to run a flask file](https://raw.githubusercontent.com/Jmete/flask-twitter/main/chatgpt-pictures/network-error.PNG)\
I ended up getting rate-limited extremely quickly which was a bit frustrating. However, as a research prototype being used all over the world, these issues are understandable. I found some help online where you can edit and save a previous prompt which sometimes gets the system to work again. I hope in the future that these issues are resolved, and I am curious on the potential for local deployments of such a system which could potentially help reduce latency or processing costs.

## Learn more
If you would like to contact me to learn more, feel free to reach out at [jamesmete.com](jamesmete.com)

