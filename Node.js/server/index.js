const express = require('express');
const path = require('path');
const app = express();

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

app.get('/', (req, res) => {
    const filePath = path.join(__dirname, 'index.html');
    res.sendFile(filePath);
});
app.get('/about', (req, res) => {   
    res.send('About page');
});