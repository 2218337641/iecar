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
        // this.fetchs()
        // console.log(sere)
        myChart.showLoading(showLoadingDefault)
        this.$nextTick(function(){
            this.drawLine(myChart);
        })
        this.$store.commit('openLoading')
        this.$store.dispatch('fetchHeatChinaRealData', myChart)
    },
    methods:{
        // fetchs(){
        //     let _this = this
        //     this.axios.get('/data/index',{
        //         params:{}
        //     }).then(res=>{
        //         console.log(res)
        //     }).catch(err=>{
        //         console.log(err)
        //     })
        // },
        drawLine(Objs){
            var option={
                backgroundColor:'#272D3A',
                // 标题
                title:{
                    text:'中国地图',
                    left:'center',
                    textStyle:{
                        color:'#fff'
                    }
                },
                // 视觉映射插件
                // 设置组件的最大值最小值，且分段数以及在选择范围中的视觉元素定义颜色、尺寸等
                visualMap:{
                    show:true,
                    min:1,
                    max:1000,
                    // splitNumber:5,
                    inRange:{
                        color:['#d994e5b','#eac736','#50a3ba'].reverse()
                    },
                    textStyle:{
                        color:'#fff'
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
                    label:{
                        // true会直接显示城市名称
                        emphasis:{
                            show:true
                        }
                    },
                    itemStyle:{
                        // 地图背景色
                        normal:{
                            areaColor:'#465471',
                            borderColor:'#282F3C'
                        },
                        // 悬浮时
                        emphasis:{
                            areaColor:'#8796B4'
                        }
                    }
                },
                // 系列列表
                // series:[
                //     {
                //         name:'二手车市场销量',
                //         type:'scatter',
                //         // 使用地理坐标系，通过geoIndex置顶相应的地理坐标系组件
                //         coordinateSystem:'geo',
                //         data:[],
                //         // 标记的大小
                //         symbolSize:12,
                //         // 鼠标悬浮的时候在圆点上显示数值
                //         label:{
                //             normal:{
                //                 show:false
                //             },
                //             emphasis:{
                //                 show:false
                //             }
                //         },
                //         itemStyle: {
                //             normal: {
                //                 color: '#ddb926'
                //             },
                //             // 鼠标悬浮的时候圆点样式变化
                //             emphasis: {
                //                 borderColor: '#fff',
                //                 borderWidth: 1
                //             }
                //         }
                //     },
                //     {
                //         name: 'top5',
                //         // 表的类型 这里是散点
                //         type: 'effectScatter',
                //         // 使用地理坐标系，通过 geoIndex 指定相应的地理坐标系组件
                //         coordinateSystem: 'geo',
                //         data: [],
                //         // 标记的大小
                //         symbolSize: 12,
                //         showEffectOn: 'render',
                //         rippleEffect: {
                //         brushType: 'stroke'
                //         },
                //         hoverAnimation: true,
                //         label: {
                //         normal: {
                //             show: false
                //         }
                //         },
                //         itemStyle: {
                //         normal: {
                //             color: '#f4e925',
                //             shadowBlur: 10,
                //             shadowColor: '#333'
                //         }
                //         },
                //         zlevel: 1
                //     }
                // ]
            }
            Objs.setOption(option)
        },
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