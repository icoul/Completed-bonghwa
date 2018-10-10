import Vue from 'vue'
import Vuex from 'vuex'
import api from './api.js'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000'

const store = new Vuex.Store({
    state: {
        users: {},
        token: 'ABFBRHRWWGWRGRGWR'
    },
    mutations: {
        'GET_USER': function (state, response) {
            state.users = response.body
        },
        'ADD_USER': function (state, response) {
            state.users.push(response.body)
        },
        'DELETE_USER': function (state) {

        },
        'API_FAIL': function (state, error) {
            console.log(error)
        }
    },
    getters: {
        getToken: state => {
            return state.token
        },
        checkToken: (state, getters) => {
            return getters.getToken !== ''
        }
    },
    actions: {
        getUsers (store) {
            return api.get(apiRoot + '/login/')
                .then((response) => store.commit('GET_USER', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
    }
})

export default store
