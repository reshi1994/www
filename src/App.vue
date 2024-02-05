<script lang="ts" setup>
import spinnerC from '@/components/spinnerC.vue'
import navigateC from '@/components/navigateC.vue'
import  loginDialogC from '@/components/loginDialogC.vue'
import {onUnmounted} from "vue";

// onUnmounted(async (){
//   wa
// })


</script>

<template>
  <loginDialogC/>
  <spinnerC/>
  <navigateC/>
  <nav>
<!--    <router-link to="/">Home</router-link> |-->
<!--    <router-link to="/about">About</router-link>-->
  </nav>
  <router-view/>
</template>

<style lang="less">

</style>
