# How kotway works 🤔
Hmmm, like really, how does it work?

So first:

**kotway sees the client and the app as two different things.**

Let's start with the **app**:
## The app.
The app is where the logic is running. That's it 😌.

It's the part that builds and decides the UI. For example if the app was a person, he will probably be like:

APP 🙎: "Okayy, so, I need the client to show a Text. And that text needs to be green."

Now, who's gonna tell the client what the App wants? It's the adapter!

## The adapter
The adapter is like a bridge 🌉. It connects the App to the Client, and the Client to the App. 

If you're not using or building a custom adapter, then you're not gonna do anything with the adapter, seriously, don't even think about it.

## The client
The client is the part where it shows the interface elements. It doesn't know what the App wants, until we tell it. 

But who's gonna tell it? Yup, the adapter.

So if the client was a person, and he got the earlier App message, he will respond like:

CLIENT 👷: "Alright I got the message. Here is the text. And oh, it is green. Just the way you wanted 😉."

## That's it 😎!
Wow look at you. You know understand correctly how `kotway` works under the hood!