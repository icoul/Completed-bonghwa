import api from '../api.js'
import router from '../router'
import uploads from '../service/uploads'

const apiRoot = 'http://localhost:8000'

const state = {
    post: {},
    posts: [],
    linkPosts: {}
};

const mutations = {
    'SET_POST': function (state, response) {
        state.posts = response.body.posts;
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
    },
    sendPost (store, form) {
        return new Promise((resolve, reject) => {
            uploads.uploadImage(form,
                response => {
                    resolve(true);
                },
                errors => {
                    store.commit('API_FAIL')
                }
            )
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
    }
};

export const posts = {
    namespaced: true,
    state,
    actions,
    mutations
};
