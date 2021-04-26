<template>
  <div class="div_d">
    <div class="div_d3">
      <div class="demo-input-suffix div_d1">
        用户昵称:
        <el-input placeholder="请输入用户昵称" v-model="query.nickName" class="el_input_1"></el-input>
      </div>

      <div class="demo-input-suffix div_d1">
        联系电话:
        <el-input placeholder="请输入联系方式" v-model="query.userPhone" class="el_input_1"></el-input>
      </div>

      <div class="demo-input-suffix div_d1">
        押金状态:
        <el-select v-model="query.isFlag" size="small" placeholder="请选择" clearable>
          <el-option label="已缴纳" value="2"></el-option>
          <el-option label="未缴纳" value="1"></el-option>
        </el-select>
      </div>

      <div class="demo-input-suffix div_d1">
        账号状态:
        <el-select v-model="query.isDeposit" size="small" placeholder="请选择" clearable>
          <el-option label="禁用" value="1"></el-option>
          <el-option label="正常" value="2"></el-option>
        </el-select>
      </div>
      <el-row class="el_row_1">
        <el-button type="primary" @click="showChaXun">查询</el-button>
        <el-button type="primary">批量发送短信</el-button>
      </el-row>
    </div>

    <div class="div_d4">
      <el-table ref="multipleTable" :data="showSJ" tooltip-effect="dark" style="width: 100%">
        <el-table-column type="selection" width="55"></el-table-column>
        <el-table-column type="index" label="序号"></el-table-column>
        <el-table-column prop="userNo" label="用户编号"></el-table-column>
        <el-table-column prop="nickName" label="用户昵称"></el-table-column>
        <el-table-column label="用户头像">
          <template slot-scope="scope">
            <img :src="scope.row.avatarUrl" alt />
          </template>
        </el-table-column>
        <el-table-column prop="userPhone" label="手机号"></el-table-column>
        <el-table-column prop="cTime" label="注册日期"></el-table-column>
        <el-table-column prop="isFlag" label="状态"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="text" @click="showUpdate(scope.row.userId)">启用</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <div class="block">
      <el-pagination
        @size-change="handleSizeChange"
        background
        @current-change="handleCurrentChange"
        :current-page="currentPage4"
        :page-sizes="[10, 20, 50, 100]"
        :page-size="10"
        layout="total, sizes, prev, pager, next, jumper"
        :total="total"
      ></el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      total: 0,
      size: 0,
      currentPage4: 1,
      query: {
        nickName: "",
        userPhone: "",
        isFlag: "",
        isDeposit: ""
      },
      xiala1: [],
      xiala2: [],
      showSJ: []
    };
  },
  mounted() {},
  created() {
    this.showFenYe();
  },
  methods: {
    handleSizeChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/users/admin/getBackUsersList?offset=1&limit=${val}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data.records;
      });
    },
    handleCurrentChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/users/admin/getBackUsersList?offset=${val}&limit=10`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data.records;
      });
    },
    // 查询
    showChaXun() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/users/admin/getBackUsersList?offset=1&limit=10&nickName=${this.query.nickName}&userPhone=${this.query.userPhone}&isDeposit=${this.query.isFlag}&isFlag=${this.query.isDeposit}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data.records;
      });
    },
    showFenYe() {
      this.$axios({
        method: "GET",
        url:
          "http://122.112.253.28:8085/api/users/admin/getBackUsersList?offset=1&limit=10",
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.total = result.data.data.total;
        this.size = result.data.data.size;
        this.showSJ = result.data.data.records;
      });
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    // 修改
    showUpdate(userId) {}
  }
};
</script>

<style scoped>
.div_d2 {
  height: 870px;
}
.el_input_1 {
  width: 190px;
  height: 28px;
}
.div_d1 {
  width: 300px;
  height: 45px;
  float: left;
}
.div_d3 {
  height: 70px;
}
.el_row_1 {
  float: left;
}
.block {
  text-align: right;
  height: 50px;
  line-height: 50px;
  padding-top: 11px;
}
</style>