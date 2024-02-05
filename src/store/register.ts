import {reactive} from "vue";
import request from '@/store/request'
import Swal from 'sweetalert2'

export const registerProperty = reactive({
    account: {
        email: {
            label:'Email Address*',
            name:'email',
            value:''
        },
        userName: {
            label:'Username*',
            name:'userName',
            value:''
        },
        pwd: {
            label:'Password*',
            name:'pwd',
            value:''
        },
        pwd2: {
            label:'Confirm Password*',
            name:'pwd2',
            value:''
        }
    },
    personal:{
        fullName:{
            label:'Full Name*',
            name:'fullName',
            value:''
        },
        phone:{
            label:'Phone*',
            name:'phone',
            value:''
        },
        wechat:{
            label:'WeChat*',
            name:'wechat',
            value:''
        },
        address:{
            label:'Address',
            name:'address',
            value:''
        }

    }
})



export const registerHooks = function (){


    const registerBlu = async function(){
        interface Response {
            res: boolean,
            print: string,
            data: any
        }
        const  response:Response = await request.post('/register', registerProperty, {
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
            await Swal.fire({
                title: "Register Success!",
                icon: "success"
            });
        }



        console.log(response)
    }
    return {registerBlu}
}