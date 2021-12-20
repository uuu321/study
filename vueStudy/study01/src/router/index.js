import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import First from '@/components/views/First'
import User from '@/components/User'

//第三方库需要Use一下才能用
Vue.use(Router)

//new：实例化Router，将routes添加进去
//export default：抛出这个实例对象方便外部读取以及访问
export default new Router({
  //定义routes路由的集合，数组类型
  routes: [
  //单个路由均为对象类型，path：路径，component：组件
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },{
      path: '/first',
      name: 'First',
      component: First
    },
  //当匹配到路径为空的时候，重定向，执行重定向的路由
    {
      path: '/empty1',
      name: 'empty1',
      redirect: '/first'
    },
  //或者重新配置路由，router-view指定跳转页面
    {
      path: '/empty2',
      name: 'empty2',
      component: First
    },
  //动态路由Query
    {
      path: '/UserQuery',
      name: 'UserQuery',
      component: User
    },
  //动态路由Param
    {
      path: '/UserParam/:name/:id/:sex',
      name: 'UserParam',
      component: User
    }

  ]
})
