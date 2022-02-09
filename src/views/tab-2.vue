<template>
    <div class="tab">
      <section ref='char1'></section>
      <section ref = 'char2'></section>
      <section ref='char3'></section>
      <section ref='char3'></section>
  </div>
</template>

<script>
export default {
    data(){
        return{

        }
    },
    mounted(){

    },
    created(){
        
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