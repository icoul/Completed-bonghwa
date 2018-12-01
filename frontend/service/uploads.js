import Vue from 'vue'
import Axios from 'axios';

export default {
    uploadImage (form, cb, ecb = null) {
        Axios.post('/sendPost', form)
            .then(response => cb(response))
            .catch(error => ecb(error))
    }
}
