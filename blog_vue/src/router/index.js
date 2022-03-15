import VueRouter from "vue-router"
import Index from '../pages/Index'
import Login from '../pages/Login'
import Logon from '../pages/Logon'
import News from '../pages/News'
import WeiBo from '../pages/news/WeiBo'
import SelfInfo from '../pages/SelfInfo'
export default new VueRouter({
    routes:[
        {
            name:'index',
            path:'/index',
            component:Index,
        },
        {
            name:'news',
            path: '/news',
            component:News,
            children:[
                {
                    name:'weibo',
                    path: 'weibo',
                    component:WeiBo
                }
            ]
        },
        {
            name:'login',
            path:'/login',
            component:Login
        },
        {
            name:'logon',
            path:'/logon',
            component:Logon
        },
        {
            name:'self_info',
            path:'/self_info',
            component:SelfInfo
        }
    ]
})