# Website
Set up environment & configrations:


Node will be used as:
(1) Web server

(2) Node web server will render HTML from React component which we write for front end

(3) Node API server:talk to database


For Windows:

1 Install node and npm: download from https://nodejs.org/en/ and run installer. During the installer running, choose the npm install    manager.

2 Test node version: node -v  

  Test npm version: npm -v
 
 
3 In console type : npm init

 Create package.json file to store the general information and dependencies for project

4 Start documenting and insttalling dependencies

(1) main dependencies: the packages our code will use as product

   1.1 create node web server by using Express.js :
   
        npm install --save express
   1.2 create driver for connecting from node to Mongo
   
        npm i -S mongodb
        
   1.3 front end using react and react-dom:
   
        npm i -S react react-dom
        
(2)dev dependencies : only use in local develop environment
 

