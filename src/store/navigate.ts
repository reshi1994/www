import {loginProperty} from './login'
import {reactive} from "vue";

// 不同 store.ts 文件之间相互调用时， 必须要先修改原来的数据后， 才能够使用，直接使用显示undefined; 而在vue script中，可以先加载pinia , 然后加载组件
// ts 文件的加载 早于 pinia；所以在
export const navigateProperty = reactive({
    loginedUser:{
        surName: 'SignIn',
        givenName: 'Here'
    },

})



export const navigateHooks = function (){
    const switchDrawer = function (){
        loginProperty.loginDrawer.show = !loginProperty.loginDrawer.show
        console.log(loginProperty.loginDrawer.show)
    }
    return {switchDrawer}
}

