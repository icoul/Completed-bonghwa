import api from '../api.js'
import router from '../router'

const apiRoot = 'http://localhost:8000'

const state = {
    users: []
};

const mutations = {
    'SET_USERS': function (state, response) {
        state.users = response.body.users
    },
    'API_FAIL': function (state, error) {
        console.log(error);
    }
};

const actions = {
    getUsers (store) {
        api.get(apiRoot + '/getUsers/')
            .then((response) => store.commit('SET_USERS', response))
            .catch((error) => store.commit('API_FAIL', error))
    }
};

export const users = {
    namespaced: true,
    state,
    actions,
    mutations
};
