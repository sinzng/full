const mysql = require('mysql2')

const pool = mysql.createPool ({
    // mysql connection info
    host:"192.168.1.28",
    user:"mysql",
    port:3306,
    password:"1234",
    database:"testdb"

})

const promisPool = pool.promise()

module.exports = promisPool;