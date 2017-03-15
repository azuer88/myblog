Title: Setup a django project with webpack+reactjs+npm frontend framework
Date: 2017-02-15 15:22:41 PHT+0800
Category: guide
Slug: setup-a-django-project-with-webpack-reactjs-npm-frontend-framework
Tags: setup,howto,django,webpack,npm,reactjs,project
Authors: Blue Cuenca
Summary: Instructions on setting up a django+webpack+reactjs+npm project


<!-- start here -->
## Create project as usual...  
 
I usually start from [github][1], creating a repository, then clone that repository.

After creating and cloning, create the virtual environment (see [virtualenvwrapper docs][2]) for more info on installing and setting it up.

## Setup development tools


Install NodeJS v6.x [see here][3]


Install global npm modules:


```
sudo npm install -g --upgrade npm 
sudo npm install -g babel
```




Insert the following into package.json, right after the ```"homepage"``` key:

```
  "devDependencies": {
    "babel-core": "^6.9.1",
    "babel-loader": "^6.2.4",
    "babel-preset-react": "^6.5.0",
    "bootstrap": "^3.3.6",
    "bootstrap-loader": "^1.3.0",
    "bootstrap-sass": "^3.3.7",
    "css-loader": "^0.23.1",
    "extract-text-webpack-plugin": "^1.0.1",
    "file-loader": "^0.8.5",
    "less": "^2.7.1",
    "less-loader": "^2.2.3",
    "node-sass": "^3.11.2",
    "postcss-loader": "^0.9.1",
    "raw-loader": "^0.5.1",
    "react": "^15.1.0",
    "react-bootstrap": "^0.29.4",
    "react-dom": "^15.1.0",
    "react-hot-loader": "^1.3.0",
    "react-placeholder": "0.0.1",
    "resolve-url-loader": "^1.6.0",
    "sass-loader": "^4.0.2",
    "style-loader": "^0.13.1",
    "url-loader": "^0.5.7",
    "webpack": "^1.13.1",
    "webpack-bundle-tracker": "0.0.93",
    "webpack-dev-server": "^1.16.2"
  },
  "dependencies": {
    "react-bootstrap": "^0.29.5"
  }
```

then run:

```
npm install
```

## Install Django and webpack for Django

Run:
```
pip install django django-webpack-loader
```

Everything we need is now installed....  it is time to get our hands dirty.


***To be Continued***

[1]: http://www.github.com
[2]: http://virtualenvwrapper.readthedocs.io/en/latest/install.html
[3]: http://askubuntu.com/a/635469/334127
