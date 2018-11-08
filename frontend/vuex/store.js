import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api.js'
import router from '../router'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000'

const store = new Vuex.Store({
    state: {
        token: ''
    },
    mutations: {
        'SET_TOKEN': function (state, response) {
            state.token = response.body.token
            
            if (state.token === '') {
                router.push('Login')
            }
        },
        'LOGIN_SUCCESS': function (state, response) {
            state.token = response.body.token
            
            if (state.token !== '') {
                router.push('Main')
            }
        },
        'LOGIN_FAIL': function (state) {
            window.alert('로그인에 실패했습니다.');
        },
        'LOGOUT': function (state, response) {
            state.token = ''
            router.push('Login')
        },
        'API_FAIL': function (state, error) {
            console.log(error)
        }
    },
    getters: {
        
    },
    actions: {
        setTokenFromServer (store) {
            api.get(apiRoot + '/token/')
                .then((response) => store.commit('SET_TOKEN', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
        loginCheck (store, map) {
            api.get(apiRoot + '/login/' + map.id + '/' + map.password)
                .then((response) => store.commit('LOGIN_SUCCESS', response))
                .catch((error) => store.commit('LOGIN_FAIL', error))
        },
        logout (store) {
            api.get(apiRoot + '/logout/')
                .then((response) => store.commit('LOGOUT', response))
                .catch((error) => store.commit('API_FAIL', error))
        }
    }
})

export default store
