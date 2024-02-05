<script lang="ts" setup>
import {loginProperty, loginHooks} from '@/store/login'
import {toRefs} from "vue";

const {credential, modalLogin} = toRefs(loginProperty)
const {setAdminStatus, showBanned, loginBlu} = loginHooks()
</script>

<template>
  <!-- Login modal -->
  <div v-show="modalLogin.show">
    <div class="modal fade" id="login-modal" tabindex="-1" role="dialog"
         aria-labelledby="myLargeModalLabel"
         aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="login-box bg-white box-shadow border-radius-10">
            <div class="login-title">
              <h2 class="text-center text-primary">Login To DeskApp</h2>
            </div>
            <form>
              <!--            登录身份    -->

              <div class="select-role">
                <div class="btn-group btn-group-toggle" data-toggle="buttons">
                  <label class="btn" @click.prevent="setAdminStatus(true)">
                    <input type="radio" name="options" id="admin" value="admin">
                    <div class="icon"><img src="/vendors/images/briefcase.svg" class="svg" alt=""></div>
                    <span>I'm</span>
                    Manager
                  </label>
                  <label class="btn focus active" @click.prevent="setAdminStatus(false)">
                    <input type="radio" name="options" id="user" value="user">
                    <div class="icon"><img src="/vendors/images/person.svg" class="svg" alt=""></div>
                    <span>I'm</span>
                    Employee
                  </label>
                </div>
              </div>

              <!--用户名和密码-->
              <div class="input-group custom">
                <input type="text" class="form-control form-control-lg" placeholder="Username"
                       v-model="credential.userName">
                <div class="input-group-append custom">
                  <span class="input-group-text"><i class="icon-copy dw dw-user1"></i></span>
                </div>
              </div>
              <div class="input-group custom">
                <input type="password" class="form-control form-control-lg" placeholder="**********"
                       v-model="credential.pwd">
                <div class="input-group-append custom">
                  <span class="input-group-text"><i class="dw dw-padlock1"></i></span>
                </div>
              </div>


              <div class="row pb-30">
                <div class="col-6">
                  <div class="custom-control custom-checkbox">
                    <input type="checkbox" class="custom-control-input" id="customCheck2">
                    <label class="custom-control-label" for="customCheck2">Remember</label>
                  </div>
                </div>
                <div class="col-6">
                  <!--                <div class="forgot-password"><a href="#" data-toggle="modal" data-target="#register-modal">Forgot Password</a></div>-->
                  <div class="forgot-password"><a href="#" @click="showBanned">Forgot Password</a></div>
                </div>
              </div>

              <div class="row">
                <div class="col-sm-12">
                  <div class="input-group mb-0">
                    <!--
                      use code for form submit
                      <input class="btn btn-primary btn-lg btn-block" type="submit" value="Sign In">
                    -->
                    <a class="btn btn-primary btn-lg btn-block" href="#" @click="loginBlu">Sign
                      In</a>
                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped lang="less">

</style>