<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import axios from "axios"
import {
  mapState,
  mapMutations
} from 'vuex'
export default {
  data(){
    return{
      rest:{},
      souced:[],
      serie:[],
      southird:[],
      northird:[],
      linethird:[],
      otherthird:[],
      lessen:[],
      lineco:[],
    }
  },
  created(){
    this.get()
  },
  computed:{
    ...mapState(['source','series'])
  },
  methods:{
    get(){
      axios.get('http://127.0.0.1/user').then(res=>{
        console.log(res.data);
        // 所有数据
        this.rest = res.data
        // 南北方车辆数据数组
        this.souced = [this.rest[0].conorth,this.rest[0].cosounth]
        // 各地二手车年限与折价率
        this.serie = [[this.rest[0].sytim,this.rest[0].bjtim,this.rest[0].tjtim,this.rest[0].qdtim,this.rest[0].xatim,this.rest[0].cqtim,this.rest[0].whtim,this.rest[0].njtim,this.rest[0].gztim,this.rest[0].sztim],[this.rest[0].sypro*100,this.rest[0].bjpro*100,this.rest[0].tjpro*100,this.rest[0].qdpro*100,this.rest[0].xapro*100,this.rest[0].cqpro*100,this.rest[0].whpro*100,this.rest[0].njpro*100,this.rest[0].gzpro*100,this.rest[0].szpro*100]]
        console.log(this.souced)
        console.log(this.serie)
        // 南北方三年内油用车及新能源车数据
        this.northird = [this.rest[0].count_norpet,this.rest[0].count_noren]
        this.southird = [this.rest[0].count_soupet,this.rest[0].count_souen]
        // 一二线的新能源对比数据
        this.linethird = [this.rest[0].count_thlipe,this.rest[0].count_thlien]
        this.otherthird = [this.rest[0].count_otlipe,this.rest[0].count_otlien]
        this.lessen = [this.rest[0].bjen,this.rest[0].xaen,this.rest[0].cqen,this.rest[0].njen,this.rest[0].gzen,this.rest[0].szen]
        // 线级城市数据
        this.lineco = [this.rest[0].count_li,this.rest[0].count_ot]
        console.log(this.lineco)
        this.linepr = [this.rest[0].res_linepr,this.rest[0].res_otpr]
        this.lineti = [this.rest[0].res_lineti,this.rest[0].res_otti]
        this.linero = [this.rest[0].res_linero,this.rest[0].res_otro]
        // console.log(this.rest)
        // console.log(this.rest[0].njpro)
        this.$store.commit("getsncount",this.souced)
        this.$store.commit("getct",this.serie)
        this.$store.commit("getnorthird",this.northird)
        this.$store.commit("getsouthird",this.southird)
        this.$store.commit("getlinethird",this.linethird)
        this.$store.commit("getotherthird",this.otherthird)
        this.$store.commit("getlessen",this.lessen)
        this.$store.commit("getlineco",this.lineco)
        this.$store.commit("getlinepr",this.linepr)
        this.$store.commit("getlineti",this.lineti)
        this.$store.commit("getlinero",this.linero)
        console.log(this.source)
      }).catch(err=>{
        console.log("获取数据失败"+err)
      })
    }
  }
}

</script>

<style lang="less" scoped>

</style>