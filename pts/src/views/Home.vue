<template>
  <div class="bac">
    <div class="login">
      <h1 class="log-h1">登录</h1>
      <div class="name">
        <el-input
          placeholder="请输入账户"
          v-model="login.userAccount"
          name="userAccount"
          class="in1"
          type="text"
        ></el-input>
      </div>
      <div class="name">
        <el-input placeholder="请输入密码" v-model="login.password" show-password class="in1"></el-input>
      </div>
      <el-checkbox v-model="login.checked" class="log-check">保持登录状态</el-checkbox>
      <el-row class="log-sub">
        <el-button type="primary" @click="submit" class="sub">登录</el-button>
      </el-row>
    </div>
  </div>
</template>
<script>
const QS = require("qs");
export default {
  data() {
    return {
      login: {
        userAccount: "admin",
        password: "",
        checked: true
      }
    };
  },
  methods: {
    // 登录
    submit() {
      let data = QS.stringify({
        userAccount: this.login.userAccount,
        passWord: this.login.password
      });
      this.$axios({
        method: "POST",
        url: "http://122.112.253.28:8085/api/manager/admin/login",
        data: data
      }).then(result => {
        console.log(result);
        if (this.login.password.length < 6) {
          this.$message.error("最少6位数");
        } else if (result.data.msg == "操作成功！") {
          sessionStorage.setItem("token", result.data.data.token);
          this.$message({
            message: "登录成功",
            type: "success"
          });
          this.$router.push({
            path: "/About"
          });
        } else {
          this.$message({
            message: "登录失败",
            type: "info"
          });
        }
      });
    }
  }
};
</script>
<style scoped>
.bac {
  width: 100vw;
  height: 100vh;
  background: url("../assets/1.jpg") no-repeat;
  background-size: 100% 100%;
}
.login {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  padding: 30px 30px 10px 30px;
  width: 380px;
  box-shadow: 0 2px 12px 0 rgb(0 0 0 / 10%);
  border-radius: 8px;
  background: #fff;
}
.log-h1 {
  text-align: center;
  font-size: 20px;
}
.name {
  background: rgba(0, 0, 0, 0.1);
  border-radius: 5px;
  color: #454545;
  margin-bottom: 18px;
  text-align: center;
}
.in1 {
  position: relative;
  font-size: 14px;
  line-height: 28px;
  width: 80%;
}
.log-check {
  color: #409eff;
  display: inline-block;
  padding-left: 10px;
  line-height: 19px;
  font-size: 14px;
  margin-bottom: 18px;
}
.sub {
  width: 100%;
  margin-bottom: 30px;
  font-size: 12px;
  /* height: 28px;
  line-height: 28px; */
  border-radius: 3px;
}
</style>