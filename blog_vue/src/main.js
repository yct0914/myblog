import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueRouter from 'vue-router'
import router from './router'
Vue.config.productionTip = false

//使用ElementUI插件
Vue.use(ElementUI)
//使用vue-router
Vue.use(VueRouter)
new Vue({
  render: h => h(App),
  router:router,
  data:function(){
    return {
      isLogon:false
    }
  },
  
  beforeCreate() {
    //全局事件总线创建
    Vue.prototype.$bus = this
    //自动跳转到Index
    this.$router.push('/logon')
  },
}).$mount('#app')
//注册一个路由前置守卫
router.beforeEach((to,from,next)=>{
  //默认跳转到微博新闻
  if(to.name == 'news'){
    next({name:'weibo',replace:true})
  }
  next()
})