import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api.js'

Vue.use(Vuex)
const apiRoot = 'http://localhost:8000'

const store = new Vuex.Store({
    state: {
        users: {},
        token: ''
    },
    mutations: {
        'GET_TOKEN': function (state, response) {
            state.token = response.body.token
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
        getToken (store) {
            return api.get(apiRoot + '/auth/')
                .then((response) => store.commit('GET_TOKEN', response))
                .catch((error) => store.commit('API_FAIL', error))
        },
    }
})

export default store
