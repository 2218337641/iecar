import Vue from 'vue'
import VueRouter from 'vue-router'

// 解决重复点击路由菜单报错问题
const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch((err) => err);
};

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: ()=>import('@/views/home.vue'),
    redirect: '/tab-1',
    children:[
      
      {
        path:'tab-2',
        component:()=>import('@/views/tab-2.vue')
      },
      {
        path:'tab-1',
        component:()=>import('@/views/tab-1.vue')
      },
      {
        path:'tab-3',
        component:()=>import('@/views/tab-3.vue')
      }
    ]
  },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

// const originalPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push(loction){
//   return originalPush.call(this,location).catch(err => err)
// }
const router = new VueRouter({
  routes
})

// const createRouter=()=>
//   new Router({
//     routes,
//   })

//   // 路由初始化
//   const router = createRouter();

//   export function resetRouter(){
//     const newRouter=createRouter();
//     router.matcher=newRouter.matcher;
//   }
export default router
