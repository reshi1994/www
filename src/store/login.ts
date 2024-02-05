import {reactive} from "vue";
import Swal from 'sweetalert2'
import request from "@/store/request";

export const loginProperty = reactive({
    credential: {
        admin:null,
        userName:'',
        pwd:''

    },
    modalLogin:{
        show:false
    }

})


export const loginHooks = function (){
    const setAdminStatus = function (value:Boolean){
        // @ts-ignore
        loginProperty.credential.admin = value
    }

    const showBanned = async function(){
        await Swal.fire({
            title: "暂时不提供找回密码！！!",
            icon: "warning"
        });
    }
    const loginBlu = async function(){
        interface Response {
            res: boolean,
            print: string,
            data: any
        }
        const  response:Response = await request.post('/login', loginProperty.credential, {
            headers: {
                'content-type': 'application/json', // 设置请求头为 JSON
            },
            withCredentials: true
        })
        if (!response.res){
            let errorText = response.print
            await Swal.fire({
                // title: 'Error!',
                text: errorText,
                icon: 'error',
                confirmButtonText: 'Confirm',

            })
        }else {
            // await Swal.fire({
            //     title: "Login Success!",
            //     icon: "success"
            // });
            loginProperty.modalLogin.show = false
        }

        // console.log(response)
    }

    const showLogin = function (value:Boolean){
        // @ts-ignore
        loginProperty.modalLogin.show = value
        console.log(loginProperty.modalLogin.show)
    }




    return {setAdminStatus, showBanned, loginBlu, showLogin}
}
