import api from '../api.js'
import router from '../router'

const apiRoot = 'http://localhost:8000'

const state = {
    token: '',
    user: {}
};

const mutations = {
    'SET_TOKEN': function (state, response) {
        state.token = response.body.token;

        if (state.token === '') {
            router.push('Login');
        }
    },
    'LOGIN_SUCCESS': function (state, response) {
        state.token = response.body.token;

        if (state.token !== '') {
            router.push('Main');
        }
    },
    'SIGNUP_RESULT': function (state, response) {
        const message = response.body.message;
        const result = response.body.result;

        window.alert(message);

        if (result === '1') {
            router.push('Login');
        }
    },
    'LOGIN_FAIL': function (state) {
        window.alert('로그인에 실패했습니다.');
    },
    'LOGOUT': function (state, response) {
        state.token = '';
        router.push('Login');
    },
    'API_FAIL': function (state, error) {
        console.log(error);
    }
};

const actions = {
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
    },
    signUp (store, user) {
        api.post(`${apiRoot}/signUp/${user.id}/${user.password}/${user.email}`)
            .then((response) => store.commit('SIGNUP_RESULT', response))
            .catch((error) => store.commit('API_FAIL', error))
    },
    findPass (store, info) {
        api.post(`${apiRoot}/findPass/${info.id}/${info.email}`)
            .then((response) => store.commit('SIGNUP_RESULT', response))
            .catch((error) => store.commit('API_FAIL', error))
    }
};

export const account = {
    namespaced: true,
    state,
    actions,
    mutations
};
