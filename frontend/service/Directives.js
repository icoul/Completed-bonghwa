import validator from './validator'

export default {
    validate: {
        bind (el, binding, vnode) {
            validator.setup(el.name, binding.expression, vnode.context)
        }
    }
}
