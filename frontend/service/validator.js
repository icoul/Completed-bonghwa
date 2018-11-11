const validateFns = {
    required (key, val) {
        if (!val) {
            return `${key}는 필수입력입니다.`
        }
    },
    minLen6 (key, val) {
        if (!val || val.length < 6) {
            return `${key}는 6자 이상이어야합니다.`
        }
    },
    equalPass (key, val) {
        if (val !== validator.password) {
            return `입력한 비밀번호 값이 다릅니다.`
        }
    }
}

const validator = {
    password: '',
    init () {
        this.errors = {}
        this.password = ''
        this.validates = new Map()
        return this
    },

    setup (key, expression) {
        const validates = expression.replace(/'/g, '').split('|')
        this.validates.set(key, validates)
    },

    validate (key, value) {
        if (key === 'password') {
            validator.password = value
        }
        
        const validates = this.validates.get(key)
        const errors = validates
            .map(v => validateFns[v](key, value))
            .filter(v => !!v)
        return errors
    }
}

export default validator.init()
