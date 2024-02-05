<script lang="ts" setup>
import headerC from '@/components/headerC.vue'
import NavigateC from "@/components/navigateC.vue";
import settingC from '@/components/settingC.vue'
import preloaderC from '@/components/preloaderC.vue'
import loginC from '@/components/loginC.vue'
import registerC from "@/components/registerC.vue";
</script>

<template>
  <!--  固定展示区  一般为 导航栏  和  标题-->
  <!--   navigate   -->
  <!--  <preloader-c/>-->
  <header-c/>
  <setting-c/>
  <navigate-c/>

  <!--  挂载登录组件 注册组件 重置密码组件-->
  <login-c/>

  <register-c/>


  <!--  主要展示内容区   路由视图-->
  <router-view/>
</template>

<style lang="less">

</style>
