# Static vs Server-drive.
By default, `kotway` supports two app modes.

1. Server-driven UI App.
2. Static web App.

## Server-driven UI App
What does this weird name even means 😂?

It means that you are the one running the Python app.

So when a user (client) connects to your app, everything python will do is going to happen on your computer/server.

A user clicks a button? The even handler is running on your computer.

This is good for apps that required server-level speeds, or if the developer just doesn't want to expose the app logic.

## Static Web App
A static web app means fixed web files (like html, css, js) are being served to run FULLY on the client browser.

`kotway` provides an easy way to package/build your python app to a web-based static website. Which is possible thanks to web assembly usage through pyodide.

The command for that is:
```shell
python -m kotway build <path/to/app>
```

Which going to create a folder named `dist/` inside the provided path.
The folder will contain your website files.

if you want to quickly run a test, do:
```shell
cd path/to/dist
python -m http.server --directory .
```