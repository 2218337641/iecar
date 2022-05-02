<template>
    <div class="tab">
      <section ref='char1'></section>
      <section ref = 'char2'></section>
      <section ref='char3'></section>
      <section ref='char4'></section>
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
    data(){
        return{

        }
    },
    mounted(){

    },
    created(){
        this.$nextTick(function(){
            this.drawLine()
        })
    },
    methods:{
        drawLine(){
            var myChart1 = echarts.init(this.$refs.char1)
            var myChart2 = echarts.init(this.$refs.char2)
            var myChart3 = echarts.init(this.$refs.char3)
            var myChart4 = echarts.init(this.$refs.char4)
            myChart1.setOption({
                title:{
                    text:"线级城市二手车存量差异柱状图",
                    subtext:'数据来源:汽车之家二手车',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                xAxis: {
                type: 'category',
                data: ['一二线城市', '其他城市']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                data: this.$store.state.lineco,
                type: 'bar'
                }
            ]
            }),
            myChart2.setOption({
                title:{
                    text:"线级城市二手车平均价格差异柱状图",
                    subtext:'数据来源:汽车之家二手车',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                xAxis: {
                type: 'category',
                data: ['一二线城市', '其他城市']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                data: this.$store.state.linepr,
                type: 'bar'
                }
            ]
            }),
            myChart3.setOption({
                title:{
                    text:"线级城市二手车平均出售年限差异柱状图",
                    subtext:'数据来源:汽车之家二手车',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                xAxis: {
                type: 'category',
                data: ['一二线城市', '其他城市']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                data: this.$store.state.lineti,
                type: 'bar'
                }
            ]
            }),
            myChart4.setOption({
                title:{
                    text:"线级城市二手车平均里程差异柱状图",
                    subtext:'数据来源:汽车之家二手车',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                xAxis: {
                type: 'category',
                data: ['一二线城市', '其他城市']
            },
            yAxis: {
                type: 'value'
            },
            series: [
                {
                data: this.$store.state.linero,
                type: 'bar'
                }
            ]
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
        width: 785px;
        height: 405px;
        background-color: rgb(217, 234, 236);
    }
    section:nth-child(odd){
        margin-right: 10px;
    }
    section:nth-child(-n+2){
        margin-bottom: 10px;
    }
</style>