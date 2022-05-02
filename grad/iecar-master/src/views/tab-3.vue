<template>
  <div class="tab">
      <section ref="chart"></section>
  </div>
</template>

<script>
//主模块

let echarts = require('echarts/lib/echarts')
// 散点图
require('echarts/lib/chart/scatter')
// 散点图放大
require('echarts/lib/chart/effectScatter')
// 地图
require('echarts/lib/chart/map')
// 图例
require('echarts/lib/component/legend')
// 提示框
require('echarts/lib/component/tooltip')
// 地图geo
require('echarts/lib/component/geo')
// 手动引入中国地图js文件
require('echarts/map/js/china')

export default {
    data(){
        return{
            locationCarsList:[],
            // dataList:[{"id": "320000","name": "江苏","value": "95"},
            //     {"id": "340000","name": "安徽","value": "60"},
            //     {"id": "330000","name": "浙江","value": "105"},
            //     {"id": "310000","name": "上海","value": "75"},
            //     {"id": "370000","name": "山东","value": "50"},
            //     {"id": "320100","name": "南京市","value": "21"},
            //     {"id": "320200","name": "无锡市","value": "23"},
            //     {"id": "320300","name": "徐州市","value": "15"},
            //     {"id": "320400","name": "常州市","value": "20"},
            //     {"id": "320500","name": "苏州市","value": "25"},
            //     {"id": "321000","name": "扬州市","value": "15"},
            //     {"id": "321100","name": "镇江市","value": "11"},
            //     {"id": "321200","name": "泰州市","value": "12"},
            //     {"id": "320800","name": "淮安市","value": "6"},
            //     {"id": "320600","name": "南通市","value": "5"},
            //     {"id": "320900","name": "盐城市","value": "4"},
            //     {"id": "320700","name": "连云港市","value": "8"},
            //     {"id": "321300","name": "宿迁市","value": "11"}]
        }
    },
    created(){
        
    },
    mounted(){
        var myChart = echarts.init(this.$refs.chart);
        let showLoadingDefault={
            text:'加载中',
            color:'#23531',
            texyColor:'fff',
            maskColor:'#272D3A',
            zlevel:0
        }
        console.log(this.dataList)
        this.fetchs()
        // console.log(this.locationCarsList)
        myChart.showLoading(showLoadingDefault)
        this.$nextTick(function(){
        //     this.drawLine(myChart);
        this.fetchs(myChart)
        })
        this.$store.commit('openLoading')
        this.$store.dispatch('fetchHeatChinaRealData', myChart)
    },
    methods:{
        drawLine(loo,obj){
            var option = {
                // backgroundColor:'#272D3A',
                // 标题
                title:{
                    text:'省级行政区二手车市场热力图',
                    subtext:'数据来源:汽车之家二手车',
                    left:'center',
                    textStyle:{
                        fontSize:33,
                        color:'#000',
                        fontWeight:'bold'
                    }
                },
                // 提示框
                tooltip:{
                    // 数据项图形触发，在无类目轴的图表中使用
                    trigger:'item',
                    formatter: function (params) {
                    var nameArr = params.seriesName.split(",");
                    if(null!=params.data&&"undefined"!=params.data){
                        if(isNaN(params.value) || ""==params.value || null ==params.value){
                            params.value=0;
                        }
                        return params.name + '<br />' + nameArr[0] + '：' + params.value ;
                    }else{
                        if(isNaN(params.value) || ""==params.value || null ==params.value){
                            params.value=0;
                        }
                        return params.name + '<br />' + nameArr[0] + '：' + params.value;
                    }
                }//数据格式化
                },
                // 视觉映射插件
                visualMap:{
                    show:true,
                    min:0,
                    max:2000,
                    left:'left',
                    top:'top',
                    text:['高','低'],//取值范围的文字
                    // seriesIndex:0,
                    // calculable:true,
                    inRange:{
                        color:['#e0ffff', '#F50900']//取值范围的颜色
                    }
                },
                // 图例按钮
                // legend:{
                //     orient:'vertical',
                //     left:'left',
                //     top:'bottom',
                //     data:['二手车销量'],
                //     textStyle:{
                //         color:'#fff'
                //     }
                // },
                // 地理坐标系组件
                geo:{
                    map:'china',
                    // 视角缩放比例
                    zoom:1.23,
                    label:{
                        // true会直接显示城市名称
                        normal:{
                            show:true,
                            fontSize:'12',
                            color:'#fff'
                        }
                    },
                    // 是否开启鼠标缩放和平移漫游
                    // roam:true,
                    itemStyle:{
                        // 地图背景色
                        normal:{
                            // show:true,
                            areaColor:'#465471',
                            borderColor:'#282F3C',
                        },
                        // 悬浮时
                        emphasis:{
                            areaColor:'#8796B4',//鼠标选择区域颜色
                            shadowOffsetX:0,
                            shadowOffsetY:0,
                            shadowBlur:20,
                            borderWidth:0,
                            shadowColor:'rgba(0,0,0,0.5)'
                        }
                    }
                },
                series:[
                    {
                        name:'数量',
                        type:'map',
                        geoIndex:0,
                        // coordinateSystem:'geo',
                        data:loo,
                        // pointSize:8,
                        // blurSize:5
                    }]
            }
            obj.setOption(option)
            // Chart.setOption(option)
        },
        fetchs(objs){
            var api = '/data/index'
            this.axios.get(api).then((res)=>{
                this.locationCarsList = res.data,
                // console.log('-----------------')
                // console.log(this.locationCarsList)
                this.drawLine(this.locationCarsList,objs)
            }).catch((err)=>{
                console.log(err)
            })
        }
    }
}
</script>

<style lang="less" scoped>
    .tab{
        width: 1580px;
        height: 100%;
    }
    section{
        float: left;
        width: 1580px;
        height: 820px;
        background-color: rgb(217, 234, 236);
    }
</style>