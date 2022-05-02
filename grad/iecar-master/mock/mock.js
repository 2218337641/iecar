import Mock from 'mockjs'

// 用于生成随机数据的工具
const Random = Mock.Random
// var arr = []
// function det(obj){
//     if(obj in arr){

//     }
// }
var arr =[  
    {name: '北京',value: ''+474 },{name: '天津',value: ''+137 },  
    // {name: '上海',value: ''+Random.float(0,1000,0,3) },{name: '重庆',value: ''+Random.float(0,1000,0,3) },  
    {name: '上海',value: ''+77 },{name: '重庆',value: ''+467 },  
    {name: '河北',value: ''+317 },{name: '河南',value: ''+787 },  
    {name: '云南',value: ''+291 },{name: '辽宁',value: ''+228 },  
    {name: '黑龙江',value: ''+67 },{name: '湖南',value: ''+274 },  
    {name: '安徽',value: ''+444 },{name: '山东',value: ''+660 },  
    {name: '新疆',value: ''+53 },{name: '江苏',value: ''+859 },  
    {name: '浙江',value: ''+1182 },{name: '江西',value: ''+172 },  
    {name: '湖北',value: ''+443 },{name: '广西',value: ''+360 },  
    {name: '甘肃',value: ''+103 },{name: '山西',value: ''+97 },  
    {name: '内蒙古',value: ''+31 },{name: '陕西',value: ''+432 },  
    {name: '吉林',value: ''+9 },{name: '福建',value: ''+368 },  
    {name: '贵州',value: ''+163 },{name: '广东',value: ''+1883 },  
    {name: '青海',value: ''+0 },{name: '西藏',value: ''+0 },  
    {name: '四川',value: ''+853 },{name: '宁夏',value: ''+23 },  
    {name: '海南',value: ''+50 },{name: '台湾',value: ''+0 },  
    {name: '香港',value: ''+0 },{name: '澳门',value: ''+0 },{name: '南海诸岛',value: ''+0 }
];


// Mock.mock('/data/index', 'get',  options => {
//     let arr = []
//     for(let i = 0;i<34;i++){
//         let template = {
//             name:Random.province(),
//             value:Random.float(0,1000,0,3)
//         }
//         // det(template)
//         arr.push(template)
//     }
//     console.log(arr)
// }) 
Mock.mock('/data/index', 'get', arr)





// import Mock from 'mockjs'

// // 配置拦截ajax的请求时的行为
// Mock.setup({
//     timeout:'200 - 400'
// })

// const vCode = '123456';

// function getVerificatCode (prarms){
//     const prarmsObj = JSON.parse(prarms.body);
//     return Object.assign(prarmsObj,{vCode: vCode})
// }

// function loginFun(prarms){
//     const prarmsObj = JSON.parse(prarms.body);
//     if(prarmsObj.code===vCode){
//         return{code:1,text:'登陆成功'}
//     }else{
//         return {code:2,text:'验证码有误，登录失败'}
//     }
// }

// // Mock.mock(url,post/get,返回的数据)
// Mock.mock('/getVerificatCode','post',getVerificatCode);//获取验证码
// Mock.mock('/login','post',loginFun);//登录

// import Mock from 'mockjs'
// const Random = Mock.Random//一个工具类，用于生成各种随机数据

// let data = []//用于接受生成数据的数组
// let size = [
//     '300x250', '250x250', '240x400', '336x280', 
//   '180x150', '720x300', '468x60', '234x60', 
//   '88x31', '120x90', '120x60', '120x240', 
//   '125x125', '728x90', '160x600', '120x600', 
//   '300x600'
// ]//定义随机值
// let arrl = []
// var obj = {}
// for(let i = 0;i<10;i++){
//     obj[Random.province()] = [Random.float(0,100,0,3),Random.float(0,100,0,3)]
    // obj.key = Random.province()
    // obj.value = [Random.float(0,100,0,3),Random.float(0,100,0,3)]
    // arrl.push(obj)
    // let template = {
    //     // 'Boolean' : Random.boolean,//可生成基本数据类型
    //     // 'Natural' : Random.natural(1,10),//生成1到10之间的自然数
    //     // 'Integer' : Random.integer(1,100),//生成1到100之间的整数
    //     'Float' : Random.float(0,100,0,3),//生成0到100之间的浮点数，小数点后尾数为0到5位
    //     // 'Character' : Random.character(),//生成随机字符串，可加参数定义规则
    //     // 'String' : Random.string(2,10),//生成2到10个字符之间的字符串
    //     // 'Range' : Random.range(0,10,2),//生成一个随机数组
    //     // 'Date' : Random.date(),//生成一个随机日期，可加参数定义日期格式
    //     // 'Image' : Random.image(Random.size,'#02adea','Hello'),//
    //     // 'Color' : Random.color(),//生成一个颜色随机值
    //     // 'Paragraph' : Random.paragraph(2,5),//生成2至5个句子的文本
    //     // 'Name' : Random.name(),//生成姓名
    //     // 'url' : Random.url(),//生成web地址
    //     'Address' : Random.province(),//生成地址
    // }
    // data.push(template)
// }



// Mock.mock('/data/index', 'get', obj) // 根据数据模板生成模拟数据
// Mock.mock('/data/index2', 'post', obj)