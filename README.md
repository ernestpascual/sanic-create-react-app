# Sanic + Create React 

##Step 1: Make a new create-react-app through the create-react-app cli
```
create-react-app <project name>
```

##Step 2:  Make sure that npm is installed in correctly then Install webpack and webpack cli 
```
npm init
npm install  -D
npm i webpack webpack-cli -D
```

##Step 3: Install Babel dependcies
```
npm i babel-core babel-loader babel-preset-env babel-preset-react -D
```
If you ever encounter an error regarding babel core, install the following dependency.

```
 npm install babel-loader@7 -S
```
##Step 4: Make a .babelrc
```
{
    "presets": ["env", "react"]
  }
```
##Step 5: Create a webpack.config.js file
```
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
```

##Step 6: Install html-webpack-plugin dependency
```
npm i html-webpack-plugin -D
```

##Step 7: Update webpack.config
```
const HtmlWebPackPlugin = require("html-webpack-plugin");

const htmlPlugin = new HtmlWebPackPlugin({
  template: "./public/index.html",
  filename: "./index.html"
});

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },
  plugins: [htmlPlugin]
};
```

##Step 8: Setup webpack-dev-server
```
npm i webpack-dev-server -D
```
Change the your package.json start script to
```
"start": "webpack-dev-server --mode development --open"
```

## Step 9: Setup CSS loader for webpack
Install style loader:

```
npm i css-loader style-loader -D
```


##Step 10: Update your webpack.config:

```
const HtmlWebPackPlugin = require("html-webpack-plugin");

const htmlWebpackPlugin = new HtmlWebPackPlugin({
  template: "./src/index.html",
  filename: "./index.html"
});

module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },
  plugins: [htmlWebpackPlugin]
};
```

## Generate webpack files
```
npm run build
```

## Add Sanic server file
Make sure you have atleast Python 3.5 first!
Save the following as requirements.txt
```
aiohttp==3.4.4
sanic==0.8.1
```
run the following command
```
pip3 install requirements.txt
```

Change your package.json start to:
```
"start": "python3 server.py",
```

Make your server.py file

```
from sanic import Sanic
from sanic.response import json, html, file, text
import aiohttp
import asyncio

# gets current directory
BASE = os.getcwd()

app = Sanic()
app.static('/src', BASE + '/src')

# serve js file for webpack
app.static('/', BASE)
app.static('/main.js', './dist/main.js', name='main.js')

@app.route('/')
async def index(request):
    return await file('./dist/index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8000)),
        workers=int(os.environ.get('WEB_CONCURRENCY', 1)),
        debug=bool(os.environ.get('DEBUG', '')))
```


## RUN IT!
```
npm run start
```

## Credits
https://medium.freecodecamp.org/part-1-react-app-from-scratch-using-webpack-4-562b1d231e75

