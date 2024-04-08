const express = require('express')
const bodyParser = require('body-parser')
const mysql = require('sync-mysql')
const env = require('dotenv').config({ path: "../../.env" });

const app = express()

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))
app.use(express.json())
app.use(express.urlencoded({ extended:true }))

var connection = new mysql({
    host:process.env.host,
    user:process.env.user,
    port:process.env.port,
    password:process.env.password,
    database:process.env.database
});

app.get('/Hello', (req, res) => {
    res.send("Hello World")
});

// select all rows from st_info table
app.get('/select', (req, res) => {
    const result = connection.query("select * from user")
    console.log(result);
    // res.sendStatus(200);
    res.send(result);
});

// select all rows from st_info table
app.get('/selectQuery', (req, res) => {
    const id = req.query.id;
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    res.send(result);

  });

  app.post('/selectQuery', (req, res) => {
    const id = req.body.id;
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    res.send(result);
  });  

app.post('/insert', (req, res) => {
    const { id, pw } = req.body; 
    const result = connection.query("insert into user values(?, ?)", [id, pw]); 
    console.log(result);
    res.redirect('/selectQuery?id=' + req.body.id);
});

app.post('/update', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query('update user set passwd=? where userid=?', [pw, id]);
    console.log(result);
    res.redirect('/selectQuery?id=' + req.body.id);
  });

  app.post('/delete', (req, res) => {
    const id = req.body.id;
    const result = connection.query('delete from user where userid=?', [id]);
    console.log(result);
    res.redirect('/select');
  });

  // login
app.post('/login', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("select * from user where userid=? and passwd=?", [id, pw]);
    if (result.length == 0) {
        res.redirect('error.html')
    }
    if (id == 'admin' || id == 'root') {
        console.log(id + " => Administrator Logined")
        res.redirect("https://tecoble.techcourse.co.kr/static/715b91aab894cf4240578d9b4ec613b8/b9fcf/linux-distribution.png")
    } else {
        console.log(id + " => User Logined")
        res.redirect('error.html')

    }
}); 
// register
app.post('/register', (req, res) => {
    const { id, pw } = req.body;
    const result = connection.query("insert into user values (?, ?)", [id, pw]);
    console.log(result);
    res.redirect('/');
});


module.exports = app; 