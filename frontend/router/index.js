import Vue from 'vue'
import Router from 'vue-router'
import Contents from '../component/Contents.vue'
import Login from '../component/signIn/Login.vue'
import SignUp from '../component/signIn/SignUp.vue'
import PassChange from '../component/signIn/PassChange.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Contents',
            component: Contents
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
