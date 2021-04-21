<template>
  <div id="app">
    <div class="login">
      <div class="login-form">
        <h3 class="log-h3bt" title="智慧宿管云平台">智慧宿管云平台</h3>
        <el-form
          :model="ruleForm"
          status-icon
          :rules="rules"
          ref="ruleForm"
          label-width
          class="demo-ruleForm"
        >
          <el-form-item label prop="pass">
            <!-- <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input> -->
            <el-input placeholder="密码" v-model="ruleForm.pass" name="username">
              <i slot="prefix" class="iconfont ic1">&#xe683;</i>
            </el-input>
          </el-form-item>
          <el-form-item label prop="checkPass">
            <!-- <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input> -->
            <el-input placeholder="密码" v-model="ruleForm.checkPass" name="password" type="password">
              <i slot="prefix" class="iconfont ic1">&#xe617;</i>
            </el-input>
          </el-form-item>
          <el-form-item label prop="age">
            <!-- <el-input v-model.number="ruleForm.age" style="width:50%;float:left;"></el-input> -->
            <el-input
              placeholder="验证码"
              v-model="ruleForm.age"
              style="width:50%;float:left;"
              name="code"
            >
              <i slot="prefix" class="iconfont ic1">&#xe625;</i>
            </el-input>
            <img :src="imgurl" alt @click="lk" class="yz" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
          </el-form-item>
        </el-form>
      </div>
      <p class="p1">Copyright © 2019-2020 smartdormitory.cn All Rights Reserved.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    var checkAge = (rule, value, callback) => {
      if (!value) {
        return callback(new Error("验证码未填写"));
      } else {
        callback();
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入账号"));
      } else {
        if (this.ruleForm.checkPass !== "") {
          this.$refs.ruleForm.validateField("checkPass");
        }
        callback();
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === "") {
        callback(new Error("请输入密码"));
      } else {
        callback();
      }
    };
    return {
      input4: "",
      xs_one: false,
      xs_two: false,
      xs_three: false,
      username: "",
      password: "",
      code: "",
      imgurl: "",
      uuid: "",
      ruleForm: {
        pass: "",
        checkPass: "",
        age: ""
      },
      rules: {
        pass: [{ validator: validatePass, trigger: "blur" }],
        checkPass: [{ validator: validatePass2, trigger: "blur" }],
        age: [{ validator: checkAge, trigger: "blur" }]
      }
    };
  },
  created() {
    this.$axios({
      method: "GET",
      url: "http://122.112.253.28:8095/prod-api/captchaImage"
    }).then(result => {
      this.imgurl = "data:image/gif;base64," + result.data.data.img;
      this.uuid = result.data.data.uuid;
    });
  },
  methods: {
    lk() {
      this.sas();
    },
    sas() {
      this.$axios({
        method: "GET",
        url: "http://122.112.253.28:8095/prod-api/captchaImage"
      }).then(result => {
        this.imgurl = "data:image/gif;base64," + result.data.data.img;
        this.uuid = result.data.data.uuid;
      });
    },
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          this.onsubmit();
        } else {
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    onsubmit(values) {
      this.$axios({
        method: "post",
        url: "http://122.112.253.28:8095/prod-api/admin/login",
        data: {
          username: this.$data.ruleForm.pass,
          password: this.$data.ruleForm.checkPass,
          code: this.$data.ruleForm.age,
          uuid: this.uuid
        }
      }).then(result => {
        console.log(result);
        if (result.data.code == 200) {
          // sessionStorage.setItem("token", result.data.data.token);
          window.sessionStorage.token =result.data.data.tokenHead + " " + result.data.data.token;
          this.$router.push({
            path: "/About"
          });
        } else {
          this.$notify.error({
            title: "",
            message: "账号或密码错误"
          });
        }
      });
    }
  }
};
</script>
<style scoped>
@font-face {
  font-family: "iconfont"; /* project id 2457007 */
  src: url("//at.alicdn.com/t/font_2457007_zx7bkyt8mek.eot");
  src: url("//at.alicdn.com/t/font_2457007_zx7bkyt8mek.eot?#iefix")
      format("embedded-opentype"),
    url("//at.alicdn.com/t/font_2457007_zx7bkyt8mek.woff2") format("woff2"),
    url("//at.alicdn.com/t/font_2457007_zx7bkyt8mek.woff") format("woff"),
    url("//at.alicdn.com/t/font_2457007_zx7bkyt8mek.ttf") format("truetype"),
    url("//at.alicdn.com/t/font_2457007_zx7bkyt8mek.svg#iconfont") format("svg");
}
#app {
  width: 100vw;
  height: 100vh;
}
.login {
  height: 100vh;
  background-image: url("../assets/dormitorylogin.68a2ad9a.jpg");
  display: flex;
  justify-content: center;
  align-items: center;
  background-size: cover;
}
.login-form {
  width: 400px;
  box-sizing: inherit;
  font-size: 14px;
  background-color: white;
  border-radius: 6px;
  padding: 25px 0px 5px 0px;
}
.username {
  border: 1px solid red;
}
.log-h3bt {
  color: #707070;
  text-align: center;
  margin-bottom: 30px;
}
.ic1 {
  color: #bfc3cb;
  font-size: 14px;
  margin-left: 5px;
  float: left;
}
.ic2 {
  color: #bfc3cb;
  font-size: 18px;
  margin-left: 5px;
  float: left;
}
.log-name {
  width: 348px;
  margin-bottom: 22px;
  height: 36px;
  line-height: 36px;
  border: 1px solid #bfc3cb;
  margin: 0 auto;
  border-radius: 6px;
}
.mp {
  width: 350px;
  margin: 0 auto;
}
.log-pwd {
  width: 348px;
  margin-bottom: 22px;
  height: 36px;
  line-height: 36px;
  border: 1px solid #bfc3cb;
  margin: 0 auto;
  border-radius: 6px;
}
.log-yzm {
  float: left;
  width: 220px;
  margin-bottom: 22px;
  height: 36px;
  line-height: 36px;
  border: 1px solid #bfc3cb;
  margin: 0 auto;
  border-radius: 6px;
}
.yzm {
  height: 34px;
  border: none;
  outline: none;
  float: left;
  width: 100px;
  border-radius: 0 6px 6px 0px;
  margin-left: 5px;
  padding-left: 5px;
}
.username {
  height: 34px;
  border: none;
  outline: none;
  float: left;
  width: 313px;
  border-radius: 0 6px 6px 0px;
  margin-left: 5px;
  padding-left: 5px;
}
.yz {
  height: 36px;
  float: right;
  width: 110px;
  cursor: pointer;
}
.password {
  height: 34px;
  border: none;
  outline: none;
  float: left;
  width: 313px;
  border-radius: 0 6px 6px 0px;
  margin-left: 5px;
  padding-left: 5px;
}
.x {
  clear: both;
  width: 350px;
  margin: 0 auto;
  height: 21px;
}
.log-jz {
  width: 350px;
  margin-bottom: 22px;
  height: 36px;
  line-height: 36px;
  margin: 0 auto;
  border-radius: 6px;
}
.jz {
  border: 1px solid #dcdfe6;
}
.lab1 {
  color: #606266;
}
.submit {
  color: #fff;
  background-color: #1890ff;
  border: none;
  margin: 0 auto;
  font-size: 14px;
  width: 350px;
  cursor: pointer;
  height: 36px;
  line-height: 36px;
  display: block;
  border-radius: 4px;
  outline: none;
}
.p1 {
  height: 40px;
  line-height: 40px;
  position: fixed;
  bottom: 0;
  width: 100%;
  text-align: center;
  color: #fff;
  font-family: Arial;
  font-size: 12px;
  letter-spacing: 1px;
}
.sp1 {
  color: red;
  font-size: 12px;
  float: left;
  margin-top: 2px;
}
</style>
