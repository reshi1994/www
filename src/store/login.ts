import {defineStore} from "pinia";
import request from "@/store/request";
import {onBeforeMount, onMounted, reactive} from "vue";

export const loginProperty = reactive({
    loginDrawer: {
        show: false
    },
    loginTables: {
        signIn: {
            user: '',
            pwd: ''
        },
        resetPwd: {
            user: '',
            pwd: '',
            pwd2: ''
        },
        signUp: {
            invitationCode: '',
        }
    },

    signUpDrawer:{
        show: false
    }


})

