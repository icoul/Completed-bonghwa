import api from '../api.js'
import router from '../router'

const apiRoot = 'http://localhost:8000'

const state = {
    user: {}
};

const getters = {
    getUsername: state => {
        return state.user.username
    }
}

const mutations = {
    'SET_USER': function (state, response) {
        state.user = response.body.user;

        if (typeof state.user === 'undefined' || JSON.stringify(state.user) === '{}') {
            router.push('login');
        }

        return true
    },
    'LOGIN_SUCCESS': function (state, response) {
        state.user = response.body.user;

        if (JSON.stringify(state.user) !== '{}') {
            router.push('main');
        } else {
            window.alert('로그인에 실패했습니다.');
        }
    },
    'SIGNUP_RESULT': function (state, response) {
        const message = response.body.message;
        const result = response.body.result;

        window.alert(message);

        if (result === '1') {
            router.push('login');
        }
    },
    'LOGIN_FAIL': function (state) {
        window.alert('로그인에 실패했습니다.');
    },
    'LOGOUT': function (state, response) {
        state.user = {};
        router.push('login');
    },
    'API_FAIL': function (state, error) {
        console.log(error);
    }
};

const actions = {
    setUserFromServer (store) {
        return new Promise((resolve, reject) => {
            api.get(apiRoot + '/user/')
                .then(response => {
                    state.user = response.body.user;

                    if (typeof state.user === 'undefined' || JSON.stringify(state.user) === '{}') {
                        resolve(false);
                    } else {
                        resolve(true);
                    }
                })
                .catch((error) => {
                    store.commit('API_FAIL', error)
                })
        })
    },
    loginCheck (store, map) {
        api.get(apiRoot + `/login/${map.username}/${map.password}`)
            .then((response) => store.commit('LOGIN_SUCCESS', response))
            .catch((error) => store.commit('LOGIN_FAIL', error))
    },
    logout (store) {
        api.get(apiRoot + '/logout/')
            .then((response) => store.commit('LOGOUT', response))
            .catch((error) => store.commit('API_FAIL', error))
    },
    signUp (store, user) {
        api.post(`${apiRoot}/signUp/${user.username}/${user.password}/${user.email}`)
            .then((response) => store.commit('SIGNUP_RESULT', response))
            .catch((error) => store.commit('API_FAIL', error))
    },
    findPass (store, info) {
        api.post(`${apiRoot}/findPass/${info.username}/${info.email}`)
            .then((response) => store.commit('SIGNUP_RESULT', response))
            .catch((error) => store.commit('API_FAIL', error))
    }
};

export const account = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};
