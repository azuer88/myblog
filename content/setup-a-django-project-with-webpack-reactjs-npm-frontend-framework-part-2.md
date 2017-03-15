Title: Setup a Django Project with WebPack-ReactJS-NPM Front-End Framework Part 2
Date: 2017-02-16 14:19:07 PHT+0800
Modified: 2017-03-15 09:05:00 PHT+0800
Category: guide
Slug: setup-a-django-project-with-webpack-reactjs-npm-frontend-framework-part-2
Tags: setup,howto,django,webpack,reactjs,npm,project
Authors: Blue Cuenca
Summary: 


<!-- start here -->

In this post, we are going to continue with setting up the environment we created in [this post]({filename}setup-a-django-project-with-webpack-reactjs-npm-frontend-framework.md)


# Setup Django project

Setup a django project, usually done with `django-admin startproject <project_name>`

We need to add a few things to the *settings.py* of our new django project.

First we'll add some path constants.  so add the following after the *BASE_DIR* assignment:

```
# Build paths for webpack and for static settings
DJANGO_DIR = os.path.dirname(os.path.abspath(__FILE__))
PROJECT_NAME = os.path.basename(DJANGO_DIR)
# I usually have django inside src/ so, root is 3 levels from this file
PROJECT_ROOT = os.path.normpath(os.path.join(DJANGO_DIR, "../../../"))
```


Next, we'll add the `webpack_loader` app into the `INSTALLED_APPS`.

```
INSTALLED_APPS = [
      ...

      `webpack_loader',
]
```

Now, we'll setup the configuration for webpack loader...

Append the following to (last part of) settings.py

```
ASSETS_ROOT = os.path.join(PROJECT_ROOT, 'src', 'assets')
BUNDLES_DIR = os.path.join(ASSETS_ROOT, 'bundles', '')  # must end with /
WEBPACK_LOADER = {
    'DEFAULT': {
        CACHE: not DEBUG,
        'BUNDLE_DIR_NAME': BUNDLES_DIR,
        'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'IGNORE': [.+\.hot-upate.js', \.+\.map'],
    }
}
```

Finally, (for the settings.py, at least) we'll change some of the above settings if debug is not enabled (production settings):

```
if not DEBUG:
   BUNDLES_DIR = os.path.join(PROJECT_ROOT, 'src', static', 'bundles', '')
   WEBPACK_LOADER['DEFAULT'].update(
      {
        'BUNDLE_DIR_NAME': BUNDLES_DIR,
        'STATS_FILE': os.path.join(PROJECT_ROOT, 'webpack-stats-prod.json'),
      }
   )
```

