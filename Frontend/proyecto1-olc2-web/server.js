const express = require('express');
const app = express();

app.use(express.static('./dist/proyecto1-olc2-web'));

app.get('/*', (req, res) =>
    res.sendFile('index.html', {root: 'dist/proyecto1-olc2-web/'})

);

const port = process.env.PORT || '80';

app.listen(port, () => {
    console.log("Escuchando en el puerto ", port)
});
