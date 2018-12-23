import api from '../api.js'
import router from '../router'

const apiRoot = 'http://localhost:8000'

const state = {
    page: 1,
    option: 'all',
    post: {},
    posts: [],
    linkPosts: {}
};

const mutations = {
    'SET_POST': function (state, response) {
        response.body.posts.forEach(post => {
            state.posts.push(post);
        });
    },
    'ADD_PAGE': function (state) {
        state.page++;
    },
    'INIT_POST_OPTION': function (state, option) {
        state.option = option;
        state.page = 1;
    },
    'INIT_POST': function (state, response) {
        state.posts = response.body.posts;
    },
    'API_FAIL': function (state, error) {
        console.log(error);
    }
};

const actions = {
    getPosts (store) {
        store.commit('INIT_POST_OPTION', state.option);

        api.get(apiRoot + `/getPosts/${state.page}/${state.option}`)
            .then((response) => store.commit('INIT_POST', response))
            .catch((error) => store.commit('API_FAIL', error))
    },
    addPosts (store) {
        store.commit('ADD_PAGE');
        return new Promise((resolve, reject) => {
            api.get(apiRoot + `/getPosts/${state.page}/${state.option}`)
                .then(response => {
                    store.commit('SET_POST', response)
                    resolve(true);
                })
                .catch((error) => {
                    store.commit('API_FAIL', error)
                })
        })
    },
    sendPost (store, form) {
        return new Promise((resolve, reject) => {
            api.post(apiRoot + `/sendPost`, form)
                .then(response => {
                    resolve(response.body.result);
                })
                .catch((error) => {
                    store.commit('API_FAIL', error)
                })
        })
    },
    deletePost (store, id) {
        return new Promise((resolve, reject) => {
            api.post(apiRoot + `/deletePost/${id}`)
                .then(response => {
                    resolve(response.body.result);
                })
                .catch((error) => {
                    store.commit('API_FAIL', error)
                })
        })
    },
    sortPosts (store, option) {
        store.commit('INIT_POST_OPTION', option);
        return new Promise((resolve, reject) => {
            api.get(apiRoot + `/getPosts/${state.page}/${state.option}`)
                .then(response => {
                    store.commit('INIT_POST', response)
                    resolve(true);
                })
                .catch((error) => {
                    store.commit('API_FAIL', error)
                })
        })
    },
    getMentions (store, form) {
        return new Promise((resolve, reject) => {
            api.post(apiRoot + `/getMentions`, form)
                .then(response => {
                    resolve(response.body.mentions);
                })
                .catch((error) => {
                    store.commit('API_FAIL', error)
                })
        })
    }
};

export const posts = {
    namespaced: true,
    state,
    actions,
    mutations
};
