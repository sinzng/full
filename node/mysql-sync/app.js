
var mysql = require('sync-mysql');
const env = require('dotenv').config({ path: "../../.env" });


var connection = new mysql({
    host:process.env.host,
    user:process.env.user,
    port:process.env.port,
    password:process.env.password,
    database:process.env.database
});

let result =  connection.query('select * from st_info');
console.log(result);

// make insert data 
let data = {
    st_id: "202499",
    name: "Shin",
    dept: "Computer"
}

// inserted data's id
let insertId = data.st_id;

// insert query
result = connection.query("insert into st_info values (?, ?, ?)",
    [insertId, data.name, data.dept]);
console.log("Data is inserted~!!");

// select * query for inserted data 
result = connection.query("select * from st_info where st_id=?", [insertId]);
console.log(result);

// update query
result = connection.query("select * from st_info where st_id=?", ["Game", insertId]);
console.log("Data is updated~!!");

// select * query for inserted data 
result = connection.query("select * from st_info where st_id=?", [insertId]);
console.log(result);

// delete query 
result = connection.query("Delete from st_info where st_id=?", [insertId]);
console.log("Data is Delete~!!");

// select * query for inserted data 
result = connection.query("select * from st_info where st_id=?", [insertId]);
console.log(result);
