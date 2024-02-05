<script lang="ts" setup>
import {toRefs} from "vue";
import loginC from  './loginC.vue'
import {loginProperty} from '@/store/login'
const {show} = toRefs(loginProperty.loginDrawer)

</script>

<template>
  <el-drawer v-model="show" title="I am the title" :with-header="false" direction="ttb" size="90%"
             style="--el-drawer-bg-color:none">
    <loginC />
  </el-drawer>

</template>

<style scoped lang="less">

</style>