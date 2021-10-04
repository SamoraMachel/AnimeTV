# AnimeTV
![Cover Image](./cover.jpg)

This is a flask application used for browsing, searching and watching animes. The application is built on top of AniAPI and Beyonic API

<hr />

### Prequisites 
In order to setup the website you'll first need to install depedancies and setup the .env file
to install all the dependancies. First move into the `src` folder and execute the command
```
pip install -r requirements.txt
```

After a successful installation, create a `.env` file inside the src folder and add in
```txt
BEARER_TOKEN=" <your aniapi token> "

BASE_URL = 'https://api.aniapi.com/v1'

WEBSITE_URL = 'http://localhost:5000/'
```

To get the aniapi token, You'll have to signup to the [AniAPI Website](https://aniapi.com/login/) 

To run the application run :
```
python main.py
```