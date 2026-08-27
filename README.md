# kotway
kotway is a framework that allows building web applications in Python only without prior experience in web frontend development.

## Peak 👁️🐽👁️
Let's peak to an example app. It's VERY NOT simple and complex:

```python
import kotway

def main (page: kotway.Page):
    page.add(
        kotway.Text("Hello, kotway!")
    )

kotway.App(main).run()
```
<img width="301" height="218" alt="image" src="https://github.com/user-attachments/assets/e893dd1b-d592-4075-84ff-30065300739a" />

**Confetti 🎊!!!**, You made A WEB APP 🤯!

## Capabilities
Cleans your room, watch movies with you, and--
Wait, opps spoilers ..

### ONLY Python 👻
Yup. Everything else is a ghost. Build EVERYTHING in your web app using JUST Python. No html, no javascript, just our cute python.

### You choose the publishing 🛩️
Kotway supports BOTH server-driven UI and static websites.

You can make your web app runs its logic on your server, while only the UI is running on the client.

But also, you can choose to publish your app as a static website. And YES, it means python running on the browser!!!

### Flexibility and extensibility 💪
kotway is SUPER flexible. You can modify nearly everything inside it!

You can customize web root, the look, stylesheets, add your own controls, access any property..

And since it rely on native web tech, the UI is as fast as the browser.

## Installation 🧑‍🏫
To install `kotway` library, run this on your terminal:

1. Create a virtual environment (optional)
```shell
python -m venv venv
```

2. Install `kotway` using pip
```shell
pip install kotway
```

## Docs 🦆
I love ducks 🦆, but let's talk about docs.

I'm trying my best to cover everything. Until we have a real docs page, all documentation will be here: [CLICK ME, LES GO🐎!](https://github.com/SKbarbon/kotway/tree/main/docs)

## Contribution
The library is still a baby. A lot of features are coming, and if you encounter ANY issue please submit an issue here: [Issues page](https://github.com/SKbarbon/kotway/issues)

Or if you just wanna ask a question or talk about kotway, you can go [Here](https://github.com/SKbarbon/kotway/discussions).

Contributions are welcome. As it is currently a priority to keep growing, we need more `kotway` community packages that allows for more Customization, utility, and bridging to powerful js frameworks.
