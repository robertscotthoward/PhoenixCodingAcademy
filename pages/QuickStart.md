# Quick Start

Here's how you can pull (or "clone") this repository (or "repo") to your laptop (or desktop) and run the site there. You will need an Internet connection to clone the repo, but after that, you can do evolve the website in airplane mode. There you can modify the code and commit changes to you local cloned repo. Once you get all your changes done and tested, you can (with Internet) produce a pull request (PR) back to the repo for peer review. If approved, it will be deployed to the [production site](https://phoenixcodingacademy.pythonanywhere.com) where everyone can see it.

Steps:

* Find an existing folder somewhere on your; e.g. `C:\mystuff`
* Open a command shell in that folder.
* Run `git clone https://github.com/PhoenixCodingAcademy/PhoenixCodingAcademy.git`
* You should see a new folder called `C:\mystuff\PhoenixCodingAcademy`
* Change to that folder.
* --> Optionally, you can also go to [the Github repo](https://github.com/PhoenixCodingAcademy/PhoenixCodingAcademy) and download the zip file of the entire repo, but you won't have a local repo to which you can commit changes.
* Run `python projects/web/main.py --debug run` or just run the `StartWebServer.bat` there.
* You should see the following:
```
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

* This means the website (or "web server") is running on your machine and being served up on port 5000.
* Open `http://127.0.0.1:5000` in your browser to see the site running.
* You can open the repo in Visual Code to make changes.
* The web server will automatically detect the changes you made and serve them up.
* Hit F5 in your browser to refresh it and see your changes.

See [Git](/subjects/git) to learn how to:

* Clone the repo
* Commit your changes
* Push your changes
* Create a pull request