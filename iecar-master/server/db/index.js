// 用于操作数据库
let mysql = require('mysql')

let db = mysql.createPool({
    host: 'localhost',     //数据库IP地址
    user: 'root',          //数据库登录账号
    password: 'root',      //数据库登录密码
    database: 'iecar',       //要操作的数据库
    port: '3306'//端口号
})

module.exports = db
