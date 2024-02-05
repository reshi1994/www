<script lang="ts" setup>
import {FormInstance} from "element-plus";
import {reactive, ref, toRefs} from "vue";

// 构建表单实例
const ruleFormRef = ref<FormInstance>()

// 重置表格
const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}

// 构建表单
const rulForm = reactive({
  userName: '',
  surName: '',
  givenName: '',
  gender: '',
  pwd: '',
  pwd2: '',

})

const {userName, surName, givenName, gender, pwd, pwd2} = toRefs(rulForm)
rulForm.userName = `${surName} ${givenName}`


</script>


<template>
  <el-form
      ref="ruleFormRef"
      :model="rulForm"
      label-width="120px"
      class="demo-ruleForm"
  >
    <!--    用户名   -->
    <el-form-item label="User name" prop="userName">
      <el-input v-model="userName" type="text" autocomplete="off"  readonly />
    </el-form-item>

    <!--    姓   -->
    <el-form-item label="Sur name" prop="surName">
      <el-input v-model="surName" type="text" autocomplete="off"/>
    </el-form-item>
    <!--    名-->
    <el-form-item label="Given name" prop="givenName">
      <el-input v-model="givenName" type="text" autocomplete="off"/>
    </el-form-item>

    <!--性别-->
    <el-form-item label="Gender">
      <el-radio-group v-model="gender" prop="gender">
        <el-radio border label="女"/>
        <el-radio border label="男"/>
      </el-radio-group>
    </el-form-item>

    <!--密码-->
    <el-form-item label="Password" prop="pwd">
      <el-input v-model="pwd" type="password" autocomplete="off"/>
    </el-form-item>
    <el-form-item label="Confirm" prop="pwd2">
      <el-input v-model="pwd2" type="password" autocomplete="off" />
    </el-form-item>

<!--提交按钮-->
    <el-form-item>
      <el-button type="primary" @click="console.log(ruleFormRef)"
      >Submit
      </el-button
      >
      <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
    </el-form-item>


  </el-form>
</template>

<style lang="less" scoped>

</style>


