import Vue from 'vue'
import App from './App.vue'
import router from './router'

// Vuex
import store from './vuex/store.js'
// eslint-disable-next-line no-new
new Vue(
    {
        el: '#app',
        router,
        store: store,
        render: h => h(App),
        components: { App },
        template: '<App/>'
    }
);
