import Vue from 'vue'
import Vuex from 'vuex'

import { account } from './account.module'
import { posts } from './posts.module'
import { users } from './users.module'

Vue.use(Vuex)

export const store = new Vuex.Store({
    modules: {
        account,
        posts,
        users
    }
})
