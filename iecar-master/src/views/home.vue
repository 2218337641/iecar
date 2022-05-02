<template>
  <div class="home">
    <el-container>
      <el-header>
        二手车市场地域性差异
      </el-header>
      <el-container id="con">
          <el-aside>
            <el-menu
              default-active="1"
              class="el-menu-vertical-demo"
            >
            <el-menu-item index='1' @click="changeView(1)">
              <span slot="title">南北方二手车市场差异</span>
              </el-menu-item>
              <el-menu-item index='2' @click="changeView(0)">
                <span slot="title">不同分级城市二手车市场差异</span>
              </el-menu-item>
              <el-menu-item index='4' @click="changeView(4)">
                <span slot="title">油电车二手车市场地域性差异</span>
              </el-menu-item>
              <el-menu-item index='3' @click="changeView(3)">
                <span slot="title">中国省级行政区二手车市场概览</span>
              </el-menu-item>
            </el-menu>
          </el-aside>
          <el-main>
            <router-view></router-view>
          </el-main>
      </el-container>
  </el-container>
 
  </div>
</template>

<script>
export default {
  name:'home',
  data(){
    return{
    }
  },
  methods:{
    changeView(fl){
      // console.log(fl)
      if(fl==1){
        this.$router.push('tab-1')
      }else if(fl==0){
        this.$router.push('tab-2')
      }else if(fl==3){
        this.$router.push('tab-3')
      }else{
        this.$router.push('tab-4')
      }
      
    }
  }
}
</script>

<style lang="less" scoped>

    .home{
        width: 1920px;
        height: 100%;
        background-color: rgb(235, 235, 235);
    }
    .el-header{
        background-color: rgb(26, 106, 211);
        text-align: center;
        color: #fff;
        font-size: 28px;
        line-height: 80px;
        height: 80px !important;
    }
    .el-aside{
        font-size: 20px;
        height: 100%;
        background-color: #fff;
        border-right: 1px solid #e6e6e6;
        .el-menu{
          border-right: none;
          .el-menu-item{
            text-align: center;
            font-size: 18px;
            height: 80px;
            line-height: 80px;
            border-bottom: 1px solid #e6e6e6;

          }
        }
        
    }
    .el-main{
        height: 100%;
    }
   #con{
     height: 860px;
   }

    
</style>