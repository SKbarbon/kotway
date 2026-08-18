# Write your first app 😎
You don't know how important it is to write a first app. It will unlock a kotway achievement lol.

## Create a new project.
To start, you can either just create a new Python file,

or, which is recommended, create a project folder. You can do that using this command:

```shell
python -m kotway create
```

After you run the command, you will see a folder named "kotway_project"!

Go inside it, and open "main.py".

## Importing
Let's write our first line of code 🦦!!!!

Import `kotway'. Which going to be like:
```python
import kotway
```

## A target
Our kotway app needs an entry, which we call the target.

A target can be a class, or just a function that describes the UI and sets the logic. The app calls it and passes a `Page` instance.

So simply, create a function with page argument:
```python
import kotway

def main (page: kotway.Page):
    pass
```

## Run the app 🏃
Now, to let the app run and uses that target, let's call `App` and tell it: 

"Yo App, could you run `main`?"

```python
import kotway

def main (page: kotway.Page):
    pass

kotway.App(main).run()
```

Run the file. You can do that by:
```shell
python -m kotway run
```

You.. JUST CREATED A WEB APP 🤯!!!

Now, as you can see, the page is showing nothing. Because we didn't tell it anything to show.

## What should the app do?
Let's make an app that shows your name!! As simple as that.

To show a text like a name, we can use the Control named `Text`!

Let's call `Text`, then let's give it your name!
```python
import kotway

def main (page: kotway.Page):
    my_name = kotway.Text("KOT")

kotway.App(main).run()
```

GREAT 😁!!!

BUT the page STILL did not show the Text!

And that is because we still didn't tell the page to show it. After we do that, the app will look like this:
```python
import kotway

def main (page: kotway.Page):
    my_name = kotway.Text("KOT")
    page.add(my_name)

kotway.App(main).run()
```

Now look at you, having a web app with your name!