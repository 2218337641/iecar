let express = require('express')        //配置对应路由
let router = express.Router()
let user = require('./API/user')

router.get('/user', user.get)

module.exports = router
