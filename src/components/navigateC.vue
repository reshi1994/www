<script lang="ts" setup>
import {loginHooks} from '@/store/login'
const {showLogin} = loginHooks()
</script>

<template>
  <div class="left-side-bar">
    <div class="brand-logo">
      <a href="javascript:">
        <img src="/vendors/images/deskapp-logo.svg" alt="" class="dark-logo">
        <img src="/vendors/images/deskapp-logo-white.svg" alt="" class="light-logo">
      </a>
      <div class="close-sidebar" data-toggle="left-sidebar-close">
        <i class="ion-close-round"></i>
      </div>
    </div>

    <div class="menu-block customscroll">
      <div class="sidebar-menu">
        <ul id="accordion-menu">

          <!--          home    -->
          <li class="dropdown">
            <a href="javascript:" class="dropdown-toggle">
              <span class="micon dw dw-house-1"></span><span class="mtext">Home</span>
            </a>
            <ul class="submenu">
              <li><a href="javascript:">Dashboard style 1</a></li>
              <li><a href="javascript:">Dashboard style 2</a></li>
            </ul>
          </li>

          <!--    team    -->
          <li>
            <a href="/team" class="dropdown-toggle no-arrow">
              <span class="micon dw dw-user-12"></span><span class="mtext">Teams</span>
            </a>
          </li>

          <!--登录页 注册页 重置密码页-->
          <li class="dropdown">
            <a href="javascript:" class="dropdown-toggle">
              <span class="micon dw dw-right-arrow1"></span><span class="mtext">Additional Pages</span>
            </a>
            <ul class="submenu">
              <li><a href="#" data-toggle="modal" data-target="#login-modal" type="button" @click.prevent="showLogin(true)">Login</a></li>
              <li><a href="#" data-toggle="modal" data-target="#register-modal" >Register</a></li>
              <li><a href="#" data-toggle="modal" data-target="#register-modal">Forgot Password</a></li>
            </ul>
          </li>

        </ul>
      </div>
    </div>
  </div>
  <div class="mobile-menu-overlay"></div>
</template>

<style scoped lang="less">

</style>