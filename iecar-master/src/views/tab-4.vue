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
        this.$nextTick(function(){
            this.drawLine();
            // this.test()
        })
    },
    created(){
        
    },
    methods:{
        // test(){
        //     console.log(this.$store.state.northird)
        // },
        drawLine(){
            var myChart1 = echarts.init(this.$refs.char1)
            var myChart2 = echarts.init(this.$refs.char2)
            var myChart3 = echarts.init(this.$refs.char3)
            var myChart4 = echarts.init(this.$refs.char4)
            myChart1.setOption({
                title:{
                    text:"油用车与新能源车二手车存量南北方占比堆叠柱状图",
                    subtext:'限定车龄:8年',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                legend: {
                    data: ['北方二手车存量','南方二手车存量'],
                    top: 30
                },
                xAxis: {
                    data: ['油用车', '新能源车']
                },
                yAxis: {},
                series: [
                    {
                        name:'北方二手车存量',
                        data: this.$store.state.northird,
                        type: 'bar',
                        stack: 'x'
                    },
                    {
                        name:'南方二手车存量',
                        data: this.$store.state.southird,
                        type: 'bar',
                        stack: 'x'
                    }
                ]
            })
            myChart2.setOption({
                title:{
                    text:"油用车与新能源车二手车存量线级城市占比堆叠柱状图",
                    subtext:'限定车龄:8年',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                legend: {
                    data: ['一二线城市二手车存量','三四线城市二手车存量'],
                    top: 30
                },
                xAxis: {
                    data: ['油用车', '新能源车']
                },
                yAxis: {},
                series: [
                    {
                        name:'一二线城市二手车存量',
                        data: this.$store.state.linethird,
                        type: 'bar',
                        stack: 'x'
                    },
                    {
                        name:'三四线城市二手车存量',
                        data: this.$store.state.otherthird,
                        type: 'bar',
                        stack: 'x'
                    }
                ]
            })
            myChart3.setOption({
                title:{
                    text:"南北方与线级城市新能源汽车存量占比概率柱状图",
                    subtext:'限定车龄:8年',
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                xAxis: {
                    data: ['南北方意愿', '线级城市意愿']
                },
                yAxis: {},
                series: [
                    {
                    type: 'bar',
                    data: [this.$store.state.southird[1]/(this.$store.state.southird[0]+this.$store.state.southird[1]),this.$store.state.linethird[1]/(this.$store.state.linethird[0]+this.$store.state.linethird[1])]
                    },
                    {
                    type: 'bar',
                    data: [this.$store.state.northird[1]/(this.$store.state.northird[0]+this.$store.state.northird[1]),this.$store.state.otherthird[1]/(this.$store.state.otherthird[0]+this.$store.state.otherthird[1])]
                    }
                ]
            })
            myChart4.setOption({
                title:{
                    text:"南北方新能源二手车存量较大城市汽车年限折线图",
                    x:'center'
                },
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'shadow'
                    }
                },
                xAxis: {
                    type: 'category',
                    data: ['北京', '西安', '重庆','南京','广州','深圳']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                    data: this.$store.state.lessen,
                    type: 'line'
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
        width: 520px;
        height: 405px;
        background-color: rgb(217, 234, 236);
    }
    section:nth-child(4){
        width: 1580px;
    }
    section:nth-child(-n+2){
        margin-bottom: 10px;
        margin-right: 10px;
    }
</style>