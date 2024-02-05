import  {defineStore} from "pinia";
import request from "@/store/request";
import {reactive} from "vue";



export const teamProperty = reactive({
    teamMembers: [],
    postInfo:{
        'action': 'queryTeamMembers'
    }
})


export const teamHooks = function (){
    const reqTeamMembers = async function(){
        const  response = await request.post('/queryData', teamProperty.postInfo, {
            headers: {
                'content-type': 'application/json', // 设置请求头为 JSON
            },
            withCredentials: true
        })
        teamProperty.teamMembers = response.data
        // console.log(queryTeamMembers.teamMembers)
    }

    return {reqTeamMembers}
}

