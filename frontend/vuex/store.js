import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api.js'
import router from '../router'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000'

const store = new Vuex.Store({
    state: {
        users: {},
        token: ''
    },
    mutations: {
        'SET_TOKEN': function (state, response) {
            state.token = response.body.token
            
            if (state.token === '') {
                router.push('Login')
            }
        },
        'CHECK_TOKEN': function (state) {
            return state.token === ''
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
        async setTokenFromServer (store) {
            api.get(apiRoot + '/auth/')
                .then((response) => store.commit('SET_TOKEN', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
    }
})

export default store
