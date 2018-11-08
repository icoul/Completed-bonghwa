import Vue from 'vue'
import Router from 'vue-router'
import Index from '../component/Index.vue'
import Main from '../component/Main.vue'
import Login from '../component/signIn/Login.vue'
import SignUp from '../component/signIn/SignUp.vue'
import PassChange from '../component/signIn/PassChange.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Index',
            component: Index
        },
        {
            path: '/main',
            name: 'Main',
            component: Main
        },
        {
            path: '/login',
            name: 'Login',
            component: Login
        },
        {
            path: '/signUp',
            name: 'SignUp',
            component: SignUp
        },
        {
            path: '/passChange',
            name: 'PassChange',
            component: PassChange
        }
    ]
})
