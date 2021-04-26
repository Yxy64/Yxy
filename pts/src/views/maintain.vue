<template>
  <div>
    <div class="nav-top">
      <label class="lab">姓名：</label>
      <Input placeholder="请输入姓名" style="width: 180px" v-model="query.realName" />
      <label class="lab">联系方式：</label>
      <Input placeholder="请输入联系方式" style="width: 180px" v-model="query.userPhone" />
      <label class="lab">所属代理商：</label>
      <Select style="width:200px" class="sele" v-model="query.agentId">
        <Option v-for="(item,key) in DaiLi" :key="key" :value="item.agentId">{{item.companyName}}</Option>
      </Select>
      <el-button
        type="primary"
        icon="el-icon-search"
        style="margin-left:20px;"
        @click="showSouSuo"
      >搜索</el-button>
      <el-button plain icon="el-icon-refresh" @click="showEmpty">重置</el-button>
    </div>

    <el-table ref="multipleTable" :data="showSJ" tooltip-effect="dark" style="width: 100%" border>
      <el-table-column type="selection" width="55"></el-table-column>
      <el-table-column label="序号">
        <template slot-scope="scope">{{ scope.row.messageId }}</template>
      </el-table-column>
      <el-table-column prop="realName" label="维护人员姓名"></el-table-column>
      <el-table-column prop="userPhone" label="联系电话"></el-table-column>
      <el-table-column prop="agentId" label="所属代理商"></el-table-column>
      <el-table-column prop="companyName" label="负责医院"></el-table-column>
      <el-table-column label="操作">
        <template>
          <el-button type="text">收件人列表</el-button>
          <el-button type="text" class="del">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
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
      DaiLi: [],
      showSJ: [],
      total: 0,
      size: 0,
      currentPage4: 1,
      query: {
        realName: "",
        userPhone: "",
        agentId: "",
        maintainType: "1"
      }
    };
  },
  mounted() {
    this.showDaiLi();
  },
  methods: {
    showDaiLi() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/agent/admin/getAllAgentList`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.DaiLi = result.data.data;
      });
    },
    // 查询
    showSouSuo() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/maintain-users/admin/getBackMaintainUsersList?offset=1&limit=10&realName=${this.query.realName}&userPhone=${this.query.userPhone}&agentId=${this.query.agentId}&maintainType=${this.query.maintainType}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data;
      });
    },
    // 重置
    showEmpty() {
      this.query = {
        realName: "",
        userPhone: "",
        agentId: ""
      };
    },
    // 显示
    showShuJu() {
      this.$axios({
        method: "GET",
        url: `http://122.112.253.28:8085/api/maintain-users/admin/getBackMaintainUsersList?offset=1&limit=10&maintainType=1`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.showSJ = result.data.data;
      });
    },
    // 分页
    showFenYe() {
      this.$axios({
        method: "GET",
        url:
          "http://122.112.253.28:8085/api/maintain-users/admin/getBackMaintainUsersList?offset=1&limit=10&maintainType=1",
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(result => {
        this.total = result.data.data.total;
        this.size = result.data.data.size;
        this.showSJ = result.data.data;
      });
    },
    handleSizeChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/maintain-users/admin/getBackMaintainUsersList?offset=1&limit=${val}`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data;
      });
    },
    handleCurrentChange(val) {
      this.$axios({
        method: "get",
        url: `http://122.112.253.28:8085/api/maintain-users/admin/getBackMaintainUsersList?offset=${val}&limit=10`,
        headers: {
          Authorization: window.sessionStorage.token
        }
      }).then(relt => {
        this.total = relt.data.data.total;
        this.size = relt.data.data.size;
        this.showSJ = relt.data.data;
      });
    },
  }
};
</script>
<style scoped>
.lab {
  padding: 0 12px;
}
.nav-top {
  margin-bottom: 20px;
}
.block {
  text-align: right;
  height: 50px;
  line-height: 50px;
  padding-top: 11px;
}
</style>