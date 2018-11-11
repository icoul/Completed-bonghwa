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
                        first (key) { return errorBag[key][0] }
                    }
                },
                $validator () {
                    const context = this

                    return {
                        validateAll () {
                            for (const key of validator.validates.keys()) {
                                const errors = validator.validate(key, context[key])

                                if (errors.length) {
                                    context.$set(context.errorBag, key, errors)
                                } else {
                                    context.$delete(context.errorBag, key)
                                }
                            }
                        }
                    }
                }
            }
        })
    }
}
