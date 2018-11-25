import api from '../api.js'
import router from '../router'

const apiRoot = 'http://localhost:8000'

const state = {
    post: {},
    posts: [],
    linkPosts: {}
};

const mutations = {
    'SET_POST': function (state, response) {
        state.posts = response.body.posts
    },
    'API_FAIL': function (state, error) {
        console.log(error);
    }
};

const actions = {
    getPosts (store) {
        api.get(apiRoot + '/getPosts/')
            .then((response) => store.commit('SET_POST', response))
            .catch((error) => store.commit('API_FAIL', error))
    }
};

export const posts = {
    namespaced: true,
    state,
    actions,
    mutations
};