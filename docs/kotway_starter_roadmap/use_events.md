# Use events
A complete `kotway` app will almost always use events.

`kotway` Supports multiple events. But what we're gonna talk about in this startup roadmap is an event type that is called an `InteractionEvent` (activate nerd mode 🤓).

An interaction event is an event send from the client to the app announcing a user interaction.

## Simple example 👇
A simple example is when the user clicks a button. The client will send an Interaction event to the app saying:

"Hey! The user just clicked a button!"

And the app can do something about it.

## Let's write some code !
Let's build a simple `kotway` app that greets your name when you write it on a `TextField`!

1. First, let's have a simple app target.
```python
import kotway

def main (page: kotway.Page):
    pass

kotway.App(main).run()
```

2. Next, we will create the `Text` which the greeting will be on.
```python
import kotway

def main (page: kotway.Page):
    greeting_text = kotway.Text("")
    page.add(greeting_text)

kotway.App(main).run()
```

3. Let's create our simple `TextField`!
```python
import kotway

def main (page: kotway.Page):
    greeting_text = kotway.Text("")
    page.add(greeting_text)

    username = kotway.TextField()
    page.add(username)

kotway.App(main).run()
```

4. Create a function that can greet a name
```python
import kotway

def main (page: kotway.Page):
    def greet_name (name):
        greeting_text.content = name
        greeting_text.update()

    greeting_text = kotway.Text("")
    page.add(greeting_text)

    username = kotway.TextField()
    page.add(username)

kotway.App(main).run()
```

Notice that when we update the text inside `greet_name`, we call `.update()`. That's how we tell the client to update a control.

Now if we used the function to update the text, like:
```python
import kotway

def main (page: kotway.Page):
    def greet_name (name):
        greeting_text.content = "Greeting " + name
        greeting_text.update()

    greeting_text = kotway.Text("")
    page.add(greeting_text)

    username = kotway.TextField()
    page.add(username)

    # Testing here!
    greet_name("KOT")

kotway.App(main).run()
```

You will notice the text showing the name!

5. Make the greetings happen when a name is typed.

Now, we don't actually want to manually update the name like that 😑. 

So, what we're going to do is to assign that method to an interaction event that happened to be called per new typed character.. Hmmm I wonder what is that...

WAIT, it's `on_input`!!

We can use the `TextField.on_input`, which is an event handler that is called whenever the user is typing something new in the field.

```python
import kotway

def main (page: kotway.Page):
    def greet_name (name):
        greeting_text.content = "Greeting " + name
        greeting_text.update()

    greeting_text = kotway.Text("")
    page.add(greeting_text)

    username = kotway.TextField(
        on_input = greet_name
    )
    page.add(username)

kotway.App(main).run()
```

Now run the app, and write your name 😁.

### OHHHHHHHHH NOOOO 😱!!
You just got an error !!

Are you okay ? Com'n of course you are!

Getting errors is part of the journy 🥰.

So, what happened?

Any interaction event handler, such as `on_input` that was used, gets the event data class as an argument. The data are needed to identify the event internally, but also for you, the class gives you usefull data!

Like, it tells you what exact control does the event relate to? And is there event values we can use to complete the handler job?

Currently, we do need the value of textfield. So we can do something like this:
```python
import kotway

def main (page: kotway.Page):
    def greet_name (e: kotway.InteractionEvent):
        name = e.control.value
        greeting_text.content = "Greeting " + name
        greeting_text.update()

    greeting_text = kotway.Text("")
    page.add(greeting_text)

    username = kotway.TextField(
        on_input = greet_name
    )
    page.add(username)

kotway.App(main).run()
```

## Tada 🪄✨!
You just created a web app that get an event, does handle it, and update the client page based on some logic!