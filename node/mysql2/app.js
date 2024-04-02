const { connect } = require("http2");
const mysql = require("mysql2/promise");
const env = require('dotenv').config({ path: "../../.env" });
 

const db = async () => {
    try{ 
        //db connection
        let connection = await mysql.createConnection({

            host: process.env.host,
            user: process.env.user,
            port: process.env.port,
            password: process.env.password,
            database: process.env.database
        })

        //select query
        let [rows, fields] = await connection .query("select * from st_info")
        console.log(rows);

        // make insert data 
        let data = {
            st_id: "202499",
            name: "Shin",
            dept: "Computer"
        }


        
        // inserted data's id
        let insertId = data.st_id;

          // insert query
        [rows, fields] = await connection.query("insert into st_info values (?, ?, ?)",
        [insertId, data.name, data.dept]);
        console.log("\nData is inserted~!!");

          // select * query for inserted data 
        [rows, fields]= await connection.query("select * from st_info where st_id=?", [insertId]);
        console.log(rows);

          // update query
        [rows, fields]= await connection.query("select * from st_info where st_id=?", ["Game", insertId]);
        console.log("\nData is updated~!!");

          // select * query for inserted data 
        [rows, fields]= await connection.query("select * from st_info where st_id=?", insertId);
        console.log(rows);

        // delete query 
        [rows, fields]= await connection.query("Delete from st_info where st_id=?", insertId);
        console.log("\nData is deleted~!!");

          // select * query for inserted data 
        [rows, fields]= await connection.query("select * from st_info");
        console.log(rows);



    } catch (error) {
        console.log(error);
    }
}


db();