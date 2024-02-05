<script lang="ts" setup>
import {onMounted, toRefs} from "vue";
// 这里按需导入所需要的 JS CSS文件，否则 会出现样式动画加载不成功得到情况
onMounted(async () => {
  await import((`/public/src/plugins/jquery-steps/jquery.steps.js`));
  await import((`/public/vendors/scripts/steps-setting.js`));
});

import {user} from '@/store/register'

</script>

<template>
  <!-- register modal -->
  <div class="modal fade" id="register-modal" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="register-box register-page-wrap bg-white box-shadow border-radius-10">
          <div class="wizard-content">
            <form class="tab-wizard2 wizard-circle wizard" id="register-forms">
              <!-- Step 1 -->
              <h5>Basic Account Credentials</h5>
              <section>
                <div class="form-wrap max-width-600 mx-auto">
                  <div class="form-group row" >
                    <label class="col-sm-4 col-form-label" >Email Address*</label>
                    <div class="col-sm-8">
                      <input v-model="user.email" type="email" class="form-control" @click="console.log(user.email)">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label" >Username*</label>
                    <div class="col-sm-8">
                      <input v-model="user.userName" type="text" class="form-control">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label" >Password*</label>
                    <div class="col-sm-8">
                      <input v-model="user.pwd" type="password" class="form-control">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label" >Confirm Password*</label>
                    <div class="col-sm-8">
                      <input v-model="user.pwd2" type="password" class="form-control">
                    </div>
                  </div>
                </div>
              </section>
              <!-- Step 2 -->
              <h5>Personal Information</h5>
              <section>
                <div class="form-wrap max-width-600 mx-auto">
            <!--性别-->
                  <div class="form-group row align-items-center">
                    <label class="col-sm-4 col-form-label">Gender*</label>
                    <div class="col-sm-8">
                      <div class="custom-control custom-radio custom-control-inline pb-0">
                        <input type="radio" id="male" name="gender" class="custom-control-input">
                        <label class="custom-control-label" for="male">Male</label>
                      </div>
                      <div class="custom-control custom-radio custom-control-inline pb-0">
                        <input type="radio" id="female" name="gender" class="custom-control-input">
                        <label class="custom-control-label" for="female">Female</label>
                      </div>
                    </div>
                  </div>
<!--                  姓名    -->
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">Full Name*</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control">
                    </div>
                  </div>
<!--                  电话    -->
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">Phone*</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control">
                    </div>
                  </div>
<!--                  微信-->
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">WeChat*</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control">
                    </div>
                  </div>
<!--                  地址      -->
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">Address</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control">
                    </div>
                  </div>
                </div>
              </section>
              <!-- Step 3 -->
              <h5>Payment Method & Info</h5>
              <section>
                <div class="form-wrap max-width-600 mx-auto">
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">Credit Card Type</label>
                    <div class="col-sm-8">
                      <select class="form-control selectpicker" title="Select Card Type">
                        <option value="1">Option 1</option>
                        <option value="2">Option 2</option>
                        <option value="3">Option 3</option>
                      </select>
                    </div>
                  </div>
                  <div class="form-group row align-items-center">
                    <label class="col-sm-4 col-form-label">Credit Card Number</label>
                    <div class="col-sm-8">
                      <input type="text" class="form-control">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">CVC</label>
                    <div class="col-sm-3">
                      <input type="text" class="form-control">
                    </div>
                  </div>
                  <div class="form-group row">
                    <label class="col-sm-4 col-form-label">Expiration Date</label>
                    <div class="col-sm-8">
                      <div class="row">
                        <div class="col-6">
                          <select class="form-control selectpicker" title="Month" data-size="5">
                            <option value='01'>January</option>
                            <option value='02'>February</option>
                            <option value='03'>March</option>
                            <option value='04'>April</option>
                            <option value='05'>May</option>
                            <option value='06'>June</option>
                            <option value='07'>July</option>
                            <option value='08'>August</option>
                            <option value='09'>September</option>
                            <option value='10'>October</option>
                            <option value='11'>November</option>
                            <option value='12'>December</option>
                          </select>
                        </div>
                        <div class="col-6">
                          <select class="form-control selectpicker" title="Year" data-size="5">
                            <option>2020</option>
                            <option>2019</option>
                            <option>2018</option>
                            <option>2017</option>
                            <option>2016</option>
                            <option>2015</option>
                            <option>2014</option>
                            <option>2013</option>
                            <option>2012</option>
                            <option>2011</option>
                            <option>2010</option>
                            <option>2009</option>
                          </select>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </section>
              <!-- Step 4 -->
              <h5>Overview Information</h5>
              <section>
                <div class="form-wrap max-width-600 mx-auto">
                  <ul class="register-info">
                    <li>
                      <div class="row">
                        <div class="col-sm-4 weight-600">Email Address</div>
                        <div class="col-sm-8">example@abc.com</div>
                      </div>
                    </li>
                    <li>
                      <div class="row">
                        <div class="col-sm-4 weight-600">Username</div>
                        <div class="col-sm-8">Example</div>
                      </div>
                    </li>
                    <li>
                      <div class="row">
                        <div class="col-sm-4 weight-600">Password</div>
                        <div class="col-sm-8">.....000</div>
                      </div>
                    </li>
                    <li>
                      <div class="row">
                        <div class="col-sm-4 weight-600">Full Name</div>
                        <div class="col-sm-8">john smith</div>
                      </div>
                    </li>
                    <li>
                      <div class="row">
                        <div class="col-sm-4 weight-600">Location</div>
                        <div class="col-sm-8">123 Example</div>
                      </div>
                    </li>
                  </ul>
                  <div class="custom-control custom-checkbox mt-4">
                    <input type="checkbox" class="custom-control-input" id="customCheck2">
                    <label class="custom-control-label" for="customCheck2">I have read and agreed to the terms of services and privacy policy</label>
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
  <button type="button" id="success-modal-btn" hidden @click="console.log(user)" >Launch modal</button>
<!--  <button type="button" id="success-modal-btn" hidden data-toggle="modal" data-target="#success-modal" data-backdrop="static">Launch modal</button>-->
<!--  <div class="modal fade" id="success-modal" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">-->
<!--    <div class="modal-dialog modal-dialog-centered max-width-400" role="document">-->
<!--      <div class="modal-content">-->
<!--        <div class="modal-body text-center font-18">-->
<!--          <h3 class="mb-20">Form Submitted!</h3>-->
<!--          <div class="mb-30 text-center"><img src="vendors/images/success.png"></div>-->
<!--          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod-->
<!--        </div>-->
<!--        <div class="modal-footer justify-content-center">-->
<!--          <a href="#" class="btn btn-primary">Done</a>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
</template>

<style scoped lang="less">
//<link rel="stylesheet" type="text/css" href="src/plugins/jquery-steps/jquery.steps.css">
@import "/public/src/plugins/jquery-steps/jquery.steps.css";

</style>