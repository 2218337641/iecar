<template>
  <div class="tab">
      <!-- 二手车销量表 -->
      <section ref='char1'></section>
      <!-- 折价率以及使用年限 -->
      <section ref = 'char2'></section>
      <!-- <section ref='char3'></section> -->
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
    name:'echar',
    data(){
        return{
        }
    },
    created(){
        this.$store.commit('charX1'),
        this.$store.commit('charX3')
        // this.$store.commit('charX3')
    },
    mounted(){
        this.$nextTick(function(){
            this.drawLine();
        })
    },
    methods:{
        drawLine(){
        var myChart = echarts.init(this.$refs.char2)
        var myChart1 = echarts.init(this.$refs.char1)
        // var myChart2 = echarts.init(this.$refs.char3)
        var option = JSON.parse(JSON.stringify(this.$store.state.x1))
        var option1 = JSON.parse(JSON.stringify(this.$store.state.x3))
        // var option2 = JSON.parse(JSON.stringify(this.$store.state.x3))
        myChart.setOption(option)
        // myChart1.setOption(option1)
        myChart1.setOption({
            title:{
                text:"南北方各大城市新上架二手车辆折价率与使用年限对比图",
                subtext:'数据来源：汽车之家二手车      限定车龄:5年',
            },
            tooltip: {
                trigger: 'axis'
            },
            toolbox: {
            feature: {
            }
            },
            legend: {
                data: [
                    { name: '平均年限', icon: 'circle' },
                    '平均折价率'
                ],
                right: 90
            },
            grid: [{
                left: 50,
                right: 50,
                // height: '50%'
            }, {
                left: 50,
                right: 50,
                top: '59.5%',
                // height: '35%'
            }],
            xAxis: [
            {
                type: 'category',
                data: [
                '沈阳','北京','天津','青岛','西安','重庆','武汉','南京','广州','深圳'
                ],
                axisPointer: {
                    type: 'shadow'
                },
                axisTick: { show: false }
            },
            {
                // gridIndex: 1,
                type: 'category',
                axisPointer: {
                type: 'shadow'
                },
                position: 'top',
                axisTick: { show: false },
                axisLine:{show:false}
            }
            ],
            yAxis: [
            {
                type: 'value',
                min: 0,
                max: 10,
                interval: 1,
                splitLine: { show: false },
                axisTick: { show: false }
            },
            {
                // gridIndex: 1,
                type: 'value',
                min: 0,
                max: 100,
                // inverse: true,
                interval: 20,
                splitLine: { show: false },
                axisLabel: {
                formatter: function (item) {
                    if (item === 0) {
                    item = ''
                    } else {
                    item = item + '%'
                    }
                    return item
                },
                },
                axisTick: { show: false }
            }
            ],
            series: [
            {
                name: '平均年限',
                type: 'bar',
                barWidth: 14,
                itemStyle: {
                normal: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                    offset: 0,
                    color: '#2b8fff'
                    },
                    {
                    offset: 1,
                    color: '#1660ff'
                    }
                    ], false)
                }
                },
                barGap: '0%',
                data: this.$store.state.series[0]
            },
            {
                name: '平均折价率',
                type: 'line',
                // xAxisIndex: 1,
                yAxisIndex: 1,
                symbolSize: 8,
                label: {
                show: true,
                formatter: '{c}%'
                },
                itemStyle: {
                color: 'lightgreen'
                },
                data: this.$store.state.series[1]
            }

            ]
        })
        // myChart2.setOption(option2)
        }
    }
}
</script>

<style lang="less" scoped>
    .tab{
        width: 1580px;
        height: 100%;
        background-color: rgb(217, 234, 236);

    }
    section{
        float: left;
        width: 1580px;
        height: 300px;
        background-color: rgb(217, 234, 236);
    }
    section:nth-child(1){
        margin-right: 10px;
        height: 550px;
    }
    section:nth-child(2){
        margin-left: 520px;
        margin-bottom: 10px;
        width: 450px;
    }
</style>