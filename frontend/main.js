import Vue from 'vue'
import App from './App.vue'
import validatePlugin from './plugin/validatePlugin'
import websocket from './router/websocket'
import router from './router'

// Vuex
import { store } from './vuex'

Vue.use(validatePlugin)

// eslint-disable-next-line no-new
new Vue(
    {
        el: '#app',
        router,
        store,
        websocket,
        render: h => h(App),
        components: { App },
        template: '<App/>'
    }
);
