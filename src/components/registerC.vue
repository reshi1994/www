<script lang="ts" setup>
import {onMounted, toRefs} from "vue";
// 这里按需导入所需要的 JS CSS文件，否则 会出现样式动画加载不成功得到情况
onMounted(async () => {
  await import((`/public/src/plugins/jquery-steps/jquery.steps.js`));
  await import((`/public/vendors/scripts/steps-setting.js`));
});

import {registerProperty} from '@/store/register'
const {account, personal} = toRefs(registerProperty)

import {registerHooks} from "@/store/register";
const {registerBlu} = registerHooks()


</script>

<template>
  <!-- register modal -->
  <div class="modal fade" id="register-modal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel"
       aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="register-box register-page-wrap bg-white box-shadow border-radius-10">
          <div class="wizard-content">
            <form  class="tab-wizard2 wizard-circle wizard" id="register-forms">
              <!-- Step 1 -->
              <h5>Basic Account Credentials</h5>
              <section name="account">
                <div class="form-wrap max-width-600 mx-auto">
                  <!--                  循环遍历 account表所需要的信息   -->
                  <div class="form-group row" v-for="(item, index) in account" :key="index">
                    <label class="col-sm-4 col-form-label">{{ item.label }}</label>
                    <div class="col-sm-8">
                      <input type="text" :name="item.name" class="form-control">
                    </div>
                  </div>

                </div>
              </section>


              <!-- Step 2 -->
              <h5>Personal Information</h5>
              <section name='personal'>
                <div class="form-wrap max-width-600 mx-auto">

                  <!--                  循环遍历 account表所需要的信息   -->
                  <div class="form-group row" v-for="(item, index) in personal" :key="index">
                    <label class="col-sm-4 col-form-label">{{ item.label }}</label>
                    <div class="col-sm-8">
                      <input type="text" :name="item.name" class="form-control">
                    </div>
                  </div>


                </div>
              </section>


              <!-- Step 3 -->
              <h5>Overview Information</h5>
              <section name="overView">
                <div class="form-wrap max-width-600 mx-auto">
                  <div class="modal-content">
                    <div class="modal-body text-center font-18">
                      <h3 class="mb-20">Register Profile Complete!</h3>
                      <div class="mb-30 text-center"><img src="/vendors/images/success.png"></div>
                      Click Submit Button To Sign In Please.
                    </div>

                  </div>
                </div>
              </section>
              <!--提交数据按钮  主要用于执行本地校验用-->
              <!--              <button href="#" type="submit" class="btn btn-primary" id="valForm" hidden>valForm</button>-->
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- success Popup html Start -->
  <!--  完成信息后， 会诱发这个按钮的点击事件   -->
  <button type="button" id="success-modal-btn" hidden @click="registerBlu">Launch modal</button>

</template>

<style scoped lang="less">
@import "/public/src/plugins/jquery-steps/jquery.steps.css";
@import "/public/src/plugins/sweetalert2/sweetalert2.css";
</style>