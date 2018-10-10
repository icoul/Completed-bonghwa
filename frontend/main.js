import Vue from 'vue'
import App from './App.vue'
// Vuex
import store from './store.js'
// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    store: store,
    render: h => h(App)
});
