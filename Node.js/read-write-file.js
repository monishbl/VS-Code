const fs = require('fs');
// import {fs} from 'fs';
fs.writeFile('message.txt', 'Hello World! 👋', (err)=> {
    if (err) {
        throw err;
    }
    console.log('File created');
    
});
fs.readFile('message.txt', (err, data) => {
    if (err) {
        throw err;
    }
    console.log(data.toString());
});