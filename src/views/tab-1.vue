<template>
  <div class="tab">
      <section ref='char1'></section>
      <section ref = 'char2'></section>
      <section ref='char3'></section>
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
        this.$store.commit('charX2')
        this.$store.commit('charX3')
    },
    mounted(){
        this.$nextTick(function(){
            this.drawLine();
        })
    },
    methods:{
        drawLine(){
        var myChart = echarts.init(this.$refs.char1)
        var myChart1 = echarts.init(this.$refs.char2)
        var myChart2 = echarts.init(this.$refs.char3)
        var option = JSON.parse(JSON.stringify(this.$store.state.x1))
        var option1 = JSON.parse(JSON.stringify(this.$store.state.x2))
        var option2 = JSON.parse(JSON.stringify(this.$store.state.x3))
        myChart.setOption(option)
        myChart1.setOption(option1)
        myChart2.setOption(option2)
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
    section:nth-child(1){
        margin-right: 10px;
    }
    section:nth-child(-n+2){
        margin-bottom: 10px;
    }
</style>