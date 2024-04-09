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

function templete_nodata(res) {
    res.writeHead(200);
        var templete =`
        <!DOCTYPE html>
        <head>
            <title>Error</title>
            <meta charset="utf-8" />
            <link type = "text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <h3>데이터가 존재하지 않습니다.</h3>

        </body>
        </html>
    `;
    res.end(templete);
    
}

function templete_result(result, res) {
    res.writeHead(200);
        var templete =`
        <!DOCTYPE html>
        <head>
            <title>Error</title>
            <meta charset="utf-8" />
            <link type = "text/css" rel="stylesheet" href="mystyle.css" />
        </head>
        <body>
            <table border="1" style="margin:auto;">
            <thead>
                <tr><th>User ID</th><th>Password</th></tr>
            </thead>
            <tbody>
            `;
            for(var i=0; i < result.length; i++) {
                templete += `
                    <tr>
                        <td>${result[i]['userid']}</td>
                        <td>${result[i]['passwd']}</td>
                    </tr>
                `; 
            }
            templete += `
            </tbody>
            </table>
        </body>
        </html>
    `;
    res.end(templete);
}

app.get('/Hello', (req, res) => {
    res.send("Hello World")
});

// select all rows from st_info table
app.get('/select', (req, res) => {
    const result = connection.query("select * from user")
    console.log(result);
    // res.sendStatus(200);
    // res.send(result);
    if(result.length==0) {
        templete_nodata(res);
    } else {
        templete_result(result, res);
    }
});

// select all rows from st_info table
app.get('/selectQuery', (req, res) => {
    const id = req.query.id;
    const result = connection.query('select * from user where userid=?', [id]);
    console.log(result);
    // res.send(result);
    if(result.length==0) {
        templete_nodata(res);
    } else {
        templete_result(result, res);
    }

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
    if (id == "") {
        res.redirect("register.html")
    } else {
        let result = connection.query('select * from user where userid=?', [id]);
        if(result.length>0) {
            res.writeHead(200);
            var templete =`
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Error</title>
                    <meta charset="utf-8" />
                </head>
                <body>
                    <div>
                    <h3 style="margin-left: 30px">Register Failed</h3>
                    <h4 style="margin-left: 30px">이미 존재하는 아이디 입니다.</h4>
                    <a href="register.html" style="margin-left:30px">다시 시도하기</a>
                    </div>
                </body>
                </html>
            `;
            res.end(templete);
        } else {
            const result = connection.query("insert into user values (?, ?)", [id, pw]);
            console.log(result);
            res.redirect('/');
        }
    }
});


module.exports = app; 