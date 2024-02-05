<script lang="ts" setup>
import {onMounted, toRefs} from "vue";
import {loginProperty} from "@/store/login";
// 挂载 login 界面所需要的 js文件
onMounted(async () => {
  await import((`@/assets/login/js/input-field`));
});


const {signIn, resetPwd, signUp} = toRefs(loginProperty.loginTables)

// loginDrawer.loginTables.signIn.user = 'abc'
// console.log(signIn)


</script>

<template>
  <div class="container-agille">
    <div class="formBox level-login">
      <div class="box boxShaddow"></div>

      <!--      登录面板      -->
      <div class="box loginBox">
        <h3>Login Here</h3>
        <form class="form" action="#" method="post">
          <div class="f_row-2">
            <input v-model="signIn.user" type="text" class="input-field" placeholder="Username" name="name" required>
          </div>
          <div class="f_row-2 last">
            <input v-model="signIn.pwd" type="password" name="password" placeholder="Password" class="input-field"
                   required>
          </div>
          <input class="submit-w3" type="submit" value="sign In">
          <div class="f_link">
            <a href="" class="resetTag">don't have an account?</a>
          </div>
        </form>
      </div>

      <!--			注册面板			-->
      <div class="box forgetbox agile">
        <!--        返回按钮    -->
        <a href="#" class="back icon-back" >
          <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px"
               y="0px"
               viewBox="0 0 199.404 199.404" style="enable-background:new 0 0 199.404 199.404;" xml:space="preserve">
						<polygon points="199.404,81.529 74.742,81.529 127.987,28.285 99.701,0 0,99.702 99.701,199.404 127.987,171.119 74.742,117.876
			  199.404,117.876 "/>
					</svg>
        </a>
        <h3>Register</h3>
        <form class="form" action="#" method="post">
          <p>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.</p>
          <div class="f_row last">
            <label>Invitation Code</label>
            <input v-model="signUp.invitationCode" type="text" name="name" placeholder="Invitation Code"
                   class="input-field" required>
            <u></u>
          </div>
          <button class="btn button submit-w3" @click.prevent="showSignTable">
            <span>Sign Up</span>
          </button>
        </form>
      </div>

      <!--			重置 密码面板			-->
      <div class="box registerBox wthree">
        <span class="reg_bg"></span>
        <h3>Reset Password</h3>
        <form class="form" action="#" method="post">
          <div class="f_row-2">
            <input v-model="resetPwd.user" type="text" class="input-field" placeholder="Username" name="name" required>
          </div>
          <div class="f_row-2 last">
            <input v-model="resetPwd.pwd" type="password" name="password" placeholder="Password" id="password1"
                   class="input-field" required>
          </div>
          <div class="f_row-2 last">
            <input v-model="resetPwd.pwd2" type="password" name="password" placeholder="Confirm Password" id="password2"
                   class="input-field"
                   required>
          </div>
          <input class="submit-w3" type="submit" value="Reset pwd">
        </form>
      </div>

      <!--    刷新按钮     -->
      <a href="#" class="regTag icon-add">
        <i class="fa fa-repeat" aria-hidden="true"></i>
      </a>

    </div>
  </div>
</template>

<style scoped>
@import url('@/assets/login/css/style.css');
@import url('@/assets/login/css/font-awesome.min.css');
</style>