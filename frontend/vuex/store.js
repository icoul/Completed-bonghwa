import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api.js'
import router from '../router'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000'

const store = new Vuex.Store({
    state: {
        token: '',
        loginId: '',
        loginPassword: ''
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
                router.push('/')
            }
        },
        'LOGIN_FAIL': function (state) {
            window.alert('로그인에 실패했습니다.');
        },
        'DELETE_USER': function (state) {

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
        }
    }
})

export default store
