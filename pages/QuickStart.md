# Quick Start

Here's how you can pull this repo and run the site on your local machine. There you can modify the code and produce a pull request (PR). If approved, it will be deployed to the [production site](https://phoenixcodingacademy.pythonanywhere.com) where everyone can see it

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
* Open `http://127.0.0.1:5000` in your browser to see the site running.
* You can open the repo in Visual Code to make changes.