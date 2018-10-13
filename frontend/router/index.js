import Vue from 'vue'
import Router from 'vue-router'
import SignIn from '../component/SignIn.vue'
import Contents from '../component/Contents.vue'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Contents',
            component: Contents
        },
        {
            path: '/test',
            name: 'SignIn',
            component: SignIn
        }
    ]
})
