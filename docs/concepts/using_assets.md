# Using assets
To include an asset in your `kotway` app, you need to have an assets folder and place that asset inside it.

By default, `kotway` will look for a folder named "assets/" in your project dir as the default assets path.

To have a custom assets path, you can pass an asset to the `assets_path` kwarg of `App`.

For example:
```python
kotway.App(main, assets_path="my/custom/assets").run()
```

## Static web app
If you built your `kotway` app as a static web app, the builder tool will copy the content of the folder named "assets/" if exists, and place the content inside the built web app's assets folder (so inside the "dist/assets/" folder).