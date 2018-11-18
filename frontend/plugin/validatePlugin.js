import Directives from '../service/Directives'
import validator from '../service/validator'

export default {
    install (Vue) {
        Vue.directive('validate', Directives.validate)

        Vue.mixin({
            data () { return { errorBag: {} } },
            computed: {
                $errors () {
                    const errorBag = this.errorBag || {}

                    return {
                        has (key) { return !!errorBag[key] },
                        first (key) { return errorBag[key][0] },
                        length () { return Object.keys(JSON.parse(JSON.stringify(errorBag))).length }
                    }
                },
                $validator () {
                    const context = this

                    return {
                        validateAll () {
                            for (const key of validator.validates.keys()) {
                                const errors = validator.validate(key, context.user[key])

                                if (errors.length) {
                                    context.$set(context.errorBag, key, errors)
                                } else {
                                    context.$delete(context.errorBag, key)
                                }
                            }

                            return new Promise(function (resolve, reject) {
                                resolve(context.$errors.length() === 0)
                            })
                        }
                    }
                }
            }
        })
    }
}
