<template>
    <div id="signIn">
        <div id="loginCont">
            <form method="post" action="{% url 'bonghwa:authentication' %}">
                {% csrf_token %}
                
                <input type="submit" value="로그인" />
            </form>
                <input @click="signup" type="button" value="회원가입" />
                <input @click="pass_change" type="button" value="비밀번호 찾기" />
        </div>
    </div>
</template>

<script>
export default {
    name: 'signIn',
    data() {
        return {
            
        }
    },
}
</script>
