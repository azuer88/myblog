---
Title: Setup a django project with webpack+reactjs+npm frontend framework
Date: 2017-02-15 15:22:41 PHT+0800
Category: guide
Slug: setup-a-django-project-with-webpack-reactjs-npm-frontend-framework
Tags: setup,howto,django,webpack,npm,reactjs,project
Authors: Blue Cuenca
Summary: Instructions on setting up a django+webpack+reactjs+npm project
---

<!-- start here -->

 # Create project as usual...

I usually start from [github][1], creating a repository, then clone that repository.

After creating and cloning, create the virtual environment (see [virtualenvwrapper docs][2]) for more info on installing and setting it up.

# Setup development tools

Install NodeJS v6.x [see here][3]

Install global npm modules:

```
sudo npm install -g --upgrade npm
sudo npm install -g babel
```

Insert the following into package.json, right after the `"homepage"` key: _updated to use wepack 2_

```
  "devDependencies": {
    "autoprefixer": "^6.7.6",
    "bootstrap-loader": "^2.0.0-beta.22",
    "bootstrap-sass": "^3.3.7",
    "css-loader": "^0.26.2",
    "fetch-er": "0.0.10",
    "file-loader": "^0.10.1",
    "import-loader": "^1.0.1",
    "imports-loader": "^0.7.1",
    "node-sass": "^4.5.0",
    "raw-loader": "^0.5.1",
    "react": "^15.4.2",
    "react-bootstrap": "^0.30.7",
    "react-bootstrap-alert": "^1.0.7",
    "react-dom": "^15.4.2",
    "react-hot-loader": "^1.3.1",
    "react-placeholder": "0.0.3",
    "resolve-url-loader": "^2.0.2",
    "sass-loader": "^6.0.2",
    "style-loader": "^0.13.2",
    "url-loader": "^0.5.8",
    "webpack": "^2.2.1",
    "webpack-dev-server": "^2.4.1"
  },
  "dependencies": {}
```

then run:

```
npm install
```

# Install Django and webpack for Django

Run:

```
pip install django django-webpack-loader
```

Everything we need is now installed.... it is time to get our hands dirty.

[**_To be Continued_**][4]

[1]: http://www.github.com
[2]: http://virtualenvwrapper.readthedocs.io/en/latest/install.html
[3]: http://askubuntu.com/a/635469/334127
[4]: {filename}setup-a-django-project-with-webpack-reactjs-npm-frontend-framework-part-2.md
